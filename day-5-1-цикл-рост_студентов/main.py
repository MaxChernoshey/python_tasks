
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  n = n + 1
print("Рост студентов :", student_heights)
print("Кол-во студентов :" , n)

sum = 0
for k in student_heights:
    sum = sum + k
t = round(sum/n)
print("Средний рост :", t)

 
  