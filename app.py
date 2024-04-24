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

    for i in jsonok["tienda"]["categorias"]["zapatillas"]["hombres"]["productos"]:
        zapatillas = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
        hombres.append(zapatillas)

    for i in jsonok["tienda"]["categorias"]["zapatillas"]["mujeres"]["productos"]:
        zapatillas = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
        mujeres.append(zapatillas)


    for i in jsonok["tienda"]["categorias"]["camisetas"]["hombres"]["productos"]:
        zapatillas = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
        hombres.append(zapatillas)

    for i in jsonok["tienda"]["categorias"]["camisetas"]["mujeres"]["productos"]:
        zapatillas = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
        mujeres.append(zapatillas)


    for i in jsonok["tienda"]["categorias"]["sudaderas"]["hombres"]["productos"]:
        zapatillas = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
        hombres.append(zapatillas)

    for i in jsonok["tienda"]["categorias"]["sudaderas"]["mujeres"]["productos"]:
        zapatillas = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
        mujeres.append(zapatillas)

    for i in jsonok["tienda"]["categorias"]["pantalones"]["hombres"]["productos"]:
        zapatillas = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
        hombres.append(zapatillas)

    for i in jsonok["tienda"]["categorias"]["pantalones"]["mujeres"]["productos"]:
        zapatillas = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
        mujeres.append(zapatillas)

    sumalista = hombres+mujeres

    for i in sumalista:
        if i["nombre"].startswith(buscador):
            final = {"id": i["id"],"nombre": i["nombre"], "marca": i["marca"], "precio": i["precio"]}
            sumalista2.append(final)
    

    return render_template("tabla.html",resultado=sumalista2,buscador=buscador)

@app.route('/details/<identificador>')
def detalles(identificador):

    listaTallas = []
    listaColores = []

    for i in jsonok["tienda"]["categorias"]["zapatillas"]["hombres"]["productos"]:
        if int(identificador) == i["id"] :
            for e in i["detalles"]["tallas"]:
                tallas = {"tallas": e}
                listaTallas.append(tallas)
            for e in i["detalles"]["colores"]:
                colores = {"colores": e}
                listaColores.append(colores)

    for i in jsonok["tienda"]["categorias"]["zapatillas"]["mujeres"]["productos"]:
        if int(identificador) == i["id"] :
            for e in i["detalles"]["tallas"]:
                tallas = {"tallas": e}
                listaTallas.append(tallas)
            for e in i["detalles"]["colores"]:
                colores = {"colores": e}
                listaColores.append(colores)

    for i in jsonok["tienda"]["categorias"]["camisetas"]["hombres"]["productos"]:
        if int(identificador) == i["id"] :
            for e in i["detalles"]["tallas"]:
                tallas = {"tallas": e}
                listaTallas.append(tallas)
            for e in i["detalles"]["colores"]:
                colores = {"colores": e}
                listaColores.append(colores)

    for i in jsonok["tienda"]["categorias"]["camisetas"]["mujeres"]["productos"]:
        if int(identificador) == i["id"] :
            for e in i["detalles"]["tallas"]:
                tallas = {"tallas": e}
                listaTallas.append(tallas)
            for e in i["detalles"]["colores"]:
                colores = {"colores": e}
                listaColores.append(colores)

    for i in jsonok["tienda"]["categorias"]["sudaderas"]["hombres"]["productos"]:
        if int(identificador) == i["id"] :
            for e in i["detalles"]["tallas"]:
                tallas = {"tallas": e}
                listaTallas.append(tallas)
            for e in i["detalles"]["colores"]:
                colores = {"colores": e}
                listaColores.append(colores)   

    for i in jsonok["tienda"]["categorias"]["sudaderas"]["mujeres"]["productos"]:
        if int(identificador) == i["id"] :
            for e in i["detalles"]["tallas"]:
                tallas = {"tallas": e}
                listaTallas.append(tallas)
            for e in i["detalles"]["colores"]:
                colores = {"colores": e}
                listaColores.append(colores)

    for i in jsonok["tienda"]["categorias"]["pantalones"]["hombres"]["productos"]:
        if int(identificador) == i["id"] :
            for e in i["detalles"]["tallas"]:
                tallas = {"tallas": e}
                listaTallas.append(tallas)
            for e in i["detalles"]["colores"]:
                colores = {"colores": e}
                listaColores.append(colores)

    for i in jsonok["tienda"]["categorias"]["pantalones"]["mujeres"]["productos"]:
        if int(identificador) == i["id"] :
            for e in i["detalles"]["tallas"]:
                tallas = {"tallas": e}
                listaTallas.append(tallas)
            for e in i["detalles"]["colores"]:
                colores = {"colores": e}
                listaColores.append(colores)


    return render_template("details.html",listaTallas=listaTallas,listaColores=listaColores)


app.run("0.0.0.0",5000,debug=True)

