todos = []
#this program will take user's input to add todos to a string
while True:
    # add new feature edit in the list of allowed actions
    user_action = input("Type add, show, edit, complete or exit: ")
    #since "add" is not eq to "add ", use strip
    user_action = user_action.strip()

    #use match case instead of if-elseif multiple times
    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todo = todo.capitalize()
            todos.append(todo)
        case 'show':
            #use enumerate func to show numbers
            for index, item in enumerate(todos):
                #print(index,'-', item) is one way of printing. But we can use f-string for the same
                print(f"{index+1}: {item}")
        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            print(todos)
        case 'complete':
            #we want to modify/manipulate the list by removing an item. Means we complete from todo list
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break
print("Bye!")

#this will never execute
print(type(todos))