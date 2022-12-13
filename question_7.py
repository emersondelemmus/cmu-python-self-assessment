#Consider the following function:

def magic_function(*args):
    values=[]
    for num in args:
        if (num*3) % 2 == 0:
            values.append(num*3)
        return values
#Which of the following function calls will return the following list:

#[6, 18, 42]
print(magic_function(2,4,6,8,14))
print(magic_function(6,18,42))
print(magic_function(2,6,14))
print(magic_function(1,2,3,6,7,14))