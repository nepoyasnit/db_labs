import psycopg2
from db_engine.constants import DB_URI_PATH


class DbEngine:
    connection: psycopg2.extensions.connection

    def __init__(self):
        self.connection = psycopg2.connect(DB_URI_PATH)

    @staticmethod
    def _get_sql_script(sql_path: str):
        file = open(sql_path, 'r')
        sql_file = file.read()
        file.close()

        sql_commands = sql_file.split(';')

        return sql_commands

    def get_query_result(self, sql_path, fields):
        cursor = self.connection.cursor()
        sql_script = self._get_sql_script(sql_path)
        cursor.execute(sql_script[0], fields)

        query_result = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        return query_result


engine = DbEngine()
