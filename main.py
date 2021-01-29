from models.user import User
from psycopg2 import connect


DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "secret",
    "database": "workshop_2",
}

cnx = connect(**DB_CONFIG)
cnx.autocommit = True
cursor = cnx.cursor()

# Create user
# user = User()
# user.username = "kevin"
# user.email = "kevin@gmail.com"
# user.set_password("secret")
# user.save(cursor)

# Load by id
# user = User.load_by_id(cursor, 2)

# Load all users
# users = User.load_all(cursor)
# for user in users:
#     print(user.email)

# Modify by user
# user = User.load_by_id(cursor, 2)
# user.email = "adi@mail.com"
# user.set_password("secret")
# user.save(cursor)

# Delete by user
# user = User.load_by_id(cursor, 4)
# user.delete(cursor)

# Checked Credential
user = User.load_by_id(cursor, 5)
is_matched = user.check_password("secret")

