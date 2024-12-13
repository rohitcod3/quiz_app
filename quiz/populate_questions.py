from quiz.models import Question

def populate_questions():
    questions = [
        {
            "text": "What is 2 + 2?",
            "option_a": "3",
            "option_b": "4",
            "option_c": "5",
            "option_d": "6",
            "correct_option": "B"
        },
        {
            "text": "What is the capital of France?",
            "option_a": "Berlin",
            "option_b": "Madrid",
            "option_c": "Paris",
            "option_d": "Rome",
            "correct_option": "C"
        },
        {
            "text": "Which programming language is used in Django?",
            "option_a": "Python",
            "option_b": "Java",
            "option_c": "C++",
            "option_d": "Ruby",
            "correct_option": "A"
        },
    ]

    for q in questions:
        Question.objects.create(**q)
    print("Questions populated successfully!")
print(Question.objects.all())
if __name__ == "__main__":
    populate_questions()
