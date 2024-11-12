""" 
Recursion Tasks:
  create a function that can generate 20 to 5 in reverse order
  create a function that will asks for user input 5 times and print after each input
"""

def sequence(num):
    if num < 5:
        return
    print(num)  
    sequence(num - 1) 
print(sequence(20))




def input():
    for i in range(5):
        user_input = input(f"Enter input {i+1}: ")
        print(f"You entered: {user_input}")
print(input())





        