DELETE FROM restaraunts
WHERE name = %s
returning TRUE;