DELETE FROM dishes
WHERE dish_id = %s
returning TRUE;