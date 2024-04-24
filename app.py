from flask import Flask, render_template,request
app = Flask(__name__)	

import json
with open("jsonok.json") as fichero:
    jsonok=json.load(fichero)

@app.route('/')
def inicio():
    return render_template("principal.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")


@app.route('/tabla',methods=["POST"])
def tabla():
    buscador=request.form.get("busqueda")

    hombres = []
    mujeres = []
    sumalista2 = []

    categorias = ["zapatillas", "camisetas", "sudaderas", "pantalones"]

    for categoria in categorias:
        for genero in ["hombres", "mujeres"]:
            for producto in jsonok["tienda"]["categorias"][categoria][genero]["productos"]:
                zapatillas = {
                    "id": producto["id"],
                    "nombre": producto["nombre"],
                    "marca": producto["marca"],
                    "precio": producto["precio"]
                }
                if genero == "hombres":
                    hombres.append(zapatillas)
                else:
                    mujeres.append(zapatillas)

    sumalista = hombres + mujeres

    for i in sumalista:
        if i["nombre"].startswith(buscador):
            sumalista2.append(i)
    

    return render_template("tabla.html",resultado=sumalista2,buscador=buscador)

@app.route('/details/<identificador>')
def detalles(identificador):

    listaTallas = []
    listaColores = []

    categorias = ["zapatillas", "camisetas", "sudaderas", "pantalones"]
    generos = ["hombres", "mujeres"]

    for categoria in categorias:
        for genero in generos:
            productos = jsonok["tienda"]["categorias"][categoria][genero]["productos"]
            for producto in productos:
                if int(identificador) == producto["id"]:
                    detalles_producto = producto["detalles"]
                    for talla in detalles_producto["tallas"]:
                        listaTallas.append({"tallas": talla})
                    for color in detalles_producto["colores"]:
                        listaColores.append({"colores": color})

    return render_template("details.html", listaTallas=listaTallas, listaColores=listaColores)


app.run("0.0.0.0",5000,debug=True)

