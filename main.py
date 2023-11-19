from services.user_service import UserService

# print(UserService().login('mihail_dubinka@gmail.com', 'dubinka_2021'))

# print(UserService().create(
#     'user', 'test1', 'test1', 'test1', 'M', '+375292639005',
#      'test1.jpg', 'test1@gmail.com', 'test', '1990-06-28',
#      'г. Минск, ул. test, д.8, кв. 5'))

# print(UserService().update(
#     2, 'test', 'test', 'test', 'M', '+375292639005',
#     'test.jpg', 'test@gmail.com', 'test1@gmail.com', 'test', '1990-06-28',
#     'г. Минск, ул. test, д.8, кв. 5'))

# print(UserService().read('mihail_dubinka@gmail.com'))

print(UserService().delete('test@gmail.com'))
