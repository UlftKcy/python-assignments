first_number = 0
second_number = 1
fibonacci = []

while second_number <= 55 :
    sum = first_number + second_number
    first_number = second_number
    second_number = sum
    fibonacci.append(first_number)
print(fibonacci)