# sequence[start:stop:step]

text = "Hello, World!"

print(text[0:5])   # Output: 'Hello' (characters from index 0 to 4)
print(text[:5])    # Output: 'Hello' (same as above, default start = 0)
print(text[7:])    # Output: 'World!' (from index 7 to end)
print(text[-6:-1]) # Output: 'World' (negative indexing)
print(text[::-1])  # Output: '!dlroW ,olleH' (reverse string)
print(text[::-2])
print(text[::2])
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:6])   # Output: [2, 3, 4, 5]
print(numbers[:4])    # Output: [0, 1, 2, 3]
print(numbers[5:])    # Output: [5, 6, 7, 8, 9]
print(numbers[::2])   # Output: [0, 2, 4, 6, 8] (every second element)
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse list)


tup = (10, 20, 30, 40, 50, 60)

print(tup[1:4])   # Output: (20, 30, 40)
print(tup[:3])    # Output: (10, 20, 30)
print(tup[::2])   # Output: (10, 30, 50)
print(tup[::-1])  # Output: (60, 50, 40, 30, 20, 10) (reverse tuple)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[:2])   # Output: [[1, 2, 3], [4, 5, 6]] (first two rows)
print([row[:2] for row in matrix])  # Output: [[1, 2], [4, 5], [7, 8]] (first two columns)



nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[1:8:2])   # Output: [1, 3, 5, 7] (every 2nd element from index 1 to 7)
print(nums[::-2])    # Output: [9, 7, 5, 3, 1] (reverse every second element)

text= "he ate camel food"
print(text[:2:-2])

