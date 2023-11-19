UPDATE users
SET role_id = %s, surname=%s, name=%s, patronymic=%s, sex=%s, phone_number=%s,
    photo_url=%s, email=%s, password=%s, birthday=%s, address=%s
WHERE email = %s
returning email;