INSERT INTO restaraunts(name, phone_number, email, owner,
stars, price, category, work_time)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
returning TRUE;