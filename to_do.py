while True:

    answer = input("Do you want to add a new To-Do item? (y/n) or type exit: ")

    if answer == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

    elif answer == "y":
        todo = input("Type your new To-Do item: ")

        with open("to_do.txt", "a") as file:
            file.write(todo + "\n")

    elif answer == "n":
        list_answer = input("Do you want to list your To-Do items? (y/n): ")

        if list_answer == "y":

            try:
                with open("to_do.txt", "r") as file:
                    todos = file.readlines()

                    for todo in todos:
                        print(todo.strip())

            except FileNotFoundError:
                print("No To-Do items found.")

    else:
        print("Please enter y, n, or exit.")