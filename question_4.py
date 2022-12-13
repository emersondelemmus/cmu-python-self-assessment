## What are the contents of `final_list` at the end of this script?

final_list = [1, 3, 5, 7, 9]
a = [0, 2, 4]
b = a * 2
c = sum(a)

final_list.extend(a)
print(f"final_list: ", final_list)

final_list.append(b)
print(f"final_list: ", final_list)

final_list.pop()
print(f"final_list: ", final_list)

final_list.pop(0)
print(f"final_list: ", final_list)

final_list.remove(3)
print(f"final_list: ", final_list)

final_list.insert(2, c)
print(f"final_list: ", final_list)

print(f"Sum: ", sum(final_list))