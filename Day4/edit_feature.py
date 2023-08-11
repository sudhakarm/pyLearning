todos = []
#this program will take user's input to add todos to a string
while True:
    # add new feature edit in the list of allowed actions
    user_action = input("Type add, show, edit or exit: ")
    #since "add" is not eq to "add ", use strip
    user_action = user_action.strip()

    #use match case instead of if-elseif multiple times
    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todo = todo.capitalize()
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            print(todos)
        case 'exit':
            break
print("Bye!")

#this will never execute
print(type(todos))