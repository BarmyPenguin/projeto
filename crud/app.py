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
	__tablename__ = 'registro'
	_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	r_nome = db.Column(db.String)
	r_empresa = db.Column(db.String)
	r_cep = db.Column(db.String)
	r_endereco = db.Column(db.String)
	r_telefone = db.Column(db.String)
	r_email = db.Column(db.String)
	r_password = db.Column(db.String) 
	

	def __init__(self, r_nome, r_empresa, r_cep, r_endereco, r_telefone, r_email, r_password):
		self.r_nome = r_nome
		self.r_empresa = r_empresa
		self.r_cep = r_cep
		self.r_endereco = r_endereco
		self.r_telefone = r_telefone
		self.r_email = r_email
		self.r_password = r_password

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
	return render_template('registrar.html')

@app.route("/telaPrincipal")
def telaPrincipal():
	try:
		if session['logged_in'] == True:
			return render_template('telaPrincipal.html')
	except (KeyError):		
		return redirect(url_for("home"))
	

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
	if request.method == "POST":
		nome = request.form.get("nome")
		telefone =  request.form.get("telefone")
		cpf = request.form.get("cpf")
		email = request.form.get("email")
		senha = request.form.get("senha")

		if nome and telefone and cpf and email and senha:
			p = Pessoa(nome, telefone, cpf, email, senha)
			db.session.add(p)
			db.session.commit()

	return redirect(url_for("index"))

@app.route("/lista")
def lista():
	pessoas = Pessoa.query.all()
	return render_template("lista.html", pessoas=pessoas)

@app.route("/teste")
def teste():
	registros = Registro.query.all()
	return render_template("teste.html", registros=registros)

@app.route("/excluir/<int:id>")
def excluir(id):
	pessoa = Pessoa.query.filter_by(_id=id).first()
	db.session.delete(pessoa)
	db.session.commit()
	pessoas = Pessoa.query.all()
	return render_template("lista.html", pessoas=pessoas)

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
	pessoa = Pessoa.query.filter_by(_id=id).first()
	
	if request.method == "POST":
		nome = request.form.get("nome")
		telefone = request.form.get("telefone")
		cpf = request.form.get("cpf")
		email = request.form.get("email")

		if nome and telefone and cpf and email:
			pessoa.nome = nome
			pessoa.telefone = telefone
			pessoa.cpf = cpf
			pessoa.email = email

			db.session.commit()

			return redirect(url_for("lista"))

	return render_template("atualizar.html", pessoa=pessoa)


@app.route("/login", methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':

		femail = request.form["username"]
		print(femail)
		fsenha  = request.form["password"]
		print(fsenha)
		pessoa = Registro.query.filter_by(r_email=femail).first()
		print(pessoa)
		


		if pessoa.r_password !=  fsenha:
		#if request.form["username"] != "admin" or request.form["password"] != "admin":
			error = 'Login invalido. Por favor, tente novamente.'
			return redirect(url_for('home'))

		else:
			session['logged_in'] = True
			flash('Você está logado!')
			return redirect(url_for('telaPrincipal'))

	return render_template('telaPrincipal.html', error=error)

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
	if request.method == "POST":
		r_nome = request.form.get("r_nome")
		r_empresa = request.form.get("r_empresa")
		r_cep = request.form.get("r_cep")
		r_endereco = request.form.get("r_endereco")
		r_telefone =  request.form.get("r_telefone")
		r_email = request.form.get("r_email")
		r_password = request.form.get("r_password")

		if r_nome and r_empresa and r_cep and r_endereco and r_telefone and r_email and r_password:
			r = Registro(r_nome, r_empresa, r_cep, r_endereco, r_telefone, r_email, r_password)
			db.session.add(r)
			db.session.commit()

	return redirect(url_for("home"))

#@app.route("/telaPrincipal")



@app.route("/sair/<int:id>", methods=['GET', 'POST'])
def sair(id):
	session.pop('logged_in', None)
	flash('Você está deslogado!')
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.run(debug=True)