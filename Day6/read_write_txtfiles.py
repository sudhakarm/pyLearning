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
            
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            print()
            todos.append(todo)
            
            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            #use enumerate func to show numbers
            for index, item in enumerate(todos):
                #print(index,'-', item) is one way of printing. But we can use f-string for the same
                print(f"{index+1}: {item}")
        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1
            new_todo = input("Enter new todo: ")
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            todos[number] = new_todo
            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()
            print(todos)
        case 'complete':
            #we want to modify/manipulate the list by removing an item. Means we complete from todo list
            number = int(input("Number of the todo to complete: "))
            
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            todos[number] = new_todo
            file = open('todos.txt','w')
            todos.pop(number-1)
            file.writelines(todos)
            file.close()
        case 'exit':
            break
print("Bye!")

#this will never execute
print(type(todos))