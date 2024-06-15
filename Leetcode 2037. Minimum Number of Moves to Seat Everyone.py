seats1    = [3,1,5,100]
students1 = [2,7,4,99]
seats2    = [2,2,6,6]
students2 = [1,3,2,6]

def minMovesToSeat(seats, students):
    res = 0
    seats_counter    = [0] * 101
    students_counter = [0] * 101
    for i in range(len(seats)):
        seats_counter[seats[i]]       += 1
        students_counter[students[i]] += 1
    
    seats    = []
    students = []
    for i in range(len(seats_counter)):
        for _ in range(seats_counter[i]):
            seats.append(i)
        for _ in range(students_counter[i]):
            students.append(i)

    for i in range(len(seats)):
        res += abs(seats[i] - students[i])
    return res

def minMovesToSeatSort(seats, students):
    res = 0
    seats, students = sorted(seats), sorted(students)
    for i in range(len(seats)):
        res +=abs(seats[i] - students[i])
    return res

def minMovesToSeatOptimized(seats, students):
    res, seats_counter, students_counter = 0, [0] * 101, [0] * 101
    for i in range(len(seats)):
        seats_counter[seats[i]]       += 1
        students_counter[students[i]] += 1
    
    seats_index, students_index, seated = 0, 0, len(students)
    for _ in range(len(seats)):
        while not seats_counter[seats_index]:
            seats_index += 1
        while not students_counter[students_index]:
            students_index += 1
        while seats_counter[seats_index] and students_counter[students_index]:
            res += abs(seats_index - students_index)
            seats_counter[seats_index] -= 1
            students_counter[students_index] -=1
            seated -= 1
            if seated == 0:
                return res
        

print(minMovesToSeat(seats1, students1))
print(minMovesToSeatSort(seats1, students1))
print(minMovesToSeatOptimized(seats1, students1))