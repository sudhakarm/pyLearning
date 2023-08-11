filenames = ["1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt"]

for filename in filenames:
    #strings are immutable, you cannot directly replace the char value like filename[1] = '-'. 
    filename = filename.replace('.','-',1)
    print(filename)

#create a tuple, its a immutable like strings.
filenames_tuple = ("1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt")

rate = 2
dollar = float(input("dollars:"))
print(dollar*rate)

#To find rank of student by number
ranking = ['John', 'Sen', 'Lisa']
rank = int(input("Enter rank number: "))
print(ranking[rank-1])

#to find name of student entering rank
ranking = ['John', 'Sen', 'Lisa']
name = input("Enter a name: ")
print(ranking.index(name)+1)