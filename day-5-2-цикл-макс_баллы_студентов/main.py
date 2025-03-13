# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#highest_score = int(student_scores[0])

# highest_score = int(student_scores[0])

# for i in range(len(student_scores)):
#     for j in range(i + 1, len(student_scores)):
#         if student_scores[i] < student_scores[j]:
#           # print ("+")
#           if highest_score < student_scores[j]:
#             highest_score = student_scores[j]
        
           
# print("The highest score in the class is: ", highest_score)

highest_score = 0
for score in student_scores:
  if score > highest_score:
      highest_score = score
print("The highest score in the class is: ", highest_score)
