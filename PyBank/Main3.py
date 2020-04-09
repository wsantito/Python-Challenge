import os
import csv
import math
from datetime import datetime   

Count = 0
Suma = 0
Avg = 0
data=[]
Row1 = 0

PyBank_csv = os.path.join("Tareas","Tarea 3 Python-Challenge","PyBank","Resources","PyBank_data.csv")

# with open (PyBank_csv) as csvfile:
#         csvreader = csv.reader(csvfile,delimiter=",")
#         print("Date: {0}".format(row[1]))

file = open(PyBank_csv,newline='')
reader = csv.reader(file)

header = next(reader) #The first line is the header
for row in reader:
    Count = Count + 1
    Suma = Suma + int(row[1])
    RowA = int(row[1])
    RowN = 0
    if Count == 1:
        FMax = row[0]
        Max = 0
        Min = 0
        Row1 = int(row[1])
    else:
        RowAdd = (RowA - Row1)
        data.append(RowAdd)
    if RowA >= 0 and Row1 >= 0:
        if RowA > Row1 and (RowA - Row1) > Max:
            FMax = row[0]
            Max = RowA - Row1
            # print(Row1)
            # Row1 = RowA
        elif RowA < Row1 and (RowA - Row1) < Min:
            FMin = row[0]
            Min = RowA - Row1
            # print(Row1)
            # Row1 = RowA
        # else:
        #     Row1 = RowA
        

    if RowA >= 0 and Row1 < 0:
        if (RowA - Row1) > Max:
            FMax = row[0]
            Max = RowA - Row1
            # print(Row1)
            # Row1 = RowA
        elif (RowA - Row1) < Min:
            FMin = row[0]
            Min = RowA - Row1
            # print(Row1)
        #     Row1 = RowA
        # else:
        #     Row1 = RowA

    if RowA < 0 and Row1 < 0:
        if (RowA - Row1) > Max:
            FMax = row[0]
            Max = RowA - Row1
            # print(Row1)
            # Row1 = RowA
        elif (RowA - Row1) < Min:
            FMin = row[0]
            Min = RowA - Row1
            # print(Row1)
            # Row1 = RowA
        # else:
        #     Row1 = RowA


    if RowA < 0 and Row1 >= 0:
        if (RowA - Row1) > Max:
            FMax = row[0]
            Max = RowA - Row1
            # print(Row1)
            # Row1 = RowA
        elif (RowA - Row1) < Min:
            FMin = row[0]
            Min = RowA - Row1
            # print(Row1)
        #     Row1 = RowA
        # else:
        #     Row1 = RowA
    Row1 = RowA

Avg = sum(data)/len(data)
RSuma = "${:,.2f}".format(Suma)
RAvg ="${:,.2f}".format(Avg)
RMax = "${:,.2f}".format(Max)
RMin = "${:,.2f}".format(Min)

print(f"Total Months: {Count}")
print(f"Total: {RSuma}")
print(f"Average Change: {RAvg}")
print(f"Greatest Increase in Profits: {FMax}  {RMax}")
print(f"Greatest Decrease in Profits: {FMin}  {RMin}")

# print(data)

