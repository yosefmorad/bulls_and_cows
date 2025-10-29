def io_user():
    user_input = []
    temp =input("enter number separated by space").split()
    for  i in temp:
        user_input.append(int(i))

    #if user_input  in treasure:
    return user_input
print(io_user())