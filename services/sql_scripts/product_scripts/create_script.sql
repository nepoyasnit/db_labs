INSERT INTO products(shop_id, name, price, promo,
                     producer, country, description, category,
                     weight, photo_url)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
returning TRUE;

