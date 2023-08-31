print("Hello, welcome to AK quiz!, so lets find out how much you know about me. ")

ans = input ("Are you to ready to play (yes/no) : ")
score = 0
total_q = 5

if ans.lower() == "yes" :
    ans = input(f"1. What is my full name ? ")
    if ans.lower() == "aanik khapangi magar" :
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    ans = input(f"2. How many members are there in my family ? ")
    if ans == "4" :
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    ans = input(f"3. What is my favourite game ? (Name Only One)")
    if ans.lower() == "football" :

        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    

    ans = input(f"4. When is my birthday (English DOB) as (dd/mm/yy)? ")
    day = input("Enter date of day : ")
    month = input("Enter month name : ")
    year = input("Enter year : ")

    if  ans.lower() == "16/09/2003" and day == "16" and month.lower() == "september" and year == "2003" :
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    ans = input(f"5. What is my favourite colour (only one colour) ? ")
    if ans.lower() == "black" or ans.lower() == "white" or ans.lower() == "blue" :
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
if score == 1:
    print(f"Thank you for playing, you got {score} question correct.")
else:
    print(f"Thank you for playing, you got {score} questions correct.")
mark = (score / total_q) * 100
print(f"Mark: {mark}")
print("Goodbye!")
      

        
    
    
