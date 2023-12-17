SELECT dishes.*, restaraunts.name FROM dishes
INNER JOIN restaraunts ON dishes.restaraunt_id = restaraunts.restaraunt_id
WHERE restaraunts.name = %s;