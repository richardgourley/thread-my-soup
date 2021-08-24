from threading import Thread, Lock

class ThreadingBase:
    def __init__(self):
        self.lock = Lock()

    def start_threads(self, func, urls_or_files):
        threads = [Thread(target=func, args=(item,)) for item in urls_or_files]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()