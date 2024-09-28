# START

num_list: list[int] = []
while True:
    num: int = int(input("Enter a number between 0-10: "))
    if num == -999:
        break
    if num > 10 or num < 0:
        print("Invalid number")
        continue
    num_list.append(num)
    for i in range(11):
        counter = num_list.count(i)
        if counter > 0:
            print(f"Statistics[{i}]: {counter}", end=" ")
            print()

#STOP