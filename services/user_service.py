from db_engine.engine import engine, DbEngine
from services.constants import USER_LOGIN_SCRIPT_PATH, OK_CODE, ERROR_CODE, NOT_REGISTERED_ERROR, \
    USER_REGISTER_SCRIPT_PATH, USER_UPDATE_SCRIPT_PATH, USER_GET_DATA_SCRIPT_PATH, \
    USER_DELETE_SCRIPT_PATH


class UserService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def login(self, email, password):
        query = self.engine.get_query_result(USER_LOGIN_SCRIPT_PATH, (email, password))
        if query[0][0] is True:
            return OK_CODE
        else:
            return NOT_REGISTERED_ERROR

    def create(self, role, surname, name, patronymic, sex, phone_number,
                 photo_url, email, password, birthday, address):
        query = self.engine.get_query_result(sql_path=USER_REGISTER_SCRIPT_PATH,
                                             fields=(role, surname, name, patronymic, sex, phone_number,
                                                     photo_url, email, password, birthday, address))
        if query:
            return OK_CODE
        else:
            return ERROR_CODE

    def update(self, role_id, surname, name, patronymic, sex, phone_number,
               photo_url, new_email, old_email, password, birthday, address):
        query = self.engine.get_query_result(sql_path=USER_UPDATE_SCRIPT_PATH,
                                             fields=(role_id, surname, name, patronymic, sex, phone_number,
                                                     photo_url, new_email, password, birthday, address, old_email))

        if query:
            return OK_CODE
        else:
            return ERROR_CODE

    def delete(self, email):
        query = self.engine.get_query_result(sql_path=USER_DELETE_SCRIPT_PATH,
                                             fields=(email,))

        if query:
            return OK_CODE
        else:
            return ERROR_CODE

    def read(self, email):
        query = self.engine.get_query_result(sql_path=USER_GET_DATA_SCRIPT_PATH,
                                             fields=(email,))
        if query:
            return query
        else:
            return ERROR_CODE
