DELETE FROM dishes
WHERE name = %s
returning TRUE;