import os
import csv
import math
from collections import Counter  

Count = 0
Cand=[]
CountA = CountB = CountC = CountD = 0

PyPoll_csv = os.path.join("Tareas","Tarea 3 Python-Challenge","PyPoll","Resources","PyPoll_data.csv")

# with open (PyBank_csv) as csvfile:
#         csvreader = csv.reader(csvfile,delimiter=",")
#         print("Date: {0}".format(row[1]))

file = open(PyPoll_csv,newline='')
reader = csv.reader(file)

header = next(reader) #The first line is the header
for row in reader:
    Count = Count + 1
    a = row[2]
    b = row[2]
    if a not in Cand:
        Cand.append(a)
    Largo = len(Cand)

file = open(PyPoll_csv,newline='')
reader = csv.reader(file)

header = next(reader) #The first line is the header
for row in reader:
    b = row[2]
    if b == Cand[0]:
        CountA = CountA + 1
    if b == Cand[1]:
        CountB = CountB + 1
    if b == Cand[2]:
        CountC = CountC + 1
    if b == Cand[3]:
        CountD = CountD + 1

Votes = [CountA , CountB , CountC , CountD]
TotalVotes = CountA + CountB + CountC + CountD
PerA = "{:.2%}".format(CountA/TotalVotes)
PerB = "{:.2%}".format(CountB/TotalVotes)
PerC = "{:.2%}".format(CountC/TotalVotes)
PerD = "{:.2%}".format(CountD/TotalVotes)
Max = max(Votes)


print("Election Results")
print("----------------------")
print(f"Total Votes: {TotalVotes}")
print("----------------------")
print(f"{Cand[0]}: {PerA}  ({CountA})")
print(f"{Cand[1]}: {PerB}  ({CountB})")
print(f"{Cand[2]}: {PerC}  ({CountC})")
print(f"{Cand[3]}: {PerD}  ({CountD})")
print("----------------------")
print(f"Winner: {Cand[Votes.index(Max)]}")
print("----------------------")