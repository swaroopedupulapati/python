"""
complete the following with using only lambda
-> take two parameters(word, letter) and check if letter exists in word
   sample input: 
       codewala, w
   sample output:
       True
-> check if number is even and greater than 10 and divisible by 6
   sample input: 
       24
   sample output:
       True
"""


input = lambda word, letter: letter in word
word = "codewala"
letter = "w"
print(input(word, letter))  




number = lambda num: num % 2 == 0 and num > 10 and num % 6 == 0
num = 24
print(number(num)) 

