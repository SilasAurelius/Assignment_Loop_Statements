"""
Task 1: Your Mood Today
Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.
"""
import random
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mood = ['happy', 'sad', 'energetic', 'calm', 'happy', 'over-joyed', 'tired']

mood_rand = mood
random.shuffle(mood)

for i in range(0, 7, 1):
    print(f"Today is: " + str(week[i]) + " and you were: " +  (mood_rand[i]))


