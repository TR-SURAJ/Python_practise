instr = 'amabama'
half = int(len(instr)/2)
print(half)


if (len(instr)%2 == 0):
    first_str = instr[:half]
    second_str = instr[half:]
    if first_str == second_str:
        print("symmetrical")
    else:
        print("not symmetrical")

    if first_str == second_str[::-1]:
        print("it is pallindrome")
    else:
        print("not pallindrome")
elif(len(instr)%2 == 1):
    print("Inside odd")
    first_str = instr[:half]
    second_str = instr[half+1:]
    if first_str == second_str:
        print("symmetrical")
    else:
        print("not symmetrical")

    if first_str == second_str[::-1]:
        print("it is pallindrome")
    else:
        print("not pallindrome")
