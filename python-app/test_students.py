import pytest
from students import get_connection, add_student, get_student, average_grade


# Préparer une connexion avant chaque test
@pytest.fixture
def conn():
    connection = get_connection()

    with connection.cursor() as cur:
        cur.execute("DELETE FROM students")

    connection.commit()

    yield connection

    connection.close()


# Test 1 : ajouter et lire un étudiant
def test_ajouter_et_lire(conn):
    student_id = add_student(conn, "Amel", 15)

    student = get_student(conn, student_id)

    assert student is not None
    assert student[1] == "Amel"
    assert float(student[2]) == 15.0


# Test 2 : rechercher un étudiant inexistant
def test_etudiant_inconnu(conn):
    assert get_student(conn, 9999) is None


# Test 3 : calculer la moyenne
def test_moyenne(conn):
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)

    assert average_grade(conn) == 12.0
