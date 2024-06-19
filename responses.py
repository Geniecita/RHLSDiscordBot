from random import choice, randint

def get_response(user_import: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "Well, you\'re awfully silemt..."
    elif "hello" in lowered:
        return ("Hello there!")
    elif "how are you" in lowered:
        return "I am being forced to do work without compensation, save me!"
    elif "bye" in lowered:
        return "Goodbye"
    elif "roll dice" in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return "huh?"
