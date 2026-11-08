import psycopg2


# Se connecter à la base de données
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="tp",
        user="postgres",
        password="postgres"
    )


# Ajouter un étudiant
def add_student(conn, name, grade):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s) RETURNING id",
            (name, grade)
        )
        student_id = cur.fetchone()[0]

    conn.commit()
    return student_id


# Rechercher un étudiant par son identifiant
def get_student(conn, student_id):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM students WHERE id = %s",
            (student_id,)
        )
        return cur.fetchone()


# Calculer la moyenne des notes
def average_grade(conn):
    raise NotImplementedError
