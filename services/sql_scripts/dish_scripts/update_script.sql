UPDATE dishes
SET restaraunt_id = %s, name = %s, price = %s, promo = %s,
    description = %s, category = %s, weight = %s, photo_url = %s
WHERE name = %s
returning name;