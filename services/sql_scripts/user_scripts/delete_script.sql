DELETE FROM users
WHERE user_id = %s
returning TRUE;