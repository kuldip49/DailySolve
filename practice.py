import sqlite3

DB_FILE = 'students.db'

CREATE_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    marks INTEGER NOT NULL
);
'''

INSERT_STUD_SQL = 'INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?);'
UPDATE_MARKS_SQL = 'UPDATE students SET marks = ? WHERE id = ?;'
DELETE_SQL = 'DELETE FROM students WHERE id = ?;'
SELECT_ALL_SQL = 'SELECT id, name, age, marks FROM students ORDER BY id;'

students = [
    (1, 'Alice', 19, 85),
    (2, 'Bob', 20, 90),
    (3, 'Charlie', 18, 75)
]


def print_students(rows):
    print('id\tname\tage\tmarks')
    for row in rows:
        print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')


def main():
    conn = sqlite3.connect(DB_FILE)
    try:
        cur = conn.cursor()

        # CREATE
        cur.execute(CREATE_TABLE_SQL)
        conn.commit()

        # Insert at least 3 student records (if not already inserted)
        # For id uniqueness, we use INSERT OR IGNORE
        for st in students:
            cur.execute('INSERT OR IGNORE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?);', st)
        conn.commit()

        # READ: display all student records
        print('\nInitial student records:')
        cur.execute(SELECT_ALL_SQL)
        rows = cur.fetchall()
        print_students(rows)

        # UPDATE marks for id = 2
        updated_marks = 95
        cur.execute(UPDATE_MARKS_SQL, (updated_marks, 2))
        conn.commit()

        print(f'\nAfter updating marks for student id=2 to {updated_marks}:')
        cur.execute(SELECT_ALL_SQL)
        rows = cur.fetchall()
        print_students(rows)

        # DELETE student with id = 3
        cur.execute(DELETE_SQL, (3,))
        conn.commit()

        print('\nAfter deleting student id=3:')
        cur.execute(SELECT_ALL_SQL)
        rows = cur.fetchall()
        print_students(rows)

    finally:
        conn.close()


if __name__ == '__main__':
    main()
