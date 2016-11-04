#coding:utf-8
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
import sys
#from flask.ext.login import LoginManager
#from flask.ext.openid import OpenID
#from config import basedir
#import os

#lm = LoginManager()
#lm.init_app(app)
#oid = OpenID(app, os.path.join(basedir, 'tmp')) 

app = Flask(__name__)
app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Pessoa(db.Model):
	__tablename__='cliente'
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String)
	telefone = db.Column(db.String)
	cpf = db.Column(db.String)
	email = db.Column(db.String)
	senha = db.Column(db.String)


	def __init__(self, nome, telefone, cpf, email, senha):
		self.nome = nome
		self.telefone = telefone
		self.cpf = cpf
		self.email = email
		self.senha = senha

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
		
	def __init__(self, nomefun, area, ideiapara, tipo, ideia):
		self.nomefun = nomefun
		self.area = area
		self.ideiapara = ideiapara
		self.tipo = tipo
		self.ideia = ideia
		
db.create_all()

@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/cadastrar")
def cadastrar():
	return render_template('cadastro.html')

@app.route("/registro")
def registro():
	return render_template('registro.html')

@app.route("/telaAdm", methods=['GET', 'POST'])
def telaAdm():
	try:
		if session['logged_in'] == True:
			return render_template('telaAdm.html')
	except (KeyError):		
		return redirect(url_for("home"))

@app.route("/telaPrincipal", methods=['GET', 'POST'])
def telaPrincipal():
	try:
		if session['logged_in'] == True:
			return render_template('telaPrincipal.html')
	except (KeyError):		
		return redirect(url_for("home"))

@app.route("/cadastrarideia", methods=['GET', 'POST'])
def cadastrarideia():
	if request.method == "POST":
		i = Ideia(request.form['nomefun'], request.form['area'], request.form['ideiapara'], request.form['tipo'], request.form['ideia'])
		db.session.add(i)
		db.session.commit()

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

@app.route("/lista")
def lista():
	pessoas = Pessoa.query.all()
	return render_template("lista.html", pessoas=pessoas)

@app.route("/ideiasteste")
def ideiasteste():
	ideias = Ideia.query.all()
	return render_template("ideiasteste.html", ideias=ideias)

@app.route("/teste")
def teste():
	registros = Registro.query.all()
	return render_template("teste.html", registros=registros)

@app.route("/excluirideia/<int:id>")
def excluirideia(id):
	ide = Ideia.query.filter_by(_id=id).first()
	db.session.delete(ide)
	db.session.commit()
	idei = Ideia.query.all()
	return render_template("ideiasteste.html", idei=idei)

@app.route("/excluir/<int:id>")
def excluir(id):
	pessoa = Registro.query.filter_by(_id=id).first()
	db.session.delete(pessoa)
	db.session.commit()
	pessoas = Registro.query.all()
	return render_template("teste.html", pessoas=pessoas)

@app.route("/atualizarideia/<int:id>", methods=['GET', 'POST'])
def atualizarideia(id):
	ide = Ideia.query.filter_by(_id=id).first()
	
	if request.method == "POST":
		nomefun = request.form.get("nomefun")
		area = request.form.get("area")
		ideapara = request.form.get("ideiapara")
		tipo = request.form.get("tipo")
		ideia = request.form.get("ideia")
		
		if nomefun and area and ideiapara and tipo and ideia:
			ide.nomefun = nomefun
			ide.area = area
			ide.ideiapara = ideiapara
			ide.tipo = tipo
			ide.ideia = ideia
			
			db.session.commit()

			return redirect(url_for("ideiasteste"))

	return render_template("atualizarideia.html", ide=ide)	

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
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

@app.route("/login", methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		try:
			femail = request.form["username"]
			fsenha  = request.form["password"]
			pessoa = Registro.query.filter_by(email=femail).first()
			
			
			if pessoa.password !=  fsenha:
				error = 'Login invalido. Por favor, tente novamente.'
				return render_template("home.html", erro=error)
			
			elif pessoa.person == 1:
				#pessoa.authenticated = True
				session['logged_in'] = True
				flash('Você está logado!')
				#login_user(pessoa, remember=True)
				return redirect(url_for('telaAdm'))
			else:
				#pessoa.authenticated = True
				session['logged_in'] = True
				flash('Você está logado!')
				#login_user(pessoa, remember=True)
				return redirect(url_for('telaPrincipal'))

		except:		
			error = 'Login invalido. Por favor, tente novamente.'
			return render_template("home.html", erro=error)

		
		
	return render_template('telaPrincipal.html', error=error)

@app.route("/registrar", methods=['GET', 'POST'])
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
		
	return redirect(url_for('home'))

@app.route("/sair/<int:id>", methods=['GET', 'POST'])
def sair(id):
	#user = current_user
	#user.authenticated = False
	#db.session.add(user)
	#db.session.commit()
	#logout_user()
	session.pop('logged_in', None)
	flash('Você está deslogado!')
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)
	#app.run(host="0.0.0.0", port=80)
