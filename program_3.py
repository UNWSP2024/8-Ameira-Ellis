# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random
def capital_quiz():
    states_and_capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        # Add more states and capitals as needed
    }

    states = list(states_and_capitals.keys())
    correct_count = 0
    incorrect_count = 0

    for _ in range(5):  # Quiz with 5 questions
        state = random.choice(states)
        user_answer = input(f"What is the capital of {state}? ")

        if user_answer.strip().lower() == states_and_capitals[state].lower():
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect! The capital of {state} is {states_and_capitals[state]}.")
            incorrect_count += 1

    print(f"You got {correct_count} correct and {incorrect_count} incorrect.")
capital_quiz()

