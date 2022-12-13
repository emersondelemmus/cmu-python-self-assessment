## What is the value of Output = ?
output = 0
for i in [5, 2, 9, 6]:
    for j in [3, 1, 4, 3]:
        if j == 4:
            continue
        output += j
    if i == 9:
        break
    output *= i

print(output)