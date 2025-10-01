import random

print("########")
print("Maths Tutor")
print("#########")

def expopnent():
    
    try:
        exponent_value = int(input("Enter a exponent value between 2/3/4: "))
    except ValueError:
        print("Invalid. Enter a number")
        return 
    
    if exponent_value in (2,3,4):
        if exponent_value == 2:
            number = exponent_value
            for i in range(1,13):
                result = i **2 #exponent_value
                print(i, " Squared by 2 = ", result)
            
        elif exponent_value == 3:
            number = exponent_value
            for i in range(1,13):
                result = i ** 3 #exponent_value
                print(i, " Squared by 2 = ", result)
                
        elif exponent_value == 4:
            number = exponent_value
            for i in range(1,13):
                result = i ** 4 #exponent_value
                print(i, " Squared by 2 = ", result)
    
    else:
        print("can only be 2/3/4")
    
    

def multiplication_table():
    try:
        number = int(input("Enter a number between 1 and 12 for the multiplication table: "))
        
        for i in range(1,13):
        
            for j in range(1,number+1):
                result =i*j
                print(result, end="\t")
            print()
    except ValueError:
        print("Not a valid number try again")
        return
    
def test():
    number = int(input("Enter a number between 1 and 12 to test with: "))
    if 1 <= number <= 12:
        correct_count = 0
        
        for _ in range(5):  # 5 random questions
            multiplier = random.randint(1, 12)
            correct_ans = number * multiplier
            user_ans = int(input(f"{number} x {multiplier} = "))
            
            if user_ans == correct_ans:
                correct_count += 1

        percentage = (correct_count / 5) * 100
        print(f"You got {correct_count}/5 correct ({percentage}%).")

        if correct_count >= 4:
            print("Well done!")
        else:
            print("You need to revise")
        
    else:
        print("Value is outside the range of 1-12")
        
        
    
def main():
    while True:
        name= input("Please enter your name:?")
        print("*******************")
        print("Menu")
        print("*******************")
        print("1. Exponents")
        print("2.Multiplication Table")
        print("3.Test your Knowledge")
        print("4.Exit")
        print("*******************")
        #print(f"{name} , please select a menu option(1-4).")
        
        choice = input(f"{name} , please select a menu option(1-4).")
        if choice == "4":
            return 
            print("closing the sytstem")
        elif choice == "1":
            print("\nExponents")
            expopnent()
            
        elif choice == "2":
            print("*******************")
            print("\nMultiplication Table")
            multiplication_table()
            
        elif choice == "3":
            print("*******************")
            print("\nTest your knowledge")
            test()
    
    
    
    
    
#
main()