import csv
from datetime import date

with open('PopChange.csv') as pop_list:
    reader1 = csv.reader(pop_list, delimiter=',')
    header = next(reader1)
with open('Housing.csv', 'r') as housing:
    reader2 = csv.reader(housing)
    header2 = next(reader2)

print("Name: Jose Reyes")
print("Course: SDEV300")
print("Date: ", date.today())

print("***************** Welcome to the Python Data Analysis App**********")

choice = int(0)


def pop_change():
    """Population function"""
    print("You have entered Population Data.Select the Column you want to analyze:")

    for row in reader1:
        april_pop = row[5]
        print(april_pop)

    op = ''
    while op != 'a' or 'b' or 'c' or 'd':
        print("a. Pop Apr 1 ")
        print("b. Pop Jul 1 ")
        print("c. Change Pop ")
        print("d. Exit Column ")
        print(pop_change)

        op = input("Enter your option: ")
        op = op.lower()
        count = 0

        if op == 'a':
            print("You have entered Population Data.Select the Column you want to analyze:")
            print("The statistics for this column are: ")
            line = pop_list.readline()
            count += 1
            if len(line) == 0:
                break
            print(line, end='')
        print("Count: ", count - 1)


pop_change()


def main():
    """Main function"""
    while choice != 3:
        print("Select the file you want to analyze: ")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program ")

        choice = int(input("Enter your choice from 1-3:"))
        opcode = []
        result = opcode[choice - 1]()
        if choice > 3 or choice == 0:
            print("Invalid entry: has to be a number from 1-3")
        elif choice == 3:
            print("Thank you for using this app ")
            break
        print(result)
