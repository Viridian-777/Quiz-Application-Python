import sqlite3

DB_FILE = "quizapp.db"

def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER NOT NULL,
            question TEXT NOT NULL,
            options TEXT NOT NULL,
            answer TEXT NOT NULL,
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            quiz_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
        )
    ''')

    conn.commit()
    conn.close()

def populate():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    quizzes = [("Python Quiz",), ("DBMS Quiz",), ("DSA Quiz",)]
    cursor.executemany("INSERT INTO quizzes (name) VALUES (?)", quizzes)

    questions = [(1, "What is the output of the following code: `print(type([]))`?", "<class 'list'>,<class 'tuple'>,<class 'set'>,<class 'dict'>", "<class 'list'>"),
    (1, "Which of the following is used to define a block of code in Python?", "Braces,Parentheses,Indentation,Semicolons", "Indentation"),
    (1, "What is the correct way to open a file for writing in Python?", "open('file.txt', 'r'),open('file.txt', 'w'),open('file.txt', 'x'),open('file.txt', 'a')", "open('file.txt', 'w')"),
    (1, "Which of the following methods is used to add an element to a list?", "append(),add(),insert(),extend()", "append()"),
    (1, "What is the output of `bool(0)` in Python?", "True,False,None,Error", "False"),
    
    (2, "Which of the following is a valid SQL data type?", "STRING,CHAR,FLOAT,Both CHAR and FLOAT", "Both CHAR and FLOAT"),
    (2, "What is the primary key?", "A unique identifier for a record,A foreign key,A default key,An optional key", "A unique identifier for a record"),
    (2, "What does ACID stand for in DBMS?", "Atomicity, Consistency, Isolation, Durability,Access, Control, Integration, Data,Accuracy, Consistency, Integrity, Durability,Atomicity, Clarity, Integration, Durability", "Atomicity, Consistency, Isolation, Durability"),
    (2, "Which of the following is a NoSQL database?", "MongoDB,MySQL,Oracle,PostgreSQL", "MongoDB"),
    (2, "What does the JOIN clause do in SQL?", "Combines rows from two or more tables,Deletes rows from a table,Adds new rows to a table,Modifies rows in a table", "Combines rows from two or more tables"),
    
    (3, "Which data structure uses LIFO (Last In, First Out)?", "Stack,Queue,Array,Tree", "Stack"),
    (3, "What is the maximum number of nodes in a binary tree of height `h`?", "2^h,2^(h+1)-1,2^h-1,2^(h-1)", "2^(h+1)-1"),
    (3, "Which of the following algorithms is used for finding the shortest path in a graph?", "Dijkstra's Algorithm,Prim's Algorithm,Kruskal's Algorithm,DFS", "Dijkstra's Algorithm"),
    (3, "What is the time complexity of inserting an element into a heap?", "O(1),O(log n),O(n),O(n log n)", "O(log n)"),
    (3, "Which of the following data structures can be used to implement a priority queue?", "Heap,Queue,Stack,Linked List", "Heap")
    ]
    cursor.executemany("INSERT INTO questions (quiz_id, question, options, correct_answer) VALUES (?, ?, ?, ?)", questions)


    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    populate()
    print("Database setup complete with seed data!")
