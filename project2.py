print("welcome to the pattern generator and number analyzer!")

while True:
    print("\nselect an option:")
    print("1. Generate a pattern")
    print("2. Analyze a number")
    print("3. Exit")
    
    choice = int(input("enter your choice (1, 2, or 3): ")) 
    
    match choice:
        case 1:
            n = int(input("enter the number of rows for the pattern: "))
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print("*", end="")
                print()
       
        case 2:
            start = int(input("enter the start of the range: "))
            end = int(input("enter the end of the range: "))
            total_sum = 0
            current = start 
          
            while current <= end:
                if current % 2 == 0:
                    print(f"{current} is even")
                else:
                    print(f"{current} is odd")
                
                total_sum += current
                current += 1  
                   
            print(f"sum of all numbers from {start} to {end} is: {total_sum}")
            
        case 3:
            print("exiting the program. goodbye!")
            break
            
        case _:
            print("invalid choice. please try again.")