"""
Task 1: The Selective DJ
Loop through a slice of the genres list from the previous question and print out the genres. Use slicing to create a sublist of genres from the second to the fourth track.
"""
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
"""
sub_genres = genres[1:]
print(sub_genres)
"""
"""
Task 2: The One-Liner Band with List Comprehensions
Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list.
"""
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

newlist = [x for x in genres]
newlist.append("Music")
print(newlist)

"""
Task 3: Numerical Beats with range
Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".
"""
"""
for i in range(10, -1, -1):
    print(f"Count {i}")
    if i == 0:
        print("The beat drops now!")
"""