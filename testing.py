import random
import time

# generates a math problem. returns the first num, second num, and operator
def generate_problem():
    operators = ['+', '-', '*', '/']
    op = random.choice(operators)
    num1 = random.randint(2, 9)  # 1-digit number
    num2 = random.randint(2, 99)  # 2-digit number

    if op == '/':
        # Ensure the division results in an integer
        num1, num2 = num2, random.randint(2, 9)
        num1 *= num2
    if op == '-':
        num1, num2 = max(num1, num2), min(num1, num2) # make sure num1 > num2
        # ai is smarter than me lol
    return num1, num2, op

# kinda obvious
def calculate_answer(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2


def main():
    easy_prob = []
    medium_prob = []
    hard_prob = []
    print("Welcome to the Mental Math Challenge!")
    print("You need to answer 10 questions as fast as you can.")
    while True: # loop for every game play
        start_time = time.time()
        problems_solved = 0

        while problems_solved < 10:
            num1, num2, op = generate_problem()
            correct_answer = calculate_answer(num1, num2, op)

            while True: # loop for each question
                try:
                    user_answer = int(input(f" {num1} {op} {num2}  "))
                    if user_answer == correct_answer:
                        print("Correct!")

                        # Get difficulty rating
                        while True:
                            rating = input(
                                "Rate the difficulty of this problem (Easy, Medium, Hard): "
                            ).strip().lower()
                            if rating in ['e', 'm', 'h']:
                                break
                            else:
                                print(
                                    "Invalid rating. Please enter Easy, Medium, or Hard."
                                )

                        # Save problem to the appropriate list
                        problem_str = f"{num1} {op} {num2}"
                        if rating == 'e':
                            easy_prob.append(problem_str)
                        elif rating == 'm':
                            medium_prob.append(problem_str)
                        elif rating == 'h':
                            hard_prob.append(problem_str)
                        problems_solved += 1
                        break
                    else:
                        print("Incorrect. Try again.")
                except ValueError:
                    print("Please enter a valid number.")

        end_time = time.time()
        total_time = end_time - start_time
        print(
            f"Congratulations! You completed 10 problems in {total_time:.2f} seconds."
        )
        # Print the categorized problems
        print("\nCategorized Problems:")
        print(f"Easy: {easy_prob}")
        print(f"Medium: {medium_prob}")
        print(f"Hard: {hard_prob}")
        
        input("press enter to play again.")


if __name__ == "__main__":
    main()
