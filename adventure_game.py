"""A tiny command-line choose-your-own-adventure game."""


def prompt_choice(question, options):
    print(question)
    for key, label in options.items():
        print(f"  {key}) {label}")

    while True:
        choice = input("Choose an option: ").strip().lower()
        if choice in options:
            return choice
        print("Invalid option. Please try again.")


def play_game():
    print("Welcome to the Forest Quest!")
    path = prompt_choice(
        "You enter a forest and find two paths. Which way do you go?",
        {"l": "Left path", "r": "Right path"},
    )

    if path == "l":
        action = prompt_choice(
            "You meet a friendly wizard. What do you do?",
            {"t": "Talk to the wizard", "w": "Walk away quietly"},
        )
        if action == "t":
            print("The wizard gives you a map. You find treasure and win!")
        else:
            print("You get lost in the trees. Game over.")
    else:
        action = prompt_choice(
            "You find a river blocking your way. What do you do?",
            {"s": "Swim across", "b": "Build a raft"},
        )
        if action == "b":
            print("Your raft works! You cross safely and win!")
        else:
            print("The current is too strong. Game over.")


if __name__ == "__main__":
    play_game()
