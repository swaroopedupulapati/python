#for-else
for i in range(5):
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
else:
    print("No Negative values Entered")

print("============================================")

# while-else
start = 0
while start < 5:
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
    start += 1
else:
    print("No Negative values Entered")
