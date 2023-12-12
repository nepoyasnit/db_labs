INSERT INTO orders(is_active, order_time, user_id, courier_id)
VALUES(%s, %s, %s, %s)
returning TRUE;