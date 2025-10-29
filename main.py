from game import io ,logic ,validate ,secret
import random
# if __name__ == "__name__":

while True:
        num = secret.generate_secret()
        m = user_guess = {0:"X" ,1:"X" ,2:"X" ,3:"X"  ,"cow":0 }
        print(f"the list secret is {m}")
        temp_io= io.io_user()
        io.io_user()


        logic.score_guess(num ,temp_io)

        u = validate.validate()
        if validate.validate() == "you wim":
            break
