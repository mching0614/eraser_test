## This is a test Python script. Its purpose is to exercise and
## evaluate the Eraser.io tool
##

def get_input():
    name_input = input("Enter your name: ")
    if name_input.lower().strip() == 'ryan':
        print("GEAUX TIGERS")
    else:
        print("You are not Ryan")
    return name_input

def get_score():
    bama_score = input("how many points did bama score?: ")
    lsu_score = input("how many points did lsu score?: ")

    if lsu_score > bama_score:
        print("Get on the Lane Train!")
    else:
        print("Somebody fire this bum")

def national_champs():
    print("Who will be the national champs?")

    if True:
        print("LSU!!!")
        print("Bama stinks")

def predict_wl():
    while True:
        try:
            wins_guess = int(input("LSU plays 12 games this season. How many games will they win?: "))
            if wins_guess == 12:
                print("You are purty smart!")
                break
            else:
                print("Incorrect. Try again")
        except ValueError:
            print("That's not a valid integer. Please input a number.")

def print_hello():
    print("Hello Sam")

if __name__ == "__main__":
    try:
        input_1 = get_input()
        input_2 = get_score()
        predict_wl()
        national_champs()
        print_hello()
    except Exception as e:
        print(e)