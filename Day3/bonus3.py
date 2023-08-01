meals = ['pasta','pizza','salad']

for meal in meals:
    print(meal.capitalize())
print("Bye!")

for item in ["hello", "hi"]:
    print(item.upper())

names =["Dalay", "Smith", "Apex"]
 
for name in names:
    print("Next one is: ")
    print(name)

### exercise 
country = "India"

match country:
    case 'USA':
        print("Hello")
    case 'India':
        print("Namaste")
    case 'Germany':
        print("Hallo")