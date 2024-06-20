"""
Task 1: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.
Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"
"""
import random
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
times = ['morning', 'afternoon', 'evening']
moods = ['happy', 'sad', 'energetic', 'calm']



for i in days:
    for x in times:
        print(f"Today is {i} in the {x}, you feel {random.choice(moods)}")    
        
        