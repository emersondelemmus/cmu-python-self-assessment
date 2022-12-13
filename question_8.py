#What is the value of result

def nested_magic_function(x):
    def inner(y):
        return x+2**y-x
    return inner

func_dg = nested_magic_function(1)
result = func_dg(6)
print(result)