from db_engine.engine import engine, DbEngine
from services.constants import OK_CODE, RESTARAUNT_CREATE_SCRIPT_PATH, \
    RESTARAUNT_READ_SCRIPT_PATH, RESTARAUNT_UPDATE_SCRIPT_PATH, RESTARAUNT_DELETE_SCRIPT_PATH


class RestarauntService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, name, phone_number, email, owner, stars,
               price, category, work_time):
        query = self.engine.get_query_result(sql_path=RESTARAUNT_CREATE_SCRIPT_PATH,
                                             fields=(name, phone_number, email, owner, stars,
                                                     price, category, work_time))

        if query:
            return OK_CODE

    def read(self, name):
        query = self.engine.get_query_result(sql_path=RESTARAUNT_READ_SCRIPT_PATH,
                                             fields=(name,))
        if query:
            return query

    def update(self, new_name, old_name, phone_number, email, owner, stars,
               price, category, work_time):
        query = self.engine.get_query_result(sql_path=RESTARAUNT_UPDATE_SCRIPT_PATH,
                                             fields=(new_name, phone_number, email, owner, stars,
                                                     price, category, work_time, old_name))
        if query:
            return OK_CODE

    def delete(self, name):
        query = self.engine.get_query_result(sql_path=RESTARAUNT_DELETE_SCRIPT_PATH,
                                             fields=(name,))
        if query:
            return OK_CODE
