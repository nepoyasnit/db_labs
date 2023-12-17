from services.user_service import UserService
from services.restaurant_service import RestaurantService
from controllers.constants import ACCESS_ERROR
from constants import OK_CODE, ERROR_CODE, NOT_REGISTERED_ERROR


class UserController:
    service: UserService
    is_registered: bool

    def __init__(self):
        self.is_registered = False
        self.user_service = UserService()
        self.restaurant_service = RestaurantService()

    def login(self, email: str, password: str):
        if self.user_service.login(email, password) == OK_CODE:
            self.is_registered = True

    def register(self, role, surname, name, patronymic, sex, phone_number,
                 photo_url, email, password, birthday, address):
        if self.user_service.create(role, surname, name, patronymic, sex, phone_number,
                                    photo_url, email, password, birthday, address) == OK_CODE:
            self.is_registered = True

    def logout(self):
        self.is_registered = False

    def get_restaurants(self):
        if not self.is_registered:
            return ACCESS_ERROR
        return self.restaurant_service.read_all()
