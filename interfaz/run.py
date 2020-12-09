from flask import Flask, render_template
from flask import request
import os
diccionario={}

def parseo(linea):
	palabra=""
	i=0
	primeraves=False
	primerapalabra=""
	while i< len(linea):
		if linea[i]!='\t' and linea[i]!='\n':
			palabra+=linea[i]
		else:
			if primeraves==False:
				diccionario[palabra]=[]
				primerapalabra=palabra
				primeraves=True

			else:
				diccionario[primerapalabra].append(palabra)
			while  i<len(linea) and linea[i]==' ':
				i+=1
			palabra=""
		#print(linea[i])
		i+=1


def archivo(archivo):
	file=open(archivo,'r')
	for linea in file:
		print(linea)
		parseo(linea)
	#print(diccionario)
archivo('/home/etamotu/interfaz/part-r-00000.txt')
archivo('/home/etamotu/interfaz/part-r-00001.txt')
archivo('/home/etamotu/interfaz/part-r-00002.txt')

app = Flask(__name__)
posts = []
resultado=[]
@app.route('/', methods=["GET",'POST'])
def index():
	global resultado,diccionario
	if request.method == 'POST':
			name=request.form['busqueda']
			print("name",name)
			if name in diccionario:
				resultado=diccionario[name]
				resultado=resultado[:-1]
			print("resultado",resultado)
			return render_template("listar.html", resultado=resultado,tamano=len(resultado))
	return render_template("base.html")

@app.route("/p/<string:slug>/")
def show_post(slug):
    return "Mostrando el post {}".format(slug)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
	global resultado,diccionario
	if request.method == 'POST':
                        name=request.form['busqueda']
                        print("name",name)
                        if name in diccionario:
                                resultado=diccionario[name]
                        print("resultado",resultado)
                        #return render_template("listar.html",resultado)
	return render_template("base.html")

@app.route("/listar/", methods=["GET", "POST"])
def listar():
	global resultado,diccionario
	indice=0
	if request.method == 'POST':
                        name=request.form['busqueda']
                        print("name",name)
                        if name in diccionario:
                                resultado=diccionario[name]
				resultado=resultado[:-1]
                        print("resultado",resultado)
			tamano=len(resultado)
	return render_template("listar.html", resultado=resultado, tamano=tamano )

app.run(host='0.0.0.0')
