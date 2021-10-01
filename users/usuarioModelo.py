import database.config as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class User:
    def __init__(self,nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def buscar(llega):
        sql = f'SELECT * FROM usuarios WHERE email="{llega}"'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    def guardar(self):
        sql="INSERT INTO usuarios VALUE (null,%s,%s,%s,%s,now())" 
        usuario = (self.nombre,self.apellidos,self.email,self.password)
        cursor.execute(sql,usuario)
        database.commit()
        return f'{self.nombre} ahora estas registrado'