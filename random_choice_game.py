"""
Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
"""
import random
item_list = ['comb', 'tooth brush', 'cup', 'drums', 'phone']

while True:
    guess = input(f"Guess which item! (comb/tooth brush/cup/drums/phone): ")
    if guess == random.choice(item_list):
        print("Great job! You're correct!")
        break
    else:
        print("Sorry, that is not the correct item!")


