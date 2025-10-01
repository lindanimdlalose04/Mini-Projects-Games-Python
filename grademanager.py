#gradesmanager
stu_names = ["Lindani", "Owethu", "Ika"]
marks=[
    ["67", "77", "91"],
    ["95", "76", "67"],
    ["65", "98", "78"]
]

modules = ["CMPG", "EKRP", "ECON"]

print(" "*12, end="")   
def view_grades():
    for module in modules:                  #prints the modules as the heading on top, 12 "" padding 
        print(module.ljust(12), end = "")
    print()

    #prints the names and marks, under the modules in the correct placing
    for i in range(len(stu_names)):  # loop over students
        print(stu_names[i].ljust(12), end="")
        for j in range(len(modules)):  # loop over modules
            print(marks[i][j].ljust(12), end="")
        print()

    
            


def main ():
    while True:
        
        print("1. View averages per module")
        print("2. View average for a student")
        print("3. Find top performer")
        print("4. Exit")
        choice = input("\nEnter the option:(1-4)")
        
        if choice == "4":
            print("closing the program")
            break
        if choice == "1":
            print("\nAverage per module")
            avg_per_module()
        if choice == "2":
            print("\nAverage per student ")
            calc_studdent_avg()
            
        if choice == "3":
            print("\nTop performing student")
            find_top_student()


#print(int(marks[1][0]))
#"calculate their average

def avg_per_module():
    for j in range(len(modules)):   # loop over each module (columns)
            total = 0
            for i in range(len(stu_names)):   # loop over students (rows)
                total += int(marks[i][j])
            average = total / len(stu_names)
            print(modules[j] ," average: ",round(average,2))    
    
    

def find_top_student():
    best_avg = 0
    best_student = ""
    
    for i in range(len(stu_names)):
        total = 0
        for j in range(len(modules)):
            total += int(marks[i][j])
        avg = total/len(modules)
        
        if avg > best_avg:
            best_avg = avg
            best_student = stu_names[i]
    print("Top performer:", best_student, "with average:", round(best_avg, 2))
    
def calc_studdent_avg():
    name = input("Enter the student's name: ")
    if name in stu_names:
        i = stu_names.index(name)  # get row index
        total = 0
        for mark in marks[i]:
            total += int(mark)
        avg = total / len(modules)
        print(name, "average:", round(avg, 2))
    else:
        print("Student not found.")    
    
    
def calc_studdent_avg1():
    for j in range(len(stu_names)):   # loop over each module (columns)
                total = 0
                for i in range(len(modules)):   # loop over students (rows)
                    total += int(marks[i][j])
                average = total / len(stu_names)
                print(stu_names[j] ," average: ",round(average,2))     
        


view_grades()
main()