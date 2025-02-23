student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#looping through dicts
for (key, value) in student_dict.items():
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through data frame
for (key, value) in student_data_frame.items():
    print(key)
    #titles each column
    print(value)
    #data each of columns
#LOOP THROUGH ROWS OF DATAFRAME
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)