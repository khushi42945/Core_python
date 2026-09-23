# 2. Fibonacci Sequence up to N TermsProblem Statement:Using a loop, generate and display the first $N$ terms of the Fibonacci sequence ($0, 1, 1, 2, 3, 5, 8, \dots$).The sequence begins with 0 and 1, and each subsequent term is the sum of the preceding two.

n = int(input("Enter the number of terms for the Fibonacci sequence: "))

num1 = 0
num2 = 1

print("Fibonacci Series:")
for i in range(n):
    print(num1, end=" ")
    
    next = num1 + num2
    num1 = num2
    num2 = next