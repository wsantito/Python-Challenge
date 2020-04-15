import os
import csv
import operator

Cand = []
MyDict = {}
C = Count = 0

PyPoll_csv = os.path.join("Tareas","Tarea 3 Python-Challenge","PyPoll","Resources","PyPoll_data.csv")

file = open(PyPoll_csv,newline='')
reader = csv.reader(file)

header = next(reader) #The first line is the header
for row in reader:
    Count = Count + 1
    a = row[2]
    if a not in MyDict:
        MyDict[a]=1
        C = C + 1
        if a not in Cand:
            Cand.append(a)

    if a in MyDict:
        MyDict[a] = MyDict[a] + 1
        
TotalVotes = sum(MyDict.values()) 
H = len(MyDict)
Max = max(MyDict.items(), key=operator.itemgetter(1))[0]

i = -1
for value in MyDict.values():
    i = i + 1
    if i < H:
        globals()['MyPer{}'.format(i)] = "{:.2%}".format(value/TotalVotes)

print("Election Results")
print("----------------------")
print("Total Votes: {:,.0f}".format(TotalVotes))
print("----------------------")
i=-1
for value in MyDict.values():
    i = i + 1
    if i < H:
        K = MyDict[Cand[i]]
        print(f"{Cand[i]}: {globals()['MyPer{}'.format(i)]}" " ({:,.0f})".format(K))
        globals()['MyPer{}'.format(i)] = "{:.2%}".format(value/TotalVotes)
print("----------------------")
print(f"Winner: {Max}")
print("----------------------")