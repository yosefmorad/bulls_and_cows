from game import logic ,secret ,io

def validate():
    a = logic.score_guess(secret,io)
    # b = secret.generate_secret()
    if a.bull  == 4:
        return "you win"
print(validate())

