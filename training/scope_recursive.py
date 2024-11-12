
name = "elena"
def homepage():
    global name
    name = "caroline"
homepage()
print(name)


def sequence(n):
    if n < 0:
        return n
    print(sequence(n-1))
sequence(5)
