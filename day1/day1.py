
file = open("input.txt", "r")

lines = file.readlines()
file.close()

first_list = []
second_list = []


for line in lines:
    first_list.append(int(line.split("   ")[0]))
    second_list.append(int(line.split("   ")[1].strip()))
    
sorted_first_list = sorted(first_list)
sorted_second_list = sorted(second_list)

distance = 0
for i in range(len(sorted_first_list)):
    distance = distance + abs(sorted_first_list[i] - sorted_second_list[i])

print(distance)    

total = 0
for number in sorted_first_list:
    times_number_appears = sorted_second_list.count(number)
    total = total + (number * times_number_appears)

print(total)