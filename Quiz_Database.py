import mysql.connector as conn
import random
connection = conn.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="name of your database"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
for user in cursor.fetchall():
    print(user)

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    connection.commit()
    print("Registration successful! Please log in.\n")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        print(f"Welcome back, {username}!")
        return user['user_id']
    else:
        print("Login failed. Please register or check your credentials.\n")
        return None


def start_quiz(user_id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM topics")
    topics = cursor.fetchall()

    print("\nAvailable Topics:")
    for topic in topics:
        print(f"{topic['topic_id']}: {topic['topic_name']}")

    topic_id = int(input("Select a topic by entering the topic ID: "))

   
    cursor.execute("SELECT * FROM questions WHERE topic_id=%s", (topic_id,))
    questions = cursor.fetchall()
    random_questions = random.sample(questions, 5)

    score = 0
    for question in random_questions:
        print(f"\n{question['question_text']}")
        print(f"A. {question['option_a']}")
        print(f"B. {question['option_b']}")
        print(f"C. {question['option_c']}")
        print(f"D. {question['option_d']}")
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == question['correct_option']:
            print("Correct!")
            score += 2
        else:
            print("Incorrect.")
            score -= 0.5
            print("Correct answer is :" , question['correct_option'])

    
    cursor.execute("INSERT INTO scores (user_id, topic_id, score) VALUES (%s, %s, %s)", (user_id, topic_id, score))
    connection.commit()
    print(f"Quiz complete! Your score: {score:.2f}")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            register()
        elif choice == '2':
            user_id = login()
            if user_id:
                start_quiz(user_id)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()