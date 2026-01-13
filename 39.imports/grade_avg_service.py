

def calculate_homework(args):
	grades_sum = 0
	for homework in args.values():
		grades_sum += homework
	return round(grades_sum / len(args), 2)
