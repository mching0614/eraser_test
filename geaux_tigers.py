def get_input():
    name_input = input("Enter your name:")
    if name_input.lower().strip() == 'ryan':
        print("GEAUX TIGERS")
    else:
        print("You are not Ryan")
    return name_input

def get_score():
    bama_score = input("how many points did Bama score:")
    lsu_score = input("how many points did LSU score:")
    if bama_score < lsu_score:
        print("all aboard the lane train")
    else:
        print("fire this bum")

if __name__ == "__main__":
    try:
        input = get_input()
        input_2 = get_score()
    except Exception as e:
        print(e)