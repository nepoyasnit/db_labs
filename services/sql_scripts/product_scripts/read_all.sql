SELECT products.*, shops.name AS shop_name FROM products
INNER JOIN shops ON products.shop_id = shops.shop_id
WHERE shops.name = %s;