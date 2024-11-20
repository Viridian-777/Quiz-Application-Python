import re

filename = "registration_info.txt"
result_file = "result.txt"

def get_valid_phone():
    while True:
        phone = input("Enter your phone number (10 digits only): ")
        if phone.isdigit() and len(phone) == 10 and phone[0] in "6789":
            return phone
        print("Invalid phone number.")

def get_valid_name():
    while True:
        name = input("Enter your name (alphabets only): ")
        if name.isalpha():
            return name
        print("Invalid name. Please enter alphabets only.")

def get_valid_email():
    while True:
        email = input("Enter your email (e.g., xyz@gmail.com): ")
        if re.match(r'^[\w\.-]+@gmail\.com$', email):
            return email
        print("Invalid email format. Please enter a valid email.")

def get_valid_password():
    while True:
        password = input("Enter your password (at least 8 characters, 1 uppercase letter, 1 number, and 1 special character): ")
        if re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            return password
        print("Password must be at least 8 characters long, contain at least one uppercase letter, one number, and one special character.")

def save_registration_info(filename, phone, name, email, password):
    with open(filename, 'a') as file:
        file.write(f"Phone: {phone}\nName: {name}\nEmail: {email}\nPassword: {password}\n\n")
    print("Registration successful!")

def check_login_credentials(filename, email, password):
    with open(filename, 'r') as file:
        content = file.read()
    entries = re.findall(r"Email:\s*(\S+)\nPassword:\s*(\S+)", content)
    for stored_email, stored_password in entries:
        if email.strip().lower() == stored_email.lower() and password.strip() == stored_password:
            return True
    return False

def registration():
    print("Registration Form")
    name = get_valid_name()
    email = get_valid_email()
    password = get_valid_password()
    phone = get_valid_phone()
    save_registration_info(filename, phone, name, email, password)

def login():
    while True:
        print("Login Form")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if check_login_credentials(filename, email, password):
            print("Login successful!")
            return email
        print("Invalid email or password. Please try again.")
        exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()
        if exit_choice == 'yes':
            print("Exiting the system.")
            break

def show_quiz(email):
    print("\nChoose quiz type:")
    print("1. Python")
    print("2. DBMS")
    print("3. DSA")
    quiz_choice = input("Enter your choice (1, 2, or 3): ")
    questions = {
        "python": [
            {"question": "What is the output of the following code: `print(type([]))`?", "options": ["<class 'list'>", "<class 'tuple'>", "<class 'set'>", "<class 'dict'>"], "answer": "<class 'list'>"},
            {"question": "Which of the following is used to define a block of code in Python?", "options": ["Braces", "Parentheses", "Indentation", "Semicolons"], "answer": "Indentation"},
            {"question": "What is the correct way to open a file for writing in Python?", "options": ["open('file.txt', 'r')", "open('file.txt', 'w')", "open('file.txt', 'x')", "open('file.txt', 'a')"], "answer": "open('file.txt', 'w')"},
            {"question": "Which of the following methods is used to add an element to a list?", "options": ["append()", "add()", "insert()", "extend()"], "answer": "append()"},
            {"question": "What is the output of `bool(0)` in Python?", "options": ["True", "False", "None", "Error"], "answer": "False"}
        ],
        "dbms": [
            {"question": "Which of the following is a valid SQL data type?", "options": ["STRING", "CHAR", "FLOAT", "Both CHAR and FLOAT"], "answer": "Both CHAR and FLOAT"},
            {"question": "What is the primary key?", "options": ["A unique identifier for a record", "A foreign key", "A default key", "An optional key"], "answer": "A unique identifier for a record"},
            {"question": "What does ACID stand for in DBMS?", "options": ["Atomicity, Consistency, Isolation, Durability", "Access, Control, Integration, Data", "Accuracy, Consistency, Integrity, Durability", "Atomicity, Clarity, Integration, Durability"], "answer": "Atomicity, Consistency, Isolation, Durability"},
            {"question": "Which of the following is a NoSQL database?", "options": ["MongoDB", "MySQL", "Oracle", "PostgreSQL"], "answer": "MongoDB"},
            {"question": "What does the JOIN clause do in SQL?", "options": ["Combines rows from two or more tables", "Deletes rows from a table", "Adds new rows to a table", "Modifies rows in a table"], "answer": "Combines rows from two or more tables"}
        ],
        "dsa": [
            {"question": "Which data structure uses LIFO (Last In, First Out)?", "options": ["Stack", "Queue", "Array", "Tree"], "answer": "Stack"},
            {"question": "What is the maximum number of nodes in a binary tree of height `h`?", "options": ["2^h", "2^(h+1)-1", "2^h-1", "2^(h-1)"], "answer": "2^(h+1)-1"},
            {"question": "Which of the following algorithms is used for finding the shortest path in a graph?", "options": ["Dijkstra's Algorithm", "Prim's Algorithm", "Kruskal's Algorithm", "DFS"], "answer": "Dijkstra's Algorithm"},
            {"question": "What is the time complexity of inserting an element into a heap?", "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "answer": "O(log n)"},
            {"question": "Which of the following data structures can be used to implement a priority queue?", "options": ["Heap", "Queue", "Stack", "Linked List"], "answer": "Heap"}
        ]
    }
    if quiz_choice == '1':
        quiz = questions["python"]
    elif quiz_choice == '2':
        quiz = questions["dbms"]
    elif quiz_choice == '3':
        quiz = questions["dsa"]
    else:
        print("Invalid choice.")
        return
    score = 0
    for idx, question in enumerate(quiz):
        print(f"\nQ{idx + 1}: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        answer = input("Enter the option number: ")
        if question['options'][int(answer) - 1] == question['answer']:
            score += 1
    print(f"\nYou scored {score} out of 5.")
    with open(result_file, 'a') as result_file_obj:
        result_file_obj.write(f"Email: {email}\nQuiz Type: {quiz_choice}\nScore: {score}/5\n\n")


def show_result():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if not check_login_credentials(filename, email, password):
        print("Invalid email or password.")
        return
    with open(result_file, 'r') as file:
        records = file.read()
    email_results = re.findall(rf"Email: {email}\nQuiz Type: (\d+)\nScore: (\d+)/5", records)
    if email_results:
        print(f"Results for {email}:")
        for quiz_type, score in email_results:
            quiz_name = {"1": "Python", "2": "DBMS", "3": "DSA"}.get(quiz_type, "Unknown")
            print(f"Quiz Type: {quiz_name}, Score: {score}/5")
    else:
        print("No quiz attempts found for this email.")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Attempt Quiz (if not logged in, log in first)")
        print("4. Show Result")
        print("5. Exit")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
        if choice == '1':
            registration()
        elif choice == '2':
            email = login()
        elif choice == '3':
            if 'email' in locals():
                show_quiz(email)
            else:
                print("Please log in first.")
        elif choice == '4':
            show_result()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
