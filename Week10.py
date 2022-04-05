def tutQuestion01():
    #Print "Hello Glasgow"
    print("Hello Glasgow!")

def tutQuestion02():
    #Lock till valid input is provided
    while(True):
        try:
            #Acquire user input
            xVal = input("Enter value for x: ")
            yVal = input("Enter value for y: ")

            #Validify if user input is numeric form
            xVal = float(xVal)
            yVal = float(yVal)

            #Exit lock
            break

        #User input is not in numeric form
        except ValueError:
            print("Invalid input...")
        print()

    #Calculate average
    avg = (xVal + yVal)/2

    #Display calculated average
    print("Average of x & y: " + str(avg))

def tutQuestion03(moduleCode):
    match moduleCode:
        case 'CSC1009':
            print("Object Oriented Programming")
        case 'CSC1008':
            print("Data Structures and Algorithm")
        case _:
            print("Invalid code")

def tutQuestion04():
        for x in range(102, 65, -1):
            if x % 2 == 1:
                print(str(x))

def run():
    """Week 10 Tutorial Questions"""
    tutQuestion01()
    tutQuestion02()
    tutQuestion03("CSC1009")
    tutQuestion04()


if __name__ == "__main__":
    run()