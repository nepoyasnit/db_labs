DELETE FROM shops
WHERE name = %s
returning TRUE;