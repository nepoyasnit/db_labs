from db_engine.engine import engine, DbEngine
from services.constants import REST_ADDRESS_CREATE_PATH, REST_ADDRESS_READ_PATH, REST_ADDRESS_UPDATE_PATH, \
                            REST_ADDRESS_DELETE_PATH
from constants import OK_CODE
from services.utils import check_errors


class RestAddressesService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, address, restaurant_id):
        query = self.engine.get_query_result(sql_path=REST_ADDRESS_CREATE_PATH, fields=(address, restaurant_id))
        return check_errors(query)

    def read(self, address_id):
        query = self.engine.get_query_result(sql_path=REST_ADDRESS_READ_PATH, fields=(address_id,))
        result_code = check_errors(query)

        if result_code == OK_CODE:
            return query
        return result_code

    def update(self, address, restaurant_id, address_id):
        query = self.engine.get_query_result(sql_path=REST_ADDRESS_UPDATE_PATH, fields=(address, restaurant_id,
                                                                                        address_id))
        return check_errors(query)

    def delete(self, address_id):
        query = self.engine.get_query_result(sql_path=REST_ADDRESS_DELETE_PATH, fields=(address_id,))
        return check_errors(query)
