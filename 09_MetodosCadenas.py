cadena1 = "Hola soy Santiago"

cadena2 = "Bienvenido Maquinola"

cadena3 = "PROGRAMA PARA LA INTERPRETACION DE TEXTOS"

cadena4 = "9532895623568"

cadena5 = "Hola como estas 777"

cadena6 = "Parrafo, para, separar, y reemplazar palabras"

print(dir(4))


mayusculas = cadena1.upper()  #convierte en mayusculas

minusculas = cadena2.lower()  #Convierte en minusculas

primera_mayuscula = cadena3.capitalize() #Convierte la primera en mayuscula si esta en minuscula

busqueda_find = cadena1.find("l") #Se usa para buscar en que posicion se encuentra una cadena o un caracter

#Si no encuentra el valor que le especificamos, nos devolvera -1

busqueda_index = cadena2.index("o")#Este tambien se usa para encontrar datos, pero a diferencia de find, si index no encuentra el caracter especificado tirara un error

es_numerico = cadena4.isnumeric()#se usa para saber si en una cadena de texto hay solo numeros, si hay letras u otros caracteres se devuelve false

es_alphanumerico = cadena5.isalpha()#Se usa para detectar si hay caracteres alphanumericos, es decir, de la A a la Z, no cuenta espacios,numeros,caracteres especiales etc

contar_coincidencias = cadena1.count("o")#Se usa para contar cuantas veces aparecen uno o varios caracteres en la cadena de texto especificada

contar_caracteres = len(cadena2)#Detecta la cantidad de caracteres y espacios que tiene la cadena

empieza_con = cadena3.startswith("O")#detecta si la letra o caracter especificado es el mismo con el que empieza la cadena

termina_con = cadena2.endswith("l")#detecta si la letra o caracter especificado es el mismo con el que empieza la cadena

cadena_nueva = cadena6.replace(",","I")#Esta funcion reemplaza el caracter que le indiquemos en la primera comilla por el caracter que le indiquemos en la segunda comilla

cadena_separada = cadena6.split(",")#separa las palabras con el caracter que le indiquemos entre comillas

print(mayusculas)  

print(minusculas)

print(primera_mayuscula)

print(busqueda_find)

print(es_numerico)

print(es_alphanumerico)

print(contar_coincidencias)

print(contar_caracteres)

print(empieza_con)

print(termina_con)

print(cadena_nueva)

print(cadena_separada)