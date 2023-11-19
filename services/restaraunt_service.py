from db_engine.engine import engine, DbEngine
from services.constants import OK_CODE, RESTARAUNT_CREATE_SCRIPT_PATH


class RestarauntService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, name, phone_number, email, owner, stars,
               price, category, work_time):
        query = engine.get_query_result(sql_path=RESTARAUNT_CREATE_SCRIPT_PATH,
                                        fields=(name, phone_number, email, owner, stars,
                                                price, category, work_time))

        if query:
            return OK_CODE
