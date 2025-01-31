Q1
def greeting():
    name = input("What is your name?\n")
    age = int(input("And how old are you?\n"))
    print("Hello! Your name is", name, "and you are", age, "years old.")



#Q2
def determine_data_type(value):
    if type(value) == str:
        print("Your input is a string!")
    elif type(value) == int:
        print("Your input is an integer!")
    elif type(value) == bool:
        print("Your input is a boolean value!")
    elif type(value) == float:
        print("Your input is a float value!")
        
        
        
#Q3
def list_operations():
    myList = ["blue", "red", "yellow", "green"]
    print("Here is the original list: ", myList)
    
    myList.append("purple")
    myList.append("pink")
    
    print("Here is the list after adding two new items: ", myList)
    
    myList.pop()
    print("Here is the list after removing an item: ", myList)
     
     
     
#Q4
def  tuple_unpacking():
    shapeTuple = ("circle", "square", "triangle", "rectangle")
    print("Original Tuple: ", shapeTuple)
    (shape1, shape2, *otherShapes) = shapeTuple #unpacking the first two
    
    print("First element in the tuple:", shape1)
    print("Second element in the tuple:", shape2)
    
    
    
#Q5
def student_dictionary():
    studentDict = {}
    
    for i in range(5):
        print("Enter the name of student #", i+1, ": ")
        name = input()
        print("Enter the grade of student #", i+1, ": ")
        grade = input()
        studentDict[name] = grade
        
    print("Here is the student dictionary:", studentDict)

    
#Q6
def set_operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    print("Set 1:", set1)
    print("Set 2:", set2)
    
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference:", set1 - set2)
    
#Q7
def number_checker(num):
    if num == 0:
        print("Your number is zero!")
    elif num < 0:
        print("Your number is negative!")
    else:
        print ("Your number is positive!")
        
    if num%2 == 0 and num != 0:
        print ("Your number is also even!")
    elif num%2 != 0 and num != 0:
        print("Your number is also odd!")
    
    
#Q8
def fizz_buzz():
    for i in range(1, 51):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
    
    
#Q9
def factorial(num):
    result = 1

    if num < 0:
        print("Error! :(")
    elif num == 0 or num == 1:
        print("The factorial of", num, "is 1")
    else:
        for i in range(2, num + 1):
            result *= i
        print("The factorial of", num, "is", result)
    
    
#Q10
def is_prime(num):
    
    isPrime = True
    endCondition = int(num**0.5) + 1
    
    if num < 2:
        isPrime = False
    else:
        for i in range(2, endCondition):
            if num % i == 0:
                isPrime = False
                break
    
    if isPrime == False:
        print("Your number is composite!")
    else:
        print("Your number is prime!")
    
    
#Q11
def list_of_squares(myList):
    newList = []
    
    for i in range (len(myList)):
        newList.append(myList[i] * myList[i])
        
    print("Original list:", myList)
    print("List of squares:", newList)
    return newList



#Q12
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)
    print("Merged dictionary:", merged_dict)
    return merged_dict


#Q13
def remove_list_duplicates(myList):
    seen = set()
    unique_list = []
    
    for num in myList:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)
    
    return unique_list


#Q14
def palindrome_checker(myString):
    i = 0
    j = len(myString)-1
    flag = True
    
    while i <= j:
        if myString[i] != myString[j]:
            flag = False
            break
    if flag:
        print("Yes! Palindrome")
    else:
        print("Not a palindrome :(")
        
        
        
#Q15
def fibonacci(n):
    if n == 1:
        return [0]  
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for _ in range(n - 2): 
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    print("Fibonacci Sequence:", fib_sequence)
    return fib_sequence

#Q20
def temp_converter(value, option): # 1: C to F / 2: F to  C
    if option == 1:
        print(value, "C = ",(value*9/5)+32, "F")
    elif option == 2:
        print(value, "F = ",(value - 32)*5/9, "C")
    else:
        print("Invaid option ID :(")
        
#main
