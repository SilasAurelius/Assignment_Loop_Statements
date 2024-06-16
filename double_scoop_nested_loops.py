"""
Task 1: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.
Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"
"""
import random
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
times = ['morning', 'afternoon', 'evening']
moods = ['happy', 'sad', 'energetic', 'calm']


random.shuffle(moods)

for i in days:
    for x in times:
        if i == "Sunday":
            print("Today is Sunday.")
            print("In the ", x, "you were", moods)
        elif i == "Monday":
            print("Today is Monday.")
            print("In the ", x, "you were", moods)
        elif i == "Tuesday":
            print("Today is Tuesday.")
            print("In the ", x, "you were", moods)
        elif i == "Wednesday":
            print("Today is Wednesday.")
            print("In the ", x, "you were", moods)
        elif i == "Thursday":
            print("Today is Thursday.")
            print("In the ", x, "you were", moods)
        elif i == "Friday":
            print("Today is Friday.")
            print("In the ", x, "you were", moods)
        else:
            print("Today is Saturday.")
            print("In the ", x, "you were", moods)
