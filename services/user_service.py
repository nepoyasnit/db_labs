from db_engine.engine import engine, DbEngine
from services.utils import check_errors
from services.constants import USER_LOGIN_SCRIPT_PATH, \
    USER_REGISTER_SCRIPT_PATH, USER_UPDATE_SCRIPT_PATH, USER_READ_SCRIPT_PATH, \
    USER_DELETE_SCRIPT_PATH
from constants import OK_CODE, ERROR_CODE, NOT_REGISTERED_ERROR


class UserService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def login(self, email, password):
        query = self.engine.get_query_result(USER_LOGIN_SCRIPT_PATH, (email, password))
        if query[0][0] is True:
            return OK_CODE
        return NOT_REGISTERED_ERROR

    def create(self, role, surname, name, patronymic, sex, phone_number,
               photo_url, email, password, birthday, address):
        query = self.engine.get_query_result(sql_path=USER_REGISTER_SCRIPT_PATH,
                                             fields=(role, surname, name, patronymic, sex, phone_number,
                                                     photo_url, email, password, birthday, address))

        return check_errors(query)

    def read(self, user_id):
        query = self.engine.get_query_result(sql_path=USER_READ_SCRIPT_PATH,
                                             fields=(user_id,))
        result_code = check_errors(query)
        if result_code == OK_CODE:
            return query
        return result_code

    def update(self, role_id, surname, name, patronymic, sex, phone_number,
               photo_url, email, password, birthday, address, user_id):
        query = self.engine.get_query_result(sql_path=USER_UPDATE_SCRIPT_PATH,
                                             fields=(role_id, surname, name, patronymic, sex, phone_number,
                                                     photo_url, email, password, birthday, address, user_id))

        return check_errors(query)

    def delete(self, user_id):
        query = self.engine.get_query_result(sql_path=USER_DELETE_SCRIPT_PATH,
                                             fields=(user_id,))
        return check_errors(query)
