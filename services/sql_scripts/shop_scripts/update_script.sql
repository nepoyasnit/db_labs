UPDATE shops
SET name = %s, phone_number=  %s, email = %s, owner = %s,
    work_time = %s, category = %s
WHERE name = %s
returning name;