class FileProcessing:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.opener = open

    def __enter__(self):
        self.handle = self.opener(self.path, self.mode)
        return self.handle

    def __exit__(self, exc_type, exc_value, tb):
        if exc_value:
            print('Something went wrong', exc_value)
        self.handle.close()
        del self.handle
        return True

    def read_file(self):
        file_content = self.handle.read()
        return file_content

    def write_to_file(self, any_text):
        file_content = self.handle.write(any_text)
        return file_content

    def clear_file_data(self):
        self.handle.truncate(0)


file_process = FileProcessing(path='dz_6.txt', mode='r')
with file_process as opener:
    print(file_process.read_file())

file_process2 = FileProcessing(path="dz_6.txt", mode='a')
with file_process2 as o:
    file_process2.write_to_file('I am learning python')
    file_process2.clear_file_data()
