# def read_file(filename):
#     with open(filename, "r") as infile:
#         contents = infile.read()
#     print(contents)

def read_file(filename):
    with open(filename, "r") as infile:
        contents = infile.read()
        print(infile.tell())
    print(contents)


read_file("db.txt")
