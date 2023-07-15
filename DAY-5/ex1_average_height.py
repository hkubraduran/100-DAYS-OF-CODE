# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_heights = 0
count = 0
for i in student_heights:
    count+=1
#for j in student_heights:
    #total_heights += j
for j in range(0, count):
    total_heights += student_heights[j]
avg = round(total_heights / count)
print(avg)


