import sqlite3
base_datos = 'calculador_nutricional.db'
IMC_inf = 18.5
IMC_sup = 24.9
i = True



class paciente():
    def __init__(self, apellido, nombre, edad, peso, talla):
        
        self.apellido = apellido
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.talla = talla
        self.diagnostico = None
    def estado_nutricional(self):
        IMC = self.peso / (self.talla ** 2)   
        if IMC < IMC_inf:
            self.diagnostico = 'Bajo Peso'
            print(f'El IMC del paciente {self.apellido} {self.nombre} es de {IMC}, por lo que se encuentra en {self.diagnostico}\n')
            
        elif IMC > IMC_inf and IMC <= IMC_sup:
            self.diagnostico = 'Normal'
            print(f"El IMC del paciente {self.apellido} es de {IMC}, por lo que se encuentra dentro de los paramentros normales")
            
        elif IMC > IMC_sup:
            self.diagnostico = 'Sobrepeso'
            print(f"El IMC del paciente {self.apellido} {self.nombre} es de {IMC}, por lo que se encuentra con {self.diagnostico}")
            
        else:
            pass
    def dato_comprimido(self):
        pacie = (1, self.apellido, self.nombre, self.edad, self.peso, self.talla)
        return pacie
def conectar_bd():
    conexion = sqlite3.connect(base_datos)
    cursor = conexion.cursor()
    conexion.commit()
    conexion.close()
    print(f'Conexion con base de datos {base_datos} exitosa\n')
def crear_tabla():
    conexion = sqlite3.connect(base_datos)
    cursor = conexion.cursor()
    cursor.execute("""
           CREATE TABLE IF NOT EXISTS pacientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                   apellido TEXT NOT NULL,
                   nombre TEXT NOT NULL,
                   edad INTEGER NOT NULL,
                 peso REAL NOT NULL,
                 talla REAL NOT NULL,
                   diagnostico TEXT )
                   
""")
    print(f'Tabla creada con exito\n')
    conexion.commit()
    conexion.close()

def cargar_datos(persona):
        conexion = sqlite3.connect(base_datos)
        cursor = conexion.cursor()
       
        instruccion = f"INSERT INTO pacientes(apellido, nombre, edad, peso, talla, diagnostico) VALUES('{persona.apellido}', '{persona.nombre}', '{persona.edad}', '{persona.peso}', '{persona.talla}', '{persona.diagnostico}')"
        cursor.execute(instruccion)
        print(f'Paciente {persona.nombre} {persona.apellido} cargado con exito\n')
        conexion.commit()
        conexion.close()
def cargar_varios(persona):
    conexion = sqlite3.connect(base_datos)
    cursor = conexion.cursor()
    instruccion  = f"INSERT INTO pacientes(apellido, nombre, edad, peso, talla, diagnostico) VALUES(?, ?, ?, ?, ?, ?)"
    cursor.executemany(instruccion, persona)
    print('pacientes cargados con exito\n')
    conexion.commit()
    conexion.close()
def imprimir_resultados():
    conexion = sqlite3.connect(base_datos)
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM pacientes"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)
    conexion.commit()
    conexion.close()
def imprimir_orden(columna):
    conexion = sqlite3.connect(base_datos)
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM pacientes ORDER BY {columna}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)
    conexion.commit()
    conexion.close()
def buscar(instruccion):
    conexion = sqlite3.connect(base_datos)
    cursor = conexion.cursor()
    #instruccion = f"SELECT * FROM pacientes WHERE '{field}' like '{new}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)
    conexion.commit()
    conexion.close()
def actualizar(field, new, new2):
    conexion = sqlite3.connect(base_datos)
    cursor = conexion.cursor()
    instruccion = f"UPDATE pacientes SET '{field}'='{new}' WHERE id = '{new2}'"
    cursor.execute(instruccion)
    print(f'Datos actualizados con exito\n')
    conexion.commit()
    conexion.close()
def borrar(new):
    conexion = sqlite3.connect(base_datos)
    cursor = conexion.cursor()
    instruccion = f"DELETE FROM pacientes WHERE id = '{new}'"
    cursor.execute(instruccion)
    print(f'Paciente eliminado con exito de la base de datos\n')
    conexion.commit()
    conexion.close()

def menu_principal():
        print(f"""
    ---------------------------------------------
    Seleccione como desea operar  """)
        print(f"""
    ---------------------------------------------
    | 1) Calcular estado/diagnostico nutricional|
    | 2) Guardar resultados en base de datos    |
    | 3) Actualizar un registro                 |
    | 4) Borrar un registro                     |
    | 5) Buscar                                 |
    | 6) Salir                                  |
          
""")

class CMR():
    def __init__(self, archivo_db):
        #super().__init__(apellido, nombre, edad, peso, talla)
        self.archivo_db = archivo_db
        self.conn = None
        self.cursor = None
    def informacion(self):
        
        last_name = input(f'Ingrese el apellido del paciente\n')
        name = input(f'ingrese el nombre del paciente\n')
        years_old = int(input(f'Ingrese la edad del paciente\n'))
        kg = float(input(f'Ingrese el peso del paciente\n'))
        altura = float(input(f'Ingrese la talla del paciente (expresada en metros)\n'))
        paciente.nombre = name
        paciente.apellido = last_name
        paciente.edad = years_old
        paciente.peso = kg
        paciente.talla = altura
        
    def opcion(self):
        elegido = int(input(''))
        
        if elegido == 1:
            p4.informacion()
            paciente.estado_nutricional(paciente)
        elif elegido == 2:
            cargar_datos(paciente)
        elif elegido == 3:
            campo = (input(f'Ingrese el campo que desea actualizar\n')).lower()
            campo2 = int(input(f'Ingrese el ID del paciente\n'))
            if campo == 'apellido':
                valor = input(f'Ingrese el nuevo valor para el campo {campo} selecionado\n')
                actualizar(campo, valor, campo2)
            elif campo == 'nombre':
                valor = input(f'Ingrese el nuevo valor para el campo {campo} selecionado\n')
                actualizar(campo, valor, campo2)
            elif campo == 'edad':
                valor = input(f'Ingrese el nuevo valor para el campo {campo} selecionado\n')
                actualizar(campo, valor, campo2)
            elif campo == 'peso':
                valor = input(f'Ingrese el nuevo valor para el campo {campo} selecionado\n')
                actualizar(campo, valor, campo2)
            elif campo == 'talla':
                valor = input(f'Ingrese el nuevo valor para el campo {campo} selecionado\n')
                actualizar(campo, valor, campo2)
            else:
                pass
   
        elif elegido == 4:
            campo2 = int(input(f'Ingrese el ID del paciente que desea eliminar\n'))
            borrar(campo2)
        elif elegido == 5: 
            campo = (input(f'Elija la columna para buscar(id, apellido, nombre)\n')).lower()
            if campo == 'id':
                valor = input(f'Ingrese el ID\n')
                valor2 = f"SELECT * FROM pacientes WHERE id = '{valor}'"
                buscar(valor2)
            elif campo == 'apellido':
                valor = input(f'Ingrese el apellido\n')
                valor2 = f"SELECT * FROM pacientes WHERE apellido like '{valor}'"
                buscar(valor2)
            elif campo == 'nombre':
                valor = input(f'Ingrese el nombre\n')
                valor2 = f"SELECT * FROM pacientes WHERE nombre like '{valor}'"
                buscar(valor2)
        elif elegido == 6:
            print('Hasta Luego!\n')
            i = False
        else:
            pass
    
    #def seguir(self):
        

  

p4 = CMR(base_datos)
crear_tabla()
print(f"""    -----------------------------------
      BIENVENIDO AL CONTROL NUTRICIONAL
    -----------------------------------\n""")

menu_principal()
p4.opcion()



while i == True:
    sesigue = int(input(f"""
Quiere realizar otra operacion? 
1)SI 2)NO\n"""))   
    if sesigue == 1:
        menu_principal()
        p4.opcion()
    elif sesigue == 2:
        print(f'Hasta Luego!\n')
        i = False


