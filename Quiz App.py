user_data = {}

quiz_database = {
    "DSA": {
        "questions": {
            1: {
                "question": "What is the time complexity of binary search?",
                "options": ["A) O(n)", "B) O(log n)", "C) O(n log n)", "D) O(1)"],
                "answer": "B"
            },
            2: {
                "question": "Which data structure uses LIFO principle?",
                "options": ["A) Queue", "B) Stack", "C) Linked List", "D) Binary Tree"],
                "answer": "B"
            },
            3: {
                "question": "Which of the following is not a stable sorting algorithm?",
                "options": ["A) Merge Sort", "B) Quick Sort", "C) Bubble Sort", "D) Insertion Sort"],
                "answer": "B"
            },
            4: {
                "question": "What is the maximum number of edges in a simple graph with n vertices?",
                "options": ["A) n", "B) n(n-1)/2", "C) n^2", "D) n(n+1)/2"],
                "answer": "B"
            },
            5: {
                "question": "Which data structure is used in Breadth First Search (BFS)?",
                "options": ["A) Stack", "B) Queue", "C) Priority Queue", "D) Array"],
                "answer": "B"
            }
        }
    },
    "DBMS": {
        "questions": {
            1: {
                "question": "What does ACID stand for in DBMS?",
                "options": ["A) Atomicity, Consistency, Isolation, Durability", "B) Addition, Consistency, Isolation, Durability", "C) Addition, Correctness, Isolation, Database", "D) Atomicity, Concurrency, Integrity, Durability"],
                "answer": "A"
            },
            2: {
                "question": "Which SQL keyword is used to retrieve unique values?",
                "options": ["A) SELECT", "B) DISTINCT", "C) UNIQUE", "D) FETCH"],
                "answer": "B"
            },
            3: {
                "question": "What is a foreign key?",
                "options": ["A) A key that uniquely identifies a record in a table", "B) A key used to connect two tables", "C) A key that is primary in one table and foreign in another", "D) Both B and C"],
                "answer": "D"
            },
            4: {
                "question": "Which command is used to remove a table from a database?",
                "options": ["A) REMOVE", "B) DELETE", "C) DROP", "D) ERASE"],
                "answer": "C"
            },
            5: {
                "question": "What is normalization in DBMS?",
                "options": ["A) Organizing data to avoid duplication", "B) Organizing data to ensure referential integrity", "C) Organizing data to reduce redundancy", "D) Organizing data to improve security"],
                "answer": "C"
            }
        }
    },
    "Python": {
        "questions": {
            1: {
                "question": "Which of the following is used to define a function in Python?",
                "options": ["A) def", "B) func", "C) lambda", "D) function"],
                "answer": "A"
            },
            2: {
                "question": "Which of these is a mutable data type in Python?",
                "options": ["A) Tuple", "B) String", "C) List", "D) Integer"],
                "answer": "C"
            },
            3: {
                "question": "Which of the following is used to handle exceptions in Python?",
                "options": ["A) try-except", "B) catch-finally", "C) throw-catch", "D) handle-catch"],
                "answer": "A"
            },
            4: {
                "question": "What is the output of print(2**3)?",
                "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
                "answer": "B"
            },
            5: {
                "question": "What is the correct file extension for Python files?",
                "options": ["A) .pyth", "B) .pt", "C) .py", "D) .python"],
                "answer": "C"
            }
        }
    }
}

def register():
    print("---- Registration ----")
    username = input("Enter username: ")
    if username in user_data:
        print("Username already exists! Try a different one.")
        return
    password = input("Enter password: ")
    email = input("Enter email address: ")
    full_name = input("Enter full name: ")
    age = input("Enter age: ")
    
    user_data[username] = {
        "password": password,
        "email": email,
        "full_name": full_name,
        "age": age,
        "quiz_attempted": False,
        "quiz_score": 0          
    }
    print(f"Registration successful for {username}!\n")

def login():
    print("---- Login ----")
    username = input("Enter username: ")
    if username in user_data:
        password = input("Enter password: ")
        if user_data[username]["password"] == password:
            print(f"Welcome, {username}!\n")
            return username
        else:
            print("Incorrect password!\n")
    else:
        print("Username not found!\n")
    return None

def attempt_quiz(username):
    print("---- Attempt Quiz ----")
    print("Select a subject to attempt:")
    print("1. DSA")
    print("2. DBMS")
    print("3. Python")
    
    choice = input("Enter the subject number (1-3): ")
    subjects = { '1': 'DSA', '2': 'DBMS', '3': 'Python' }
    
    if choice in subjects:
        subject = subjects[choice]
        questions = quiz_database[subject]["questions"]
        score = 0
        
        for q_num, q_data in questions.items():
            print(f"\nQuestion {q_num}: {q_data['question']}")
            for option in q_data['options']:
                print(option)
            answer = input("Enter your answer (A/B/C/D): ").upper()
            
            if answer == q_data["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {q_data['answer']}\n")
        
        user_data[username]["quiz_attempted"] = True
        user_data[username]["quiz_score"] = score
        print(f"You've completed the {subject} quiz! Your score is: {score}/5\n")
    else:
        print("Invalid choice. Please try again.")

def show_result(username):
    print("---- Show Result ----")
    if user_data[username]["quiz_attempted"]:
        score = user_data[username]["quiz_score"]
        print(f"{username}, your latest quiz score is: {score}/5\n")
    else:
        print(f"{username}, you have not attempted any quiz yet.\n")

def main_menu():
    logged_in_user = None
    
    while True:
        print("---- Main Menu ----")
        print("1. Registration")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. Show Result")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            logged_in_user = login()
        elif choice == '3':
            if logged_in_user:
                attempt_quiz(logged_in_user)
            else:
                print("You need to log in first!\n")
        elif choice == '4':
            if logged_in_user:
                show_result(logged_in_user)
            else:
                print("You need to log in first!\n")
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main_menu()
