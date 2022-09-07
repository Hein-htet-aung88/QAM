
def sayhi(name, height):
    print("hey "+name+ " u suck ya:P"+ ". you are "+ height + " cm tall:<<")

sayhi("lilin","173")

def power4(number):
    return  number*number*number*number
#cannot put any code after "return"

result = power4(8)
print(power4(6))
print(result)

def num(no1,no2,no3,no4):
    if no1 >= no2 and no1 >= no3 and no1 >= no4:
        return no1
    elif no2 >= no1 and no2 >= no3 and no2 >=no4:
        return no2
    else:
        return no4

print(num(8,88,4,5))


