import os
from datetime import datetime

class ResultFileSetUp:
    def __init__(self):
        pass

    def check_results_dir_exists(self):
        dir_exists = os.path.exists("results")
        return dir_exists

    def make_results_dir(self):
        os.mkdir('results')

    def create_timestamped_results_file(self):
        date_now = datetime.now()
        results_file = f"results/results_{date_now.month}_{date_now.day}_{date_now.year}_{date_now.hour}:{date_now.minute}.{date_now.second}.txt"
        return results_file

    