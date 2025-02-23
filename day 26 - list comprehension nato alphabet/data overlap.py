with open("file1.txt") as file:
    file1contents = file.readlines()
    file1contents = [line.replace("\n", "") for line in file1contents]


with open("file2.txt") as file:
    file2contents = file.readlines()
    file2contents = [line.replace("\n", "") for line in file2contents]



result = [int(idx) for idx in file1contents if idx in file2contents] #new_list = [new_item for item in list if test]
#checks if in file2
#goes thru all of file1 then returns value?
#returns empty if file2 is not in file1
print(result)

#Result should be [3, 6, 5, 33, 12, 7, 42, 13]

# file1contents = ['3', '6', '5', '8', '33', '12', '7', '4', '72', '2', '42', '13']
# file2contents = ['3', '6', '13', '5', '7', '89', '12', '3', '33', '34', '1', '344', '42']

# result = [[idx for idx in file1contents if idx == c] for c in file2contents] #new_list = [new_item for item in list if test]

# print(result)