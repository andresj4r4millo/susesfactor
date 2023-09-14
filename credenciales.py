# Definir las variables antes del bucle
usuario = ""
contraseña = ""

# Abre el archivo en modo lectura
cone=0
with open("credenciales.txt", "r") as archivo:
    for linea in archivo:
        if cone==0:
            usuario=linea
        elif cone==1:
            contraseña=linea
        cone+=1
print("Usuario:", usuario)
print("Contraseña:", contraseña)


