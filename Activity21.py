x = 10
if x > 5:
    print("x is greater than 5")
print()
print()
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
print()
print()
x = 7
if x > 10:
    print("x is greater than 10")
elif x == 7:
    print("x is equal to 7")
else:
    print("x is less than or equal to 10 and not equal to 7")
print()
print()
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print()
print()
for i in range(5): #range(5) givess numbers 0,1,2,3,4
    print(i)
print()
print()
for letter in "Python":
    print(letter)
print()
print()
count = 0
while count < 5:
    print(count)
    count += 1 #Increment the counter
print()
print()
while True:
    name = input("Enter your name(or type 'exit' to stop): ")
    if name == "exit":
        break
    print(f"Hello, {name}!")
print()
print()
for i in range(10):
    if i == 5:
        break # Exit the loop when i is 5
    print(i)
print()
print()
for i in range(5):
    if i == 2:
        continue # Skip the iteration when i is 2
    print(i)
print()
print()
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print()
print()
for i in range (5):
    print(i)
else:
    print("Loop completed without a break.")