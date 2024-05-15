# No tiene un par key-velue, por lo que es un set, conjunto
set_countries = {"col", "mex", "bol"}
print(set_countries)
print(type(set_countries))

# Si se repite algún elemento, al imprimir se elimina
set_numbers ={1, 2, 2, 443, 35}
print(set_numbers)

# El set puede incluir varios tipos de datos, se ordena solo
set_types = {1, "hola", False, 12.9}
print(set_types)

# Se puede crear a partir de un string
set_from_string = set("hoola")
print(set_from_string)

# También se puede crear a partir de una tupla
set_from_tuples = set(("abc", "cbv", "as", "abc"))
print(set_from_tuples)

# También a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

# Si se quiere convertir este set unico a lista, se hace así: 
unique_numbers = list(set_numbers)
print(unique_numbers)
