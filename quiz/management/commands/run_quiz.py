from django.core.management.base import BaseCommand
from quiz.models import QuizUser as User, Question, QuizResult
import random


class Command(BaseCommand):
    help = 'Run the CLI Quiz App'

    def handle(self, *args, **options):
        self.stdout.write("Welcome to the Quiz App!")
        current_user = None

        while True:
            if current_user:
                self.stdout.write(f"\nLogged in as: {current_user.username}")
                self.stdout.write("\nMenu:")
                self.stdout.write("1. Take Quiz")
                self.stdout.write("2. View Results")
                self.stdout.write("3. Logout")
                choice = input("Choose an option: ").strip()

                if choice == "1":
                    self.run_quiz(current_user)
                elif choice == "2":
                    self.view_results(current_user)
                elif choice == "3":
                    self.stdout.write("Logged out successfully.")
                    current_user = None  # Reset current_user
                else:
                    self.stdout.write("Invalid choice. Please try again.")
            else:
                self.stdout.write("\nMenu:")
                self.stdout.write("1. Register")
                self.stdout.write("2. Login")
                self.stdout.write("3. Exit")
                choice = input("Choose an option: ").strip()

                if choice == "1":
                    self.register_user()
                elif choice == "2":
                    current_user = self.login_user()  # Save logged-in user
                elif choice == "3":
                    self.stdout.write("Goodbye!")
                    break
                else:
                    self.stdout.write("Invalid choice. Please try again.")

    def register_user(self):
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()
        if User.objects.filter(username=username).exists():
            self.stdout.write("Username already exists!")
        else:
            User.objects.create(username=username, password=password)
            self.stdout.write("Registration successful!")

    def login_user(self):
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        try:
            user = User.objects.get(username=username, password=password)
            self.stdout.write("Login successful!")
            return user  # Return the logged-in user
        except User.DoesNotExist:
            self.stdout.write("Invalid credentials.")
            return None

    def run_quiz(self, user):
        questions = list(Question.objects.all())
        if not questions:
            self.stdout.write("No questions available.")
            return

        random.shuffle(questions)
        selected_questions = questions[:5]
        score = 0

        for question in selected_questions:
            self.stdout.write(f"\nQuestion: {question.text}")
            options = [question.option_a, question.option_b, question.option_c, question.option_d]
            for idx, option in enumerate(options, start=1):
                self.stdout.write(f"{idx}. {option}")

            while True:
                try:
                    answer = int(input("Your answer (1/2/3/4): ").strip())
                    if 1 <= answer <= 4:
                        if options[answer - 1] == getattr(question, f"option_{question.correct_option.lower()}"):
                            score += 1
                        break
                    else:
                        self.stdout.write("Please enter a valid option (1/2/3/4).")
                except ValueError:
                    self.stdout.write("Invalid input. Please enter a number (1/2/3/4).")

        QuizResult.objects.create(user=user, score=score)
        self.stdout.write(f"\nYour score: {score}/5")

        if score <= 2:
            self.stdout.write("Please try again!")
        elif score == 3:
            self.stdout.write("Good job!")
        elif score == 4:
            self.stdout.write("Excellent work!")
        elif score == 5:
            self.stdout.write("You are a genius!")

    def view_results(self, user):
        results = QuizResult.objects.filter(user=user).order_by('-timestamp')  # Fetch results sorted by the latest
        if not results.exists():
            self.stdout.write("No results found.")
        else:
            self.stdout.write("\nYour Past Results:")
            for result in results:
                self.stdout.write(f"Score: {result.score}/5, Date: {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
