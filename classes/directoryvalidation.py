import os 

class DirectoryValidation:
	def __init__(self):
		pass

	def validate_directory(self, directory_to_search):
		search_dir = os.path.relpath(directory_to_search)
		is_dir = os.path.exists(search_dir)

		if is_dir == False:
			return False

		return True
