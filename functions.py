def find_largest(number):
    if not number :
        return None
    # assume the first number is the largest number
    largest = number[0]
    for num in number:
        if num > largest :
            largest = num
    return largest 
number =[4,7,2,90,11]
print (find_largest(number))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text :
        if char in vowels :
            count += 1
            return count
print(count_vowels ("proggramming"))

def highest_scorer (scores_dict):
            if not scores_dict:
                return None
            highest_score = None 
            highest_score = -float("inf")
            for student ,score in scores_dict.items():
                if score > highest_score:
                    highest_score = score
                    highest_student = student
                    return highest_student
                print((highest_student))







            

    

    
    