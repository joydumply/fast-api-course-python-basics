from grade_avg_service import calculate_homework

homework_assignment_grades = {
	'homework_1': 85,
	'homework_2': 100,
	'homework_3': 81
}


avg = calculate_homework(homework_assignment_grades)
print(avg)