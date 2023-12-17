from db_engine.engine import engine, DbEngine
from services.constants import ORDER_CREATE_SCRIPT_PATH, ORDER_READ_SCRIPT_PATH, ORDER_UPDATE_SCRIPT_PATH, \
                            ORDER_DELETE_SCRIPT_PATH
from constants import OK_CODE
from services.utils import check_errors


class OrderService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, is_active, order_time, user_id, courier_id):
        query = self.engine.get_query_result(sql_path=ORDER_CREATE_SCRIPT_PATH, fields=(is_active, order_time,
                                                                                        user_id, courier_id))
        return check_errors(query)

    def read(self, order_id):
        query = self.engine.get_query_result(sql_path=ORDER_READ_SCRIPT_PATH, fields=(order_id,))

        result = check_errors(query)
        if result == OK_CODE:
            return query
        return result

    def update(self, is_active, order_time, user_id, courier_id, order_id):
        query = self.engine.get_query_result(sql_path=ORDER_UPDATE_SCRIPT_PATH, fields=(is_active, order_time,
                                                                                        user_id, courier_id, order_id))
        return check_errors(query)

    def delete(self, order_id):
        query = self.engine.get_query_result(sql_path=ORDER_DELETE_SCRIPT_PATH, fields=(order_id,))

        return check_errors(query)
