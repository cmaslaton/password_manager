import sqlite3


class Model:
    def __init__(self):
        self._crea_db()

    def _crea_db(self):
        """Si no existe, crea la db"""
        conn = sqlite3.connect('paswerdb.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""CREATE TABLE paswerdb (
                        website text,
                        username text,
                        password text                
                                    )""")
            print('DB Creada')
        except sqlite3.Error:
            print('La DB ya está creada')
        finally:
            conn.commit()
            conn.close()

    def delete_data(self, row):
        conn = sqlite3.connect('paswerdb.db')
        cursor = conn.cursor()
        try:
            cursor.execute(
                f"DELETE FROM paswerdb WHERE website = '{row[0]}' AND username = '{row[1]}' AND password = '{row[2]}'")
        except sqlite3.Error:
            print('Error borrando los datos ')
        finally:
            conn.commit()
            conn.close()

    def get_data(self):
        conn = sqlite3.connect('paswerdb.db')
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM paswerdb")
            paswers = cursor.fetchall()
            return paswers
        except sqlite3.Error:
            print('Error obteniendo los datos ')
        finally:
            conn.commit()
            conn.close()

    def save_data(self, data_dict):
        """guarda la información del formulario"""
        conn = sqlite3.connect('paswerdb.db')
        cursor = conn.cursor()
        try:
            cursor.execute(f"""INSERT INTO paswerdb VALUES (
                                            '{data_dict['website']}',
                                            '{data_dict['username']}',
                                            '{data_dict['password']}'
                                            )
                                        """)
            print('Datos Guardados!')
        except sqlite3.Error:
            print('Error en la carga de datos')
        finally:
            conn.commit()
            conn.close()

    def search_data(self, website):
        conn = sqlite3.connect('paswerdb.db')
        cursor = conn.cursor()
        try:
            cursor = cursor.execute(f"""SELECT * FROM paswerdb WHERE website LIKE '%{website}%'""")
            paswers = cursor.fetchall()
            return paswers
        except:
            pass
        finally:
            conn.commit()
            conn.close()

    def update_data(self, old_data, new_data):
        """modifica la información de la base de datos"""
        conn = sqlite3.connect('paswerdb.db')
        cursor = conn.cursor()
        try:
            cursor.execute(
                f"""UPDATE paswerdb SET website='{new_data[0]}', username='{new_data[1]}', password='{new_data[2]}' 
                    WHERE website='{old_data[0]}' AND username='{old_data[1]}' AND password='{old_data[2]}'""")
        except:
            print('Error con el update de datos')
        finally:
            conn.commit()
            conn.close()
