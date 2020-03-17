import csv
import os

# specify the folder for the CSV files
file_path = r'C:\Users\D SCIPHER\Downloads\Compressed\Facebook Page Data'

# declared a variable 'files' to contain all the individual csv file in the file_path
files = os.listdir(r"{}".format(file_path))
# print(files)

# a variable to hold files which index number are even i.e 0,2,4...
file_A = [i for i in files if files.index(i) % 2 == 0]
# print(file_A)
# a variable to hold files which index number are odd i.e 1,3,5...
file_B = [i for i in files if files.index(i) % 2 != 0]
# print(file_B)

# a variable to hold the total count of common column fields(name) in the csv file
intersect_counter = 0
# a variable to hold the total count of all parsed columns in the two csv files.
counter = 0

# take the files in file_A and file_B one by one, and simultaneously
for i in range(int(len(files) / 2)):
    # print(i)
    # open and read the files in file_A through the csv module
    with open(os.path.join(file_path, file_A[i]), 'r') as file_obj_A:
        file_data_A = csv.reader(file_obj_A)

        # a variable to hold the names
        names_A = []
        # parse the file row by row, and append name, which correspond to the index no. 0 in a row.
        for names_a in file_data_A:
            names_A.append(names_a[0])
        # update the counter
        counter += len(names_A)
    # open and read the files in file_B through the csv module
    with open(os.path.join(file_path, file_B[i]), 'r') as file_obj_B:
        file_data_B = csv.reader(file_obj_B)

        # a variable to hold the names
        names_B = []
        # parse the file row by row, and append name, which correspond to the index no. 0 in a row.
        for names_b in file_data_B:
            names_B.append(names_b[0])
        # update the counter
        counter += len(names_B)

    # create a csv file to save the common names from the two files
    with open(os.path.join(file_path, 'intersect.csv'), 'w') as file_obj_C:
        # use the set method to get the names which appear in both names_A and names_B
        intersection = set(names_A).intersection(names_B)
        csv_writer = csv.writer(file_obj_C)
        for names in intersection:
            print(names)
            intersect_counter += 1
            csv_writer.writerow(names)

print(f"Total files parsed = {counter}")
print(f"Total intersect = {intersect_counter}")
