class Conexion:
    
    def database(self, consulta):
        import mysql.connector
        db = {
            'host' : 'localhost',
            'user' : 'root',
            'password' : '',
            'database' : 'domino_db'
        }
        try:
            conexion = mysql.connector.connect(**db)
            cursor = conexion.cursor()
            resultado = ""
            
            if consulta == 1:
                consulta = "select * from fichas"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
            conexion.commit()
            return resultado
        except Error as e:
            print(e)