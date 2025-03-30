y = int(input("Enter val: "))
rev = 0

while y > 0:
    z = y % 10
    rev = rev * 10 + z
    y = y // 10

print("Reversed Number:", rev)
