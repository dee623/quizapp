class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        user_answer = input("Your answer: ")
        if user_answer.lower() == question.answer.lower():
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {question.answer}\n")
    
    print(f"You got {score} out of {len(questions)} questions correct!")

def main():
    questions = [
        Question("What is the capital of France?\n(a) Berlin\n(b) Madrid\n(c) Paris\nYour answer: ", "c"),
        Question("Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\nYour answer: ", "b"),
        Question("What is the largest mammal in the world?\n(a) Elephant\n(b) Blue Whale\n(c) Giraffe\nYour answer: ", "b"),
        Question("What is the chemical symbol for water?\n(a) H2O\n(b) O2\n(c) CO2\nYour answer: ", "a"),
        Question("What is the smallest prime number?\n(a) 0\n(b) 1\n(c) 2\nYour answer: ", "c"),
    ]

    run_quiz(questions)

if __name__ == "__main__":
    main()
