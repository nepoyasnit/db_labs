UPDATE restaraunts
SET name = %s, phone_number = %s, email = %s, owner = %s,
    stars = %s, price = %s, category = %s, work_time = %s
WHERE restaraunt_id = %s
returning TRUE;