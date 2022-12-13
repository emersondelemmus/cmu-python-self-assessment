#Consider the following incomplete function:

def shrink(num, calls=0):
    if num == 0:
        return calls
    else:
        return ______

#Fill in the Blank: Which of the following recursive cases will result in shrink(100) making the fewest number of recursive calls?

shrink(num / 100, calls + 1)
shrink(num - 25, calls + 1)
shrink(num % 5, calls + 1)
shrink(num // 10, calls + 1)
