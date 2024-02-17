class ReadFile:
    def __init__(self, filename):
        self._filename = filename

    def read_file(self):
        print("--- Reading the file ---")
        with open(self._filename, "r") as infile:
            file_content = infile.readlines()
        it_obj = iter(file_content)
        try:
            while it_obj:
                print(next(it_obj).replace("\n", ""))
        except StopIteration:
            print("--- Reached end ---")
        finally:
            pass


rf = ReadFile("db.txt")
rf.read_file()
