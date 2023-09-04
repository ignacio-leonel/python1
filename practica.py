#lo primero que hice fue crear dos listas una con los meses y otra con la ganancia mensual
#decidi hacerlo de esta forma me parecio la mas conveniente al tener ya los datos, de haberlos tenido que consumir
#de otro lado hubiera puesto una funcion que lo haga y ubique en la lista, salvando con 0 en los .null para evitar errores

meses =["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
sueldos =[300,300,300,300,300,300,500,500,500,500,700,700]

#el primer pedido fue calcular el promedio de ganancia de Juan, lo hice de la siguiente forma

#primero definí la funcion que lo haría
    
def calcular_promedio(sueldos):
    total = sum(sueldos)
    cantidad_elementos = len(sueldos)
    promedio = total / cantidad_elementos
    return promedio
#luego acá la llamé para que lo imprima por pantalla

promedio = calcular_promedio(sueldos)
print(f"El promedio de ganancia mensual fue  de: {promedio} dólares")


#el pedido siguiente era mostrar si el sueldo era alto, bajo o "estaba bien"
#decidi hacer un bucle For In que  recorriera ambas listas a la vez
for mes,sueldo in zip (meses,sueldos):

    print(f"en el mes de {mes} el sueldo fue de {sueldo}")
#y el condicional que luego de evaluar cada posicion de las listas, arroje la evaluacion mensual
    if sueldo<300:
        print("el sueldo fue bajo"); 
    elif sueldo>=300 and sueldo<900 :
        print("el sueldo esta bien");
    else:
      print("el sueldo es alto");
    
    