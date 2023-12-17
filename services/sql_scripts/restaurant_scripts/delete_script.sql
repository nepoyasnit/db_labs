DELETE FROM restaraunts
WHERE restaraunt_id = %s
returning TRUE;