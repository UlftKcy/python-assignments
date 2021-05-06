for i in range(1,100) :
    if (i % 3 == 0) and (i % 5 == 0) :
        print("multiple of 3 and 5 :", "FizzBuzz")
    elif i % 3 == 0 :
        print("multiple of 3 :", "Fizz")
    elif i % 5 == 0 :
        print("multiple of 5 :", "Buzz")
    else :
        print("rest of the numbers :", i)