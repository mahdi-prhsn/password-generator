# The first project i am going to do :)
#==================================methods======================================
def Random():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    length = 8
    new_password = ""

    for i in range(length):
        next_index = random.randrange(len(alphabet))
        new_password = new_password + alphabet[next_index]


    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(new_password)//2)
        new_password = new_password[0:replace_index] + str(random.randrange(10)) + new_password[replace_index+1:]


    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(new_password)//2,len(new_password))
        new_password = new_password[0:replace_index] + new_password[replace_index].upper() + new_password[replace_index+1:]

    return new_password


a = Random()
print(a)
