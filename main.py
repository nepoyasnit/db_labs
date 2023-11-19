from services.shop_service import ShopService

# print(ShopService().create('test', '+375294432003',
#                            'test@sosedi.by', 'test',
#                            '09:00-12:00', 'test'))

# print (ShopService().read('test'))

print(ShopService().update('test', 'test1', '+375294432003',
                            'test@sosedi.by', 'test',
                            '09:00-12:00', 'test'))
