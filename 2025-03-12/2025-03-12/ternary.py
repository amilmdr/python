a, b = 10, 20
min_value = a if a < b else b
print("Minimum:", min_value)  # Output: Minimum: 10



num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Odd

x = 10
y = 20
z = 5

min_value = x if (x < y and x < z) else (y if y < z else z)
print("Minimum:", min_value)  # Output: Minimum: 5


age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)


