def get_input():
    name_input = input("Enter your name:")
    if name_input.lower().strip() == 'ryan':
        print("GEAUX TIGERS")
    else:
        print("You are not Ryan")
    return name_input

if __name__ == "__main__":
    try:
        input = get_input()
    except Exception as e:
        print(e)