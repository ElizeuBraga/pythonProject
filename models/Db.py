import sqlite3

class Db():
    def select(self, sql, params):
        conection = sqlite3.connect('database/database.db')
        cursor = conection.cursor()
        cursor.execute(sql, (params))
        data = cursor.fetchall()
        conection.close()
        return data

    def selectOne(self, sql, params):
        conection = sqlite3.connect('database/database.db')
        cursor = conection.cursor()
        cursor.execute(sql, (params))
        data = cursor.fetchone()
        conection.close()
        return data

    def insert(self, sql, params):
        conection = sqlite3.connect('database/database.db')
        cursor = conection.cursor()
        cursor.execute(sql, (params))
        conection.commit()
        conection.close()
        return True