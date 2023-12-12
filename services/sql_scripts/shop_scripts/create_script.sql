INSERT INTO shops(name, phone_number, email, owner,
                  work_time, category)
VALUES(%s, %s, %s, %s, %s, %s)
returning TRUE;