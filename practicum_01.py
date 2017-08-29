# Practice problem 2: Add two
# A simple program that adds 2 to a number ten times
def main():
    print("This program adds 2 to a number ten times")
    x = eval(input("Enter a number: "))
    for i in range(10):
        x = x + 2
        print(x)
        
main()