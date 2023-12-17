SELECT restaraunts.*, restaraunt_addresses.address FROM restaraunts
INNER JOIN restaraunt_addresses ON restaraunts.restaraunt_id = restaraunt_addresses.restaraunt_id;