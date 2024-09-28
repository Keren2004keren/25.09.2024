# START
# a
list_temp: list[float] = [34.2, 23.4, 21.34, 18.45]

# b
while True:
    temp: float = float(input("What is the temperature?: "))
    if temp == -999:
        break
    if temp > 50 or temp < -50:
        continue
    list_temp.append(temp)
print(list_temp)

# c
temp_extend: list[float] = [-20.0, 39.1, 18.5]
list_temp.extend(temp_extend)
print(list_temp)

# d
# The extend function changes the first list completely while the + just adds two lists together
list1: list[int] = [1, 2, 3]
list2: list[int] = [4, 5, 6]
list3: list[int] = list1 + list2
print(list3)
list1.extend(list2)
print(list1)
# as we can see the + feature made us a new list, and didn't change the previous lists, while the extend function changed the entire first list

# e
print(f"The highest temperature was {max(list_temp)}. ")
print(f"The lowest temperature was {min(list_temp)}. ")

# f
if 18.5 in list_temp:
    print("True.")
else:
    print("False.")

# g
print(list_temp.count(-20.0))

# h
print(f"The average of the temperatures is {sum(list_temp) / len(list_temp)}.")

# i
for i in list_temp:
    print(i)

# j
print(f"The index of 39.1 is {list_temp.index(39.1)}.")

# k
del list_temp[0]
print(list_temp)

# l
del list_temp[:2]
print(list_temp)

# m
list_temp.remove(18.5)
print(list_temp)
# you should check if the thing you want to remove is there because if not then the program will collapse.

# n
temp_last: float = list_temp.pop()
print(temp_last)

# o
save_temp_list = list_temp.copy()
save_temp_list.sort()
print(save_temp_list)

# p
new_temp_list = save_temp_list.copy()
new_temp_list.sort(reverse=True)
print(new_temp_list)

# STOP
