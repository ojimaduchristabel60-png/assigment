#number 1
from collections  import Counter
with open("story.txt","r") as file :
     text = file.read().lower().replace("."," ")
     words = text.split()
words_counts = Counter(words)
for word, count in words_counts.items():
     print(f"{word} : {count}")
#number2
line_count= 0
word_count =0
with open ("story.txt", "r") as file :
     for line in file:
          line_count += 1
          word_count+= len(line.split())
print (f" Number of lines in the file : {line_count}")
print(f" Number of words :{word_count}")

#number 3
with open("marks.txt" ,"r") as file :
     for line in file :
          line = line.strip() 
          if line:
               name, mark = line.split(",")
               status = "PASS" if int(mark) >=50 else "FAIL"
               print (f"{name} - {status}")
# number 4
import csv
highest_record = None
max_salary = -1
with open ("data.csv", "r")as file :
      reader = csv.DictReader(file)
      for row in reader :
           try:
             salary = float(row["salary"])
           except ValueError:
            continue
           if salary > max_salary:
                max_salary = salary
                highest_record = row
print(" Record with highest salary:", {highest_record})
print("Number 5")
#number 5
import csv
updated_rows =[]
with open ("data.csv", "r") as file:
     reader = csv.DictReader(file)
     fieldnames = reader.fieldnames
     for row in reader:
         if row["salary"].strip():
            row ["salary"] =round(float(row["salary"])  * 1.10,2)
            updated_rows.append(row)
with open("updated.csv","w",newline="") as file:
     writer = csv.DictWriter( file,fieldnames= fieldnames) 
     writer.writeheader()
     writer.writerows(updated_rows)
print("Updated file saved successfully as updated .csv !") 
print("Number 6")
# number 6   
#  Create and write sample data to expenses.txt
with open("expenses.txt", "w") as file:
    file.write("Food,25\nTransport,15\nFuel,60\n")

# 2. Read file and calculate total, highest, and lowest expenses
expenses = {}

with open("expenses.txt", "r") as file:
    for line in file:
        if line.strip():
            item, amount = line.strip().split(",")
            expenses[item] = float(amount)

# Calculate results
total_expense = sum(expenses.values())
highest_item = max(expenses, key=expenses.get)
lowest_item = min(expenses, key=expenses.get)

# Display results
print(f"Total Expense: ${total_expense}")
print(f"Highest Expense: {highest_item} (${expenses[highest_item]})")
print(f"Lowest Expense: {lowest_item} (${expenses[lowest_item]})") 
#number 7
print("NUMBER 7")
1. #Create and write sample data to expenses.txt
with open("expenses.txt", "w") as file:
    file.write("Food,25\nTransport,15\nFuel,60\n")

# 2. Read file and calculate total, highest, and lowest expenses
expenses = {}

with open("expenses.txt", "r") as file:
    for line in file:
        if line.strip():
            item, amount = line.strip().split(",")
            expenses[item] = float(amount)

# Calculate results
total_expense = sum(expenses.values())
highest_item = max(expenses, key=expenses.get)
lowest_item = min(expenses, key=expenses.get)

# Display results
print(f"Total Expense: ${total_expense}")
print(f"Highest Expense: {highest_item} (${expenses[highest_item]})")
print(f"Lowest Expense: {lowest_item} (${expenses[lowest_item]})")
print ("NUMBER 7")
1.# Create and write sample credentials to users.txt
with open("users.txt", "w") as file:
    file.write("admin,1234\njohn,password\n")

# 2. Accept input from user
username_input = input("Enter username: ").strip()
password_input = input("Enter password: ").strip()

# 3. Verify credentials against file data
login_successful = False

with open("users.txt", "r") as file:
    for line in file:
        if line.strip():
            stored_user, stored_pass = line.strip().split(",")
            if username_input == stored_user and password_input == stored_pass:
                login_successful = True
                break

# Display result
if login_successful:
    print("Login successful!")
else:
    print("Invalid username or password.") #number 1
from collections  import Counter
with open("story.txt","r") as file :
     text = file.read().lower().replace("."," ")
     words = text.split()
words_counts = Counter(words)
for word, count in words_counts.items():
     print(f"{word} : {count}")
#number2
line_count= 0
word_count =0
with open ("story.txt", "r") as file :
     for line in file:
          line_count += 1
          word_count+= len(line.split())
print (f" Number of lines in the file : {line_count}")
print(f" Number of words :{word_count}")

#number 3
with open("marks.txt" ,"r") as file :
     for line in file :
          line = line.strip() 
          if line:
               name, mark = line.split(",")
               status = "PASS" if int(mark) >=50 else "FAIL"
               print (f"{name} - {status}")
# number 4
import csv
highest_record = None
max_salary = -1
with open ("data.csv", "r")as file :
      reader = csv.DictReader(file)
      for row in reader :
           try:
             salary = float(row["salary"])
           except ValueError:
            continue
           if salary > max_salary:
                max_salary = salary
                highest_record = row
print(" Record with highest salary:", {highest_record})
print("Number 5")
#number 5
import csv
updated_rows =[]
with open ("data.csv", "r") as file:
     reader = csv.DictReader(file)
     fieldnames = reader.fieldnames
     for row in reader:
         if row["salary"].strip():
            row ["salary"] =round(float(row["salary"])  * 1.10,2)
            updated_rows.append(row)
with open("updated.csv","w",newline="") as file:
     writer = csv.DictWriter( file,fieldnames= fieldnames) 
     writer.writeheader()
     writer.writerows(updated_rows)
print("Updated file saved successfully as updated .csv !") 
print("Number 6")
# number 6   
#  Create and write sample data to expenses.txt
with open("expenses.txt", "w") as file:
    file.write("Food,25\nTransport,15\nFuel,60\n")

# 2. Read file and calculate total, highest, and lowest expenses
expenses = {}

with open("expenses.txt", "r") as file:
    for line in file:
        if line.strip():
            item, amount = line.strip().split(",")
            expenses[item] = float(amount)

# Calculate results
total_expense = sum(expenses.values())
highest_item = max(expenses, key=expenses.get)
lowest_item = min(expenses, key=expenses.get)

# Display results
print(f"Total Expense: ${total_expense}")
print(f"Highest Expense: {highest_item} (${expenses[highest_item]})")
print(f"Lowest Expense: {lowest_item} (${expenses[lowest_item]})") 
#number 7
print("NUMBER 7")
1. #Create and write sample data to expenses.txt
with open("expenses.txt", "w") as file:
    file.write("Food,25\nTransport,15\nFuel,60\n")

# 2. Read file and calculate total, highest, and lowest expenses
expenses = {}

with open("expenses.txt", "r") as file:
    for line in file:
        if line.strip():
            item, amount = line.strip().split(",")
            expenses[item] = float(amount)

# Calculate results
total_expense = sum(expenses.values())
highest_item = max(expenses, key=expenses.get)
lowest_item = min(expenses, key=expenses.get)

# Display results
print(f"Total Expense: ${total_expense}")
print(f"Highest Expense: {highest_item} (${expenses[highest_item]})")
print(f"Lowest Expense: {lowest_item} (${expenses[lowest_item]})")
print ("NUMBER 7")
1.# Create and write sample credentials to users.txt
with open("users.txt", "w") as file:
    file.write("admin,1234\njohn,password\n")

# 2. Accept input from user
username_input = input("Enter username: ").strip()
password_input = input("Enter password: ").strip()

# 3. Verify credentials against file data
login_successful = False

with open("users.txt", "r") as file:
    for line in file:
        if line.strip():
            stored_user, stored_pass = line.strip().split(",")
            if username_input == stored_user and password_input == stored_pass:
                login_successful = True
                break

# Display result
if login_successful:
    print("Login successful!")
else:
    print("Invalid username or password.") 