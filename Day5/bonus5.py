waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

filenames = ['document', 'report', 'presentation']
for i,j in enumerate(filenames):
    print(f"{i}-{j.capitalize()}.txt")

