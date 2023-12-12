DELETE FROM orders
WHERE order_id = %s
returning TRUE;