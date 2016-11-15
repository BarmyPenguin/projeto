#coding:utf-8
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
import sys

import flask_login

app = Flask(__name__)
app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class Registro(db.Model):
	__tablename__ ='registro'
	_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	nome = db.Column(db.String)
	empresa = db.Column(db.String)
	cep = db.Column(db.String)
	endereco = db.Column(db.String)
	telefone = db.Column(db.String)
	email = db.Column(db.String)
	password = db.Column(db.String)
	person = db.Column(db.Integer) 
	
	def __init__(self, nome, empresa, cep, endereco, telefone, email, password, person):
		self.nome = nome
		self.empresa = empresa
		self.cep = cep
		self.endereco = endereco
		self.telefone = telefone
		self.email = email
		self.password = password
		self.person = person

class Ideia(db.Model):
	__tablename__='ideia'
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nomefun = db.Column(db.String)
	area = db.Column(db.String)
	ideiapara = db.Column(db.String)
	tipo = db.Column(db.String)
	ideia = db.Column(db.String)
	emailfunc = db.Column(db.String, db.ForeignKey("registro.email"))
		
	def __init__(self, nomefun, area, ideiapara, tipo, ideia, emailfunc):
#	def __init__(self, nomefun, area, ideiapara, tipo, ideia):
		self.nomefun = nomefun
		self.area = area
		self.ideiapara = ideiapara
		self.tipo = tipo
		self.ideia = ideia
		self.emailfunc = emailfunc

db.create_all()

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
	users = Registro.query.all()

	# pesquisar se id existe
	for pessoa in users:
		if pessoa.email == email:
			user = User()
			user.id = pessoa.email
			user.pessoa = pessoa
			return user

	return

# TODO: entender melhor quando eh chamado...
@login_manager.request_loader
def request_loader(request):
	email = request.form.get('email')

	users = Registro.query.all()

	for pessoa in users:
		if pessoa.email == email:
			user = User()
			user.id = pessoa.email
			user.pessoa = pessoa
			# DO NOT ever store passwords in plaintext and always compare password
			# hashes using constant-time comparison!
			user.is_authenticated = request.form['pw'] == user.pessoa.email
			return user	
	
	return

@login_manager.unauthorized_handler
def unauthorized_handler():
	error = 'Login invalido. Por favor, tente novamente.'
	return render_template("home.html", erro=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = 'Login invalido. Por favor, tente novamente.'
	if request.method == 'GET':
		return render_template("home.html", erro=error)
	else:
		try:
			femail = request.form['username']
			fsenha = request.form['password']
			pessoa = Registro.query.filter_by(email=femail).first()
				
			if pessoa.password == fsenha:
				user = User()
				user.id = femail
				user.pessoa = pessoa
				flask_login.login_user(user)
				if user.pessoa.person == 2:
					return redirect(url_for('telaPrincipal'))
				elif user.pessoa.person == 1:
					return redirect(url_for('ideiasteste'))
		except:
			return render_template("home.html", erro=error)

	return render_template("home.html", erro=error)

@app.route('/status')
def status():
	if flask_login.current_user.is_anonymous:
		return 'Not logged'
	else:
		return 'Logged in as: ' + flask_login.current_user.pessoa.email + " " + str(flask_login.current_user.pessoa.person)
	
@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect("/home", code=302)

@app.route("/")
def home_redirect():
	return redirect("/home", code=302)

@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/cadastrar")
#@flask_login.login_required
def cadastrar():
	return render_template('cadastro.html')

@app.route("/registro")
def registro():
	return render_template('registro.html')

@app.route("/telaPrincipal", methods=['GET', 'POST'])
@flask_login.login_required
def telaPrincipal():
	return render_template('telaPrincipal.html')

@app.route("/cadastrarideia", methods=['GET', 'POST'])
@flask_login.login_required
def cadastrarideia():
	if request.method == "POST":
		nomefun = request.form.get("nomefun")
		area = request.form.get("area")
		ideiapara = request.form.get("ideiapara")
		tipo = request.form.get("tipo")
		ideia = request.form.get("ideia")
		emailfunc = flask_login.current_user.pessoa.email

		if nomefun and area and ideiapara and tipo and ideia  and emailfunc:
			i = Ideia(nomefun, area, ideiapara, tipo, ideia, emailfunc)
			db.session.add(i)
			db.session.commit()

#		i = Ideia(request.form['nomefun'], request.form['area'], request.form['ideiapara'], request.form['tipo'], request.form['ideia'], flask_login.current_user.pessoa.email)
		
	return redirect(url_for('index'))
	
@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
	if request.method == "POST":
		nome = request.form.get("nome")
		empresa = request.form.get("empresa")
		cep = request.form.get("cep")
		endereco = request.form.get("endereco")
		telefone =  request.form.get("telefone")		
		email = request.form.get("email")
		password = request.form.get("password")
		person = 1

		if nome and empresa and cep and endereco and telefone and email and password and person:
			p = Registro(nome, empresa, cep, endereco, telefone, email, password, person)
			db.session.add(p)
			db.session.commit()

	return redirect(url_for("cadastrar"))

@app.route("/ideiasteste")
@flask_login.login_required
def ideiasteste():
	ideias = Ideia.query.all()
	return render_template("ideiasteste.html", ideias=ideias)

@app.route("/teste")
@flask_login.login_required
def teste():
	registros = Registro.query.all()
	return render_template("teste.html", registros=registros, usuario=flask_login.current_user.pessoa.person )

@app.route("/excluirideia/<int:id>")
@flask_login.login_required
def excluirideia(id):
	ide = Ideia.query.filter_by(_id=id).first()
	db.session.delete(ide)
	db.session.commit()
	idei = Ideia.query.all()
	return render_template("ideiasteste.html", idei=idei)

@app.route("/excluir/<int:id>")
@flask_login.login_required
def excluir(id):
	pessoa = Registro.query.filter_by(_id=id).first()
	db.session.delete(pessoa)
	db.session.commit()
	pessoas = Registro.query.all()
	return render_template("teste.html", pessoas=pessoas)

@app.route("/atualizarideia/<int:id>", methods=['GET', 'POST'])
@flask_login.login_required
def atualizarideia(id):
	ide = Ideia.query.filter_by(_id=id).first()
	
	if request.method == "POST":
		nomefun = request.form.get("nomefun")
		area = request.form.get("area")
		ideapara = request.form.get("ideiapara")
		tipo = request.form.get("tipo")
				
		if nomefun and area and ideiapara and tipo:
			ide.nomefun = nomefun
			ide.area = area
			ide.ideiapara = ideiapara
			ide.tipo = tipo
						
			db.session.commit()

			return redirect(url_for("ideiasteste"))

	return render_template("atualizarideia.html", ide=ide)	

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
@flask_login.login_required
def atualizar(id):
	pessoa = Registro.query.filter_by(_id=id).first()
	
	if request.method == "POST":
		nome = request.form.get("nome")
		empresa = request.form.get("empresa")
		cep = request.form.get("cep")
		endereco = request.form.get("endereco")
		telefone = request.form.get("telefone")
		email = request.form.get("email")

		if nome and empresa and cep and endereco and telefone and email:
			pessoa.nome = nome
			pessoa.empresa = empresa
			pessoa.cep = cep
			pessoa.endereco = endereco
			pessoa.telefone = telefone
			pessoa.email = email

			db.session.commit()

			return redirect(url_for("teste"))

	return render_template("atualizar.html", pessoa=pessoa)

@app.route("/registrar", methods=['GET', 'POST'])
@flask_login.login_required
def registrar():
	if request.method == "POST":
		nome = request.form.get("nome")
		empresa = request.form.get("empresa")
		cep = request.form.get("cep")
		endereco = request.form.get("endereco")
		telefone =  request.form.get("telefone")		
		email = request.form.get("email")
		password = request.form.get("password")
		person = 2

		if nome and empresa and cep and endereco and telefone and email and password and person:
			p = Registro(nome, empresa, cep, endereco, telefone, email, password, person)
			db.session.add(p)
			db.session.commit()
		
	return redirect(url_for('teste'))

if __name__ == '__main__':
	app.run(debug=True)
	#app.run(host="0.0.0.0", port=80)
