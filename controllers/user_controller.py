from services.user_service import UserService


class UserController:
    service: UserService

    def __init__(self):
        self.service = UserService()

    def login(self, email: str, password: str):
        return self.service.login(email, password)


