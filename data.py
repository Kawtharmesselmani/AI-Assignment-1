students = [
    {"name": "Lara",  "age": 23, "track": "AI",   "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar",  "age": 31, "track": "Data", "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim",   "age": 27, "track": "AI",   "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web",  "hours_studied": 8,  "scores": [50, 65, 40]},
    {"name": "Nour",  "age": 25, "track": "AI",   "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami",  "age": 35, "track": "Data", "hours_studied": 48, "scores": [88, 91, 79]},
]
# Part 1
# 1
print(students[0]["name"])
print(students[-1]["name"])

# 2
print(students[2]["scores"])

# 3
for student in students:
    print(f"{student['name']} is {student['age']} years old and studies {student['track']}.")
   
# Part 2:
# 4
ai_students = []

for student in students:
    if student["track"] == "AI":
        ai_students.append(student)

print(len(ai_students))

# 5

ai_students = [student for student in students if student["track"] == "AI"]

print(len(ai_students))

# 6

students_names = []
for student in students:
    if (student["hours_studied"] > 30):
        students_names.append(student["name"])  
        print(students_names)
    
# 7
older_students = []
for student in students:
    if student["age"] > 24 and student["track"] == "AI":
        older_students.append(student)
        print(older_students)
        
# Part 3
#8
average_age = sum(student["age"] for student in students) / len(students)
print(average_age)

# 9
total_hours_studied = sum(student["hours_studied"] for student in students)
print(total_hours_studied)

# 10
for student in students:
    if student["hours_studied"] == max(student["hours_studied"] for student in students):
        most_hours_student = student
        print(most_hours_student)
        break
print(most_hours_student["name"], most_hours_student["hours_studied"])

# 11
for student in students:
    final_grade = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {final_grade:.1f}")
    
# Part 4:

#12:
list_dictionary = []

for student in students:
    final_grade = sum(student["scores"]) / len(student["scores"])

    student_dict = {
        "name": student["name"],
        "final_grade": final_grade
    }

    list_dictionary.append(student_dict)

print(list_dictionary)

#13:
track_counts = {}

for student in students:
    track = student["track"]

    if track in track_counts:
        track_counts[track] += 1
    else:
        track_counts[track] = 1

print(track_counts)

#14:
# A set is the right tool because it stores only unique values and automatically removes duplicates.
unique_tracks = {student["track"] for student in students}

print(unique_tracks)

# Part 5:
# 15


def filter_by_track(students, track):
    return [student for student in students if student["track"] == track]


print(filter_by_track(students, "AI"))

print(filter_by_track(students, "Data"))


# 16
def average_score(student):
    return sum(student["scores"]) / len(student["scores"])


# Test with Lara
print(average_score(students[0]))

# Test with Rim
print(average_score(students[2]))


# 17

def top_student(students):
    best_student = max(students, key=average_score)
    return best_student["name"]


# Test
print(top_student(students))


# 18

def summary(students):
    return {
        "total_students": len(students),
        "average_age": sum(student["age"] for student in students) / len(students),
        "tracks": {student["track"] for student in students}
    }


# Test
print(summary(students))


# 19
def average_score(student):
    return sum(student["scores"]) / len(student["scores"])


def report(students, min_hours):
    filtered_students = [
        {
            "name": student["name"],
            "average_score": average_score(student)
        }
        for student in students
        if student["hours_studied"] >= min_hours
    ]

    return sorted(
        filtered_students,
        key=lambda student: student["average_score"],
        reverse=True
    )


# Test with 30 hours
print(report(students, 30))