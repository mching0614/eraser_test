def get_input():
    name_input = input("Enter your name:")
    if name_input.lower().strip() == 'ryan':
        print("GEAUX TIGERS")
    else:
        print("You are not Ryan")
    return name_input

def get_score():
    bama_score = input("how many points did bama score:")
    print(bama_score)

if __name__ == "__main__":
    try:
        input_1 = get_input()
        input_2 = get_score()
    except Exception as e:
        print(e)