INSERT INTO users(role_id, surname, name, patronymic, sex, phone_number, photo_url, email, password, birthday, address)
VALUES((SELECT role_id FROM roles WHERE role_name = %s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
returning name;