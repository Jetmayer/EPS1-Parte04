from os import system
import time
import conexion as conn
db = conn.DB()
system("clear")
def create():
    name = str(input("INGRESA SU NOMBRE: "))
    precio = str(input("INGRESA SU precio: "))
    codigo = str(input("INGRESA SU codigo: "))
    if(len(name) > 0 and len(precio) > 0):
        sql = "INSERT INTO sistema(name,precio,codigo) VALUES(?,?,?)"
        parametros = (name,precio,codigo)
        db.ejecutar_consulta(sql,parametros)
        print("Insertados")
def read():
    sql = "SELECT * FROM sistema"
    result = db.ejecutar_consulta(sql)
    for data in result:
        print(""" 
        ID :        {}
        NOMBRE :    {}
        precio :     {}
        """.format(data[0],data[1],data[2]))
def update():
    id = int(input("INGRESA EL ID: "))
    if(id != 0):
        name = str(input("INGRESA SU NOMBRE: "))
        precio = str(input("INGRESA SU precio: "))
        if(len(name) > 0 and len(precio) > 0):
            sql = "UPDATE sistema SET name=?,precio=? WHERE id=?"
            parametros = (name,precio,id)
            db.ejecutar_consulta(sql,parametros)
            print("Actualizado!")
    else:
        print("Se require un ID")
def delete():
    id = int(input("INGRESA EL ID: "))
    if(id != 0):
        sql = "DELETE FROM sistema WHERE id=?"
        parametros = (id,)
        db.ejecutar_consulta(sql,parametros)
        print("Eliminado!")
    else:
        print("Se require un ID")
def search():
    nombre = str(input("Buscar por nombre: "))
    if(len(nombre) > 0):
        sql = "SELECT * FROM sistema WHERE name LIKE ?"
        parametros = ('%{}%'.format(nombre),)
        result = db.ejecutar_consulta(sql,parametros)
        for data in result:
            print(""" 
            +ID :        {}
            +NOMBRE :    {}
            +precio :     {}""".format(data[0],data[1],data[2]))
while True:
    print("=========================================")
    print("\tCRUD CON SQLite3")
    print("=========================================")
    print("\t[1] Insertar ")
    print("\t[2] Listar ")
    print("\t[3] Actualizar ")
    print("\t[4] Eliminar ")
    print("\t[5] Buscar ")
    print("\t[6] Salir")
    print("=========================================")

    try:
        opcion = int(input("Selecciona una opcion: "))
        if(opcion == 1):
            create()
            time.sleep(1)
            system("clear")
        elif (opcion == 2):
            read()
            time.sleep(1)
        elif (opcion == 3):
            update()
            time.sleep(1)
            system("clear")
        elif (opcion == 4):
            delete()
            time.sleep(1)
            system("clear")
        elif (opcion == 5):
            search()

        elif (opcion == 6):
            break
    except:
        print("Por favor, selecciona las opciones correctas")
        system("clear")
