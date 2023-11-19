from services.product_service import ProductService

# print(ProductService().create('Соседи','test',
#                               10, 0,'test',
#                               'test', 'test',
#                               'test', 0.43,
#                               'sosedi/test.jpg'))

# print(ProductService().read('test'))

# print(ProductService().update('Соседи','test',
#                               'test1',10, 0,
#                               'test',
#                                'test', 'test',
#                                'test', 0.43,
#                                'sosedi/test.jpg'))

print(ProductService().delete('test_product'))
