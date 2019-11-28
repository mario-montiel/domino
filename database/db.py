import mysql.connector
import database

class Conexion:
    
    id_j_1 = []
    id_j_2 = []
    id_j_3 = []
    id_j_4 = []
    db = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'domino_db'
        }
    
    def database(self, consulta):
        try:
            conexion = mysql.connector.connect(**self.db)
            cursor = conexion.cursor()
            resultado = ""

            if consulta == 1:
                consulta = "select * from fichas"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
            conexion.commit()
            return resultado
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            
    def ingresar_jugadores(self, n_jugadores):
        try:
            id = 1
            conexion = mysql.connector.connect(**self.db)
            cursor = conexion.cursor()
            actualizar = "UPDATE jugadores SET jugadores.jugador_nombre = %s WHERE jugadores.jugador_id = %s"
            for i in n_jugadores:
                cursor.execute(actualizar, (i[0], id))
                id += 1
                    
            conexion.commit()
                
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def asignar_fichas_db(self, consulta, jugador1, jugador2, jugador3, jugador4):
        try:
            conexion = mysql.connector.connect(**self.db)
            cursor = conexion.cursor()
            fichas_id = "SELECT fichas.ficha_id FROM fichas WHERE fichas.ficha_status = %s"
            cursor.execute(fichas_id, (0,))
            resultado = cursor.fetchall()
            indice = 0
            # for i in resultado:
            #     print(i)
            for i in jugador1:
                self.id_j_1.append(i[0])
            for i in jugador2:
                self.id_j_2.append(i[0])
            for i in jugador3:
                self.id_j_3.append(i[0])
            for i in jugador4:
                self.id_j_4.append(i[0])
                
            if consulta == 2:
                actualizar = "UPDATE fichas SET fichas.jugador_id = %s WHERE fichas.ficha_id = %s"
                for i in self.id_j_1:
                    cursor.execute(actualizar, (1, self.id_j_1[indice]))
                    indice += 1
                indice = 0
                for i in self.id_j_2:
                    cursor.execute(actualizar, (2, self.id_j_2[indice]))
                    indice += 1
                indice = 0
                for i in self.id_j_3:
                    cursor.execute(actualizar, (3, self.id_j_3[indice]))
                    indice += 1
                indice = 0
                for i in self.id_j_4:
                    cursor.execute(actualizar, (4, self.id_j_4[indice]))
                    indice += 1
                indice = 0
                conexion.commit()
                
                sql = "SELECT * FROM fichas WHERE fichas.palabra = %s"
                cursor.execute(sql, (28,))
                resultado = cursor.fetchall()
                
                if resultado != "":
                    from domino.juego import Juego
                    juego = Juego()
                    juego.mula = resultado
                
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    
    def obtener_mula(self):
        try:
            conexion = mysql.connector.connect(**self.db)
            cursor = conexion.cursor()
            sql = "SELECT * FROM fichas where fichas.ficha_id = 28"
            cursor.execute(sql)
            resultado = cursor.fetchone()
            
            return resultado
        
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            
    def poner_ficha(self, ficha_seleccionada):
        try:
            print("AAAAAAAAA" + str(ficha_seleccionada))
            # consulta = "select * from fichas"
            # cursor.execute(consulta)
            # resultado = cursor.fetchall()
            
            # update = "UPDATE fichas SET fichas.ficha_status = %s WHERE fichas.ficha_id = %s"
            # for i in resultado:
            #     if i[0] == 28:
            #         cursor.execute(update, (1, self.id_j_1[indice]))
            #         indice += 1
                
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
