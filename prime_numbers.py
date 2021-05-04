n = int(input("Enter a limited number :"))
prime_list = []

for i in range(2,n):
    count = 0
    for ii in range (2,10):
        if i > ii :
            if i % ii == 0 :
                count += 1
                break
    if count == 0 :
        prime_list.append(i)
    else :
        continue
print(prime_list)