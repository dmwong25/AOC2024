with open("day1/day1_input.txt", "r") as file:
  input_data = file.readlines()
  
# columns to lists
a = []
b = []
for line in input_data:
  a.append(int(line.split()[0].strip()))
  b.append(int(line.split()[1].strip()))
  
a.sort()
b.sort()
sum = 0
for i in range(len(a)):
    sum = sum + abs(a[i] - b[i])

print(sum)