UPDATE products
SET shop_id = %s, name = %s, price = %s, promo = %s, producer = %s,
country = %s, description = %s, category = %s, weight = %s, photo_url = %s
WHERE product_id = %s
returning name;