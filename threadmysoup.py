from run import run

def print_arguments_incorrect_message():
	print("Please run 'python3 threadmysoup.py' + 1 argument:")
	print("'python3 threadmysoup.py p' to get paragraphs")
	print("'python3 threadmysoup.py a' to get links")

if __name__ == "__main__":
	import sys

	accepted_arguments = ['p', 'a']

	### sys.argv is a list of params passed by user 'python3 threadmysoup.py p' etc.
	### 1st item is always file name --> ['threadmysoup.py'...other args...]
	number_arguments = len(sys.argv)

	if number_arguments == 1:
		print("One argument required")
		print_arguments_incorrect_message()
		quit()

	if number_arguments > 2:
		print("Too many arguments")
		print_arguments_incorrect_message()
		quit()

	if number_arguments == 2:
		if sys.argv[1] in accepted_arguments:
			### proceed with program
			run(sys.argv[1])
		else:
			print("Incorrect argument entered")