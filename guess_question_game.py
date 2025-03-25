questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2+2?", "answer": "4"},
    {"question": "What color is the sky?", "answer": "blue"}
]

def python_guess_game():
    total_questions = len(questions)
    score = 0

    for question in questions:
        print(question["question"])
        user_answer = input("Which is the correct answer? : ").strip().lower()
        correct_answer = question["answer"].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {question['answer']}.\n")

    print(f"Game over! Your final score is: {score}/{total_questions}")

python_guess_game()
