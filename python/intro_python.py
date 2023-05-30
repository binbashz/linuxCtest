#variables

nombre_libro = "Harry Potter"
print(nombre_libro)

#strings

descripcion_libro = """
 libro de magia y ficcion 
 la quidiwch etc
""" 

print(nombre_libro, descripcion_libro) #imprimendo valores de vairables

print(len(nombre_libro)) #imprmie la longitud de la variable

print(nombre_libro[0]) #con los parentesis rectos , accedemos a algun caracter en particular por indice , 0 seria H
print(nombre_libro[0:5]) #cortamos el string del nombre del libro, obtenemos una palabra , dandole su longitud,ej desde 0 : a 5
print(nombre_libro[6:]) #aca solo pasamos valor de la izquierda, auotomaticamente, como python rellena hasta el final 
print(nombre_libro[:7]) #solo pasamos el valor de la derecha, entonces indicamos, que asuma el valor por defecto, es 0, com la linea 18
print(nombre_libro[:]) #esto genera una copia del string , o imprime todo. no le pasamos valores,  el valor de la izq sera 0 y el de 	
						#la derech su uiltimo por defecto, sera la longitud completa del string 


# format string

nombre = "Mauricio"
apellido = "Correa"

#la f es el operador de formateo de strings
nombre_completo = f"{nombre} {apellido}" 
#esto esta escrito dentro de un operador de formateo, la f 
# con ese operador se le pueden dar mas expresiones, com un indice etc. 
print(nombre_completo)

# metodos strings 

cacao = "venezuelA"
print(cacao.upper())  #upper toma el string y lo transforma todo a mayusucla
print(cacao.lower())  #lower pasa todas las letras a miniscula, esta es una de las funciones que pueden tener los strings


