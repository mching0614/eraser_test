## This is a test Python script. Its purpose is to exercise and
## evaluate the Eraser.io tool
##

def get_input():
    name_input = input("Enter your name:")
    if name_input.lower().strip() == 'ryan':
        print("GEAUX TIGERS")
    else:
        print("You are not Ryan")
    return name_input

def get_score():
    bama_score = input("how many points did bama score:")
    lsu_score = input("how many points did lsu score")

    if lsu_score > bama_score:
        print("Get on the Lane Train!")
    else:
        print("Somebody fire this bum")

def national_champs():
    print("Who will be the national champs?")

    if True:
        print("LSU!!!")

if __name__ == "__main__":
    try:
        input_1 = get_input()
        input_2 = get_score()
        national_champs()
    except Exception as e:
        print(e)