import csv
import os

file_path = r'C:\Users\D SCIPHER\Downloads\Compressed\Facebook Page Data'

files = os.listdir(r"{}".format(file_path))
# print(files)

file_A = [i for i in files if files.index(i) % 2 == 0]
# print(file_A)
file_B = [i for i in files if files.index(i) % 2 != 0]
# print(file_B)

intersect_counter = 0
counter = 0
for i in range(int(len(files) / 2)):
    # print(i)
    with open(os.path.join(file_path, file_A[i]), 'r') as file_obj_A:
        file_data_A = csv.reader(file_obj_A)

        names_A = []
        for names_a in file_data_A:
            names_A.append(names_a[0])
        counter += len(names_A)

    with open(os.path.join(file_path, file_B[i]), 'r') as file_obj_B:
        file_data_B = csv.reader(file_obj_B)

        names_B = []
        for names_b in file_data_B:
            names_B.append(names_b[0])
        counter += len(names_B)

    with open(os.path.join(file_path, 'intersect.csv'), 'w') as file_obj_C:
        intersection = set(names_A).intersection(names_B)
        csv_writer = csv.writer(file_obj_C)
        for names in intersection:
            print(names)
            intersect_counter += 1
            csv_writer.writerow(names)

print(f"Total files parsed = {counter}")
print(f"Total intersect = {intersect_counter}")
