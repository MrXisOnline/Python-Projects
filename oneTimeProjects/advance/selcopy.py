import os


def check_dir(file_path):
    if "." not in file_path:
        # print("True")
        return True


def check_all(dir_path):
    for file in os.listdir(dir_path):
        # print(file)
        if check_dir(file):
            n_path = os.path.join(dir_path, file)
            # print(file)
            check_all(n_path)
        elif file.endswith(".pdf") or file.endswith(".jpg"):
            file_paths.append(file)


file_paths = []
path = input("enter path : ")
check_all(path)
# print("OK")
for p in file_paths:
    print(p)
