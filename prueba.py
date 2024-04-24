import json
with open("jsonok.json") as fichero:
    jsonok=json.load(fichero)

hombres = []
mujeres = []

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

buscador = "A"



ide = "101"

for i in jsonok["tienda"]["categorias"]["zapatillas"]["hombres"]["productos"]:
    if int(ide) == i["id"] :
        for e in i["detalles"]["tallas"]:
            print(e)
        for e in i["detalles"]["colores"]:
            print(e)

for i in jsonok["tienda"]["categorias"]["zapatillas"]["mujeres"]["productos"]:
    if int(ide) == i["id"] :
        print(i)


for i in jsonok["tienda"]["categorias"]["camisetas"]["hombres"]["productos"]:
    if int(ide) == i["id"] :
        print(i)

for i in jsonok["tienda"]["categorias"]["camisetas"]["mujeres"]["productos"]:
    if int(ide) == i["id"] :
        print(i)


for i in jsonok["tienda"]["categorias"]["sudaderas"]["hombres"]["productos"]:
    if int(ide) == i["id"] :
        print(i)

for i in jsonok["tienda"]["categorias"]["sudaderas"]["mujeres"]["productos"]:
    if int(ide) == i["id"] :
        print(i)

for i in jsonok["tienda"]["categorias"]["pantalones"]["hombres"]["productos"]:
    if int(ide) == i["id"] :
        print(i)

for i in jsonok["tienda"]["categorias"]["pantalones"]["mujeres"]["productos"]:
    if int(ide) == i["id"] :
        print(i)