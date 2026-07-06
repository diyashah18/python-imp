#Implicit Type Conversion
a = 5
b = 3.5

result = a + b
print(result ,type(result))

#Explicit Type Conversion
a = "100"
b = "500"

#covert strings to int before addition 

_sum = int(a) + int(b)
print("sum", _sum , type(_sum))