import random
def generate_secret(length:int=4 , unique_digits:bool = True ,allow_leading_zero:bool = False ,max_tries=None):
    secret_num = []
    counter = 0
    while counter != length:
        num = random.randrange(1 ,999)
        if num not in secret_num:
            secret_num.append(num)
            counter +=1
    # print("max_tries:" , {max_tries})




    return secret_num



