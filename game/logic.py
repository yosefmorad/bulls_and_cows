import game.io
def score_guess(secret  ,guess):
    user_guess = {0:"X" ,1:"X" ,2:"X" ,3:"X"  ,"cow":0 }
    bull = 0

    row = 0
    guess()
    for i ,v in  enumerate(guess):
        if v in secret:
            if i == secret.index(v):
                print(f"{v} bull")
                user_guess[i]=v
                bull += 1
            else:
                print(f"{v} cow")
                user_guess["cow"] = v
                row += 1
        else:
            print(f"{v}  no bull no cow")
    print( f"{user_guess } you have {bull} bulls and {row} row")

    return bull

print(score_guess([1 ,2 ,3] ,game.io.io_user))