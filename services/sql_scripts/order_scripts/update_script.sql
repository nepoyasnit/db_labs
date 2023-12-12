UPDATE orders
SET is_active = %s, order_time = %s, user_id = %s, courier_id = %s
WHERE order_id = %s
returning TRUE;