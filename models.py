from database import get_connection
# from database import initialize_db

class User:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (self.name, self.email))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (self.name, self.email, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        conn.close()
        return [User(id=row[0], name=row[1], email=row[2]) for row in rows]


class Drama:
    def __init__(self, title, description, watch_date, user_id, completed=0, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.watch_date = watch_date
        self.user_id = user_id
        self.completed = completed

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO dramas (title, description, watch_date, completed, user_id) VALUES (?, ?, ?, ?, ?)",
                (self.title, self.description, self.watch_date, self.completed, self.user_id),
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE dramas SET title=?, description=?, watch_date=?, completed=? WHERE id=?",
                (self.title, self.description, self.watch_date, self.completed, self.id),
            )
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, description, watch_date, completed, user_id FROM dramas")
        rows = cursor.fetchall()
        conn.close()
        return [
            Drama(id=row[0], title=row[1], description=row[2], watch_date=row[3], completed=row[4], user_id=row[5])
            for row in rows
        ]

    @staticmethod
    def mark_completed(drama_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE dramas SET completed=1 WHERE id=?", (drama_id,))
        conn.commit()
        conn.close()

# initialize_db()
# d1 = Drama("Drama A", "Description A", "2023-10-01", 1)
# d2 = Drama("Drama B", "Description B", "2023-10-05", 1)
# d1.save()
# d2.save()
# d1.mark_completed(1)