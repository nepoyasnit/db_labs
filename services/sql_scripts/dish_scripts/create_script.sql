INSERT INTO dishes(restaraunt_id, name, price, promo, description, category, weight, photo_url)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s)
returning name;