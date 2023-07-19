# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#print(f"The highest score in the class is: {max(student_scores)}")
'''
for i in range(len(student_scores) - 1):
    if student_scores[i] > student_scores[i+1]:
        print(student_scores[i])
    else:
        print(student_scores[i+1])
'''
heighest_score = 0
for score in student_scores:
    if score > heighest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
