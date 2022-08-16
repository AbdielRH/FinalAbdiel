Diccionario = {"codigo": ["001", "002", "003"],
          "nombre": ["Angel", "Abdiel", "Jesus"],
         "curso": ["Matematica", "tutoria", " Ingles", "Calculo"," Razonamiento matematico"]}
nota_ = []
resp = "s"
while resp == "s":
    codigo = input("Ingresar el codigo del alumno: ")
    curso = input("Ingresa el nombre del curso: ")
    nota1 = int(input("Ingrese la  nota 1 : "))
    nota2 = int(input("Ingrese la nota 2: "))
    nota3 = int(input("Ingrese la nota 3: "))
    nota4 = int(input("Ingrese la nota 4: "))
    x = 0
    for i in Diccionario["codigo"]:
        if i == codigo:
            codigoTemp = i
            nombreTemp = Diccionario["nombre"][x]
            promedio = (nota1 + nota2 + nota3 + nota4)/4
            registro = ["Codigo: " + str(codigoTemp) + " | " + "Nombre :" + str(nombreTemp) + " | " + "Curso :" + curso + " | " + "Promedio: " + str(promedio) + " | " +"Nota 1: " + str(nota1) + "| " + "Nota 2: " + str(nota2) + " | " + "Nota 3: " + str(nota3) + " | " + "Nota 4: " + str(nota4)]
            f = open("examen_final.txt", "a")
            cadena = "".join(registro)
            f.write("\n" + cadena)
            f.close()
        x += 1
    resp = input("¿Desea seguir? : s/n ")
    f = open("examen_final.txt")
    print(f.read())
    f.close()