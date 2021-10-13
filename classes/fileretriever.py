import os

class FileRetriever:
    def __init__(self):
        pass

    def retrieve_files_from_dir(self, directory_to_search):
        retrieved_files = []

        try:
            search_dir = os.path.relpath(directory_to_search)

            for main_dir, sub_dir, files in os.walk(search_dir):
                for file in files:
                    try:
                        name, extension = os.path.splitext(file)
                        if extension == ".html":
                            file_address = f"{main_dir}/{file}"
                            # print(file_address)
                            retrieved_files.append(file_address)
                    except:
                        pass
        except:
            return None

        return retrieved_files
