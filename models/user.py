class User:
    
    def __init__(self):
        self._id = -1
        self.email = ""
        self.username = ""
        self._hashed_password = ""

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password):
        self._hashed_password = password

    def save(self, cursor):
        if self.id == -1:
            query = """
            INSERT INTO users (username, email, hashed_password)
            VALUES (%s, %s, %s) RETURNING id"""
            value = (self.username, self.email, self.hashed_password,)
            cursor.execute(query, value)
            self._id = cursor.fetchone()[0]
            return True
        else:
            query = """
            UPDATE users SET username=%s, email=%s, 
            hashed_password=%s WHERE id = %s"""
            value = (self.username, self.email, self.hashed_password, self.id)
            cursor.execute(query, value)
            return True
        return False

    @staticmethod
    def load_by_id(cursor, id):
        query = """
        SELECT id, username, email, hashed_password 
        FROM users WHERE id=%s"""
        cursor.execute(query, (id,))
        data = cursor.fetchone()
        if data:
            user = User()
            user._id = data[0]
            user.username = data[1]
            user.email = data[2]
            user._hashed_password = data[3]
            return user
        else:
            return None 

    @staticmethod
    def load_all(cursor):
        query = """
        SELECT id, username, email, 
        hashed_password FROM users"""
        cursor.execute(query)
        users = []
        for row in cursor.fetchall():
            user = User()
            user._id = row[0]
            user.username = row[1]
            user.email = row[2]
            user._hashed_password = row[3]
            users.append(user)
        return users


    def delete(self, cursor):
        if self.id == -1: return False
        query = "DELETE FROM users WHERE id=%s"
        cursor.execute(query, (self.id,))
        return True









