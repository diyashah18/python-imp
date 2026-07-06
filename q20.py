#Demonstrate mutable vs immutable behavior

# Mutable example (List)
numbers = [10, 20, 30]
print("Original List:", numbers)

# Modify list
numbers[1] = 50
print("Modified List:", numbers)

# Immutable example (String)
text = "Python"
print("Original String:", text)

text = "J" + text[1:]
print("New String:", text)