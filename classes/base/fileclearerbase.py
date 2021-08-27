class FileClearerBase:
    def __init__(self):
        pass

    def clear_results_file(self, results_file_name):
        with open(results_file_name, "w") as file:
            file.write("")

    def clear_temp_file(self, temp_file_name):
        with open(temp_file_name, "w") as file:
            file.write("")