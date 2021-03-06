def run(x):
    i = 0
    while(i < x):
        i+=1
        print(i)
    return i

def PrintFunc(x):
    if(type(x) != int or x < 0):
        return (-1)
    else:
        out = x
        if(x%3 == 0):
            out = "Fizz"
        if(x%5 == 0):
            out = "Buzz"
        if(x%3 == 0 and x%5 == 0):
            out = "FizzBuzz"

        print(out)
        return out
