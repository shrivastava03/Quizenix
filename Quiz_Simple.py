import random

users = {}  

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users[username] = password
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please register first.")
        return False

def quiz(topic):
    questions = {
    "Machine Learning": [
        {
            "question": "What is the core idea behind supervised learning?",
            "options": [
                "Training a model on labeled data",
                "Training a model on unlabeled data",
                "Using reinforcement learning techniques",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is unsupervised learning?",
            "options": [
                "Training a model on labeled data",
                "Training a model on unlabeled data",
                "Using reinforcement learning techniques",
                "None of the above"
            ],
            "answer": "B"
        },
        {
            "question": "Which algorithm is used for classification and regression tasks?",
            "options": [
                "Linear Regression",
                "Logistic Regression",
                "Support Vector Machines (SVM)",
                "All of the above"
            ],
            "answer": "D"
        },
        {
            "question": "What is overfitting in Machine Learning?",
            "options": [
                "A model performs well on training data but poorly on unseen data",
                "A model performs poorly on training data but well on unseen data",
                "A model performs equally well on both training and test data",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What does the term 'bias' refer to in a model?",
            "options": [
                "The error due to overly simple assumptions",
                "The variance in the model predictions",
                "The error caused by noise in the data",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is a decision tree?",
            "options": [
                "A supervised learning model",
                "A clustering algorithm",
                "A type of reinforcement learning model",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "Which technique helps prevent overfitting?",
            "options": [
                "Cross-validation",
                "Adding more features",
                "Ignoring regularization",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is gradient descent?",
            "options": [
                "An optimization algorithm to minimize the loss function",
                "A data scaling technique",
                "An algorithm for clustering data",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is a confusion matrix?",
            "options": [
                "A matrix used to evaluate classification models",
                "A matrix that performs data scaling",
                "A matrix for clustering",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is a neural network?",
            "options": [
                "A set of algorithms modeled after the human brain",
                "A regression algorithm",
                "A type of clustering model",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is reinforcement learning?",
            "options": [
                "A learning method based on rewards and penalties",
                "Training on labeled data",
                "Using clustering algorithms",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is the purpose of a validation dataset?",
            "options": [
                "To tune hyperparameters of the model",
                "To train the model",
                "To test the model",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "Which algorithm is commonly used for dimensionality reduction?",
            "options": [
                "Principal Component Analysis (PCA)",
                "K-Means Clustering",
                "Linear Regression",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is the role of a cost function?",
            "options": [
                "To measure the error of the model's predictions",
                "To optimize feature scaling",
                "To visualize data",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is ensemble learning?",
            "options": [
                "Combining multiple models to improve performance",
                "Using only one model for predictions",
                "Scaling features in data",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "Which of the following is a type of ensemble method?",
            "options": [
                "Random Forest",
                "Gradient Boosting",
                "Bagging",
                "All of the above"
            ],
            "answer": "D"
        },
        {
            "question": "What is a hyperparameter?",
            "options": [
                "A parameter set before the learning process",
                "A parameter learned during training",
                "A variable used for scaling data",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is feature scaling?",
            "options": [
                "Scaling features to a standard range",
                "Removing redundant features",
                "Adding new features",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "Which of the following is a clustering algorithm?",
            "options": [
                "K-Means",
                "Decision Tree",
                "Linear Regression",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is the purpose of cross-validation?",
            "options": [
                "To evaluate the model's performance",
                "To train the model on the entire dataset",
                "To preprocess the data",
                "None of the above"
            ],
            "answer": "A"
        }
    ],
    
    "Artificial Intelligence": [
        {
            "question": "What is Artificial Intelligence?",
            "options": [
                "A system that can mimic human behavior",
                "A system that performs logical computations",
                "A system that is based on neural networks only",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is the Turing Test?",
            "options": [
                "A test to measure a machine's learning ability",
                "A test to determine if a machine exhibits intelligent behavior",
                "A test to evaluate the efficiency of a neural network",
                "None of the above"
            ],
            "answer": "B"
        },
        {
            "question": "Which of the following is a common application of AI?",
            "options": [
                "Image recognition",
                "Speech processing",
                "Autonomous vehicles",
                "All of the above"
            ],
            "answer": "D"
        },
        {
            "question": "What does NLP stand for in AI?",
            "options": [
                "Natural Logic Processing",
                "Natural Language Processing",
                "Neural Language Processing",
                "None of the above"
            ],
            "answer": "B"
        },
        {
            "question": "What is machine learning in the context of AI?",
            "options": [
                "A subset of AI focused on learning from data",
                "A type of robotics",
                "A type of deep learning algorithm",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "Which algorithm is commonly used in AI for decision-making?",
            "options": [
                "A* Algorithm",
                "Linear Regression",
                "Random Forest",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is an expert system?",
            "options": [
                "A program that mimics the decision-making ability of a human expert",
                "A program that generates random decisions",
                "A neural network model",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is the primary objective of reinforcement learning?",
            "options": [
                "Maximizing a reward signal",
                "Minimizing data usage",
                "Optimizing feature scaling",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What does an AI agent consist of?",
            "options": [
                "Sensors and actuators",
                "A decision-making process",
                "Both A and B",
                "None of the above"
            ],
            "answer": "C"
        },
        {
            "question": "What is fuzzy logic?",
            "options": [
                "A method of reasoning resembling human reasoning",
                "A type of neural network",
                "A reinforcement learning algorithm",
                "None of the above"
            ],
            "answer": "A"
        },
        
    ],
    
    "Data Science": [
        {
            "question": "What is the primary goal of Data Science?",
            "options": [
                "To extract meaningful insights from data",
                "To build databases",
                "To create visualizations only",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "Which of the following is NOT a step in the Data Science workflow?",
            "options": [
                "Data cleaning",
                "Data analysis",
                "Data visualization",
                "Data fabrication"
            ],
            "answer": "D"
        },
        {
            "question": "Which programming language is most commonly used in Data Science?",
            "options": [
                "Python",
                "Java",
                "C++",
                "Ruby"
            ],
            "answer": "A"
        },
        {
            "question": "What is feature engineering?",
            "options": [
                "Creating new features or modifying existing ones to improve model performance",
                "Scaling features to standardize data",
                "Removing unnecessary columns",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is big data?",
            "options": [
                "Extremely large datasets that are difficult to process with traditional tools",
                "High-resolution images",
                "Cloud storage systems",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is the purpose of exploratory data analysis (EDA)?",
            "options": [
                "To summarize the main characteristics of the data",
                "To preprocess the data",
                "To deploy machine learning models",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What does SQL stand for?",
            "options": [
                "Structured Query Language",
                "System Query Logic",
                "Simple Query Language",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is a data pipeline?",
            "options": [
                "A series of steps to move and process data from one system to another",
                "A physical connection between servers",
                "A neural network for data processing",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "What is a data warehouse?",
            "options": [
                "A central repository for storing and managing large amounts of data",
                "A tool for data cleaning",
                "A data visualization tool",
                "None of the above"
            ],
            "answer": "A"
        },
        {
            "question": "Which of the following is a commonly used data visualization library in Python?",
            "options": [
                "Matplotlib",
                "TensorFlow",
                "PyTorch",
                "None of the above"
            ],
            "answer": "A"
        },
        
        
    ]
}

    if topic not in questions:
        print(f"Invalid topic '{topic}'. Please choose a valid topic.")
        return 0

    score = 0
    asked_questions = set()  
    available_questions = questions[topic]

    while len(asked_questions) < 5:  
        question = random.choice(available_questions)
        if question["question"] in asked_questions:
            continue
        asked_questions.add(question["question"])

        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {question['answer']}")

    print(f"\nQuiz finished! Your score: {score}/5")
    return score

if __name__ == "__main__":
    if not login():
        register()
        login()

    print("\nTopics:")
    print("1. Machine Learning")
    print("2. Artificial Intelligence")
    print("3. Data Science")
    topic_choice = input("Choose a topic (1/2/3): ").strip()

    topic_mapping = {
        "1": "Machine Learning",
        "2": "Artificial Intelligence",
        "3": "Data Science"
    }

    selected_topic = topic_mapping.get(topic_choice)
    if selected_topic:
        quiz(selected_topic)
    else:
        print("Invalid choice. Exiting.")
