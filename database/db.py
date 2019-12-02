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
                cursor.execute(actualizar, (i, id))
                id += 1
                    
            conexion.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def asignar_fichas_db(self, consulta, jugador1, jugador2, jugador3, jugador4, fichas):
        try:
            conexion = mysql.connector.connect(**self.db)
            cursor = conexion.cursor()
            indice = 0
            for i in jugador1:
                self.id_j_1.append(i)
            for i in jugador2:
                self.id_j_2.append(i)
            for i in jugador3:
                self.id_j_3.append(i)
            for i in jugador4:
                self.id_j_4.append(i)
                
            if consulta == 2:
                actualizar = "UPDATE fichas SET fichas.jugador_id = %s WHERE fichas.ficha_id = %s"
                
                for i in self.id_j_1:
                    for j in i:
                        # print(j)
                        self.id_j_1 = []
                        self.id_j_1 = j
                        cursor.execute(actualizar, (1, self.id_j_1))
                for i in self.id_j_2:
                    for j in i:
                        self.id_j_2 = []
                        self.id_j_2 = j
                        cursor.execute(actualizar, (2, self.id_j_2))
                for i in self.id_j_3:
                    for j in i:
                        self.id_j_3 = []
                        self.id_j_3 = j
                        cursor.execute(actualizar, (3, self.id_j_3))
                for i in self.id_j_4:
                    for j in i:
                        self.id_j_4 = []
                        self.id_j_4 = j
                        cursor.execute(actualizar, (4, self.id_j_4))
                conexion.commit()
                
                sql = "SELECT * FROM fichas WHERE fichas.ficha_id = %s"
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
            
    # def poner_ficha(self, ficha_seleccionada):
    #     try:
    #         print("AAAAAAAAA" + str(ficha_seleccionada))
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
            
            
            
# PYGAME MAN

    def obtener_ficha_id(self, consulta):
        try:
            conexion = mysql.connector.connect(**self.db)
            cursor = conexion.cursor()
            

            if consulta == 3:
                consulta = "select fichas.ficha_id from fichas"
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                conexion.commit()
                return resultado
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
