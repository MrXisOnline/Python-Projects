import os
import shutil

os.chdir("C:\\Users\\SG704\\Desktop\\gaps")
file_paths = []
for file in os.listdir():
    print(file)
    file_paths.append(file)
for i in range(len(file_paths)):
    cur_file = os.path.join("C:\\Users\\SG704\\Desktop\\gaps", file_paths[i])
    # print(cur_file)
    cur_num = i+1
    if cur_num < 10:
        file_name = "spam00" + str(cur_num) + ".txt"
        cur_name = os.path.join("C:\\Users\\SG704\\Desktop\\gaps", file_paths[i])
        print(cur_name)
        sec_name = os.path.join("C:\\Users\\SG704\\Desktop\\gaps", file_name)
        print(sec_name)
        shutil.move(cur_name, sec_name)
    elif (cur_num >= 10) and (cur_num <= 99):
        file_name = "spam0" + str(cur_num) + ".txt"
        cur_name = os.path.join("C:\\Users\\SG704\\Desktop\\gaps", file_paths[i])
        print(cur_name)
        sec_name = os.path.join("C:\\Users\\SG704\\Desktop\\gaps", file_name)
        print(sec_name)
        shutil.move(cur_name, sec_name)

print("Succeed")
