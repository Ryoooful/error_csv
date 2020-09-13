import pandas as pd

filepath = r"C:\Users\Ryoooful\OneDrive\Desktop\Book1.csv"
filepath2 = r"C:\Users\Ryoooful\OneDrive\Desktop\Book2.csv"
abaqus = {"ta":{"aaa":[], "bbb":[], "ccc":[], "ddd":[]}}
lines = []
with open(filepath) as f:
    lines += [s.strip() for s in  f.readlines()]

with open(filepath2) as f:
    lines += [s.strip() for s in  f.readlines()]

n = 0
for line in lines:
    spdata = [s.strip() for s in line.split(",")]
    if spdata[0] == "aaa":
        n = 0
    elif spdata[1] != "":
        abaqus["ta"]["aaa"] += [spdata[0]]
        abaqus["ta"]["bbb"] += [spdata[1]]
        abaqus["ta"]["ccc"] += [abs((float(spdata[0]) - float(spdata[1])) / float(spdata[0]))]
        abaqus["ta"]["ddd"] += [n + 1]
        n = 0
    else:
        n = n + 1

df = pd.DataFrame(data=abaqus["ta"], columns=abaqus["ta"].keys())


sdf = df.drop("aaa",axis=1).drop("bbb",axis=1).describe()
s = df.agg(["var"])

koko = pd.concat([sdf, s], axis=0)

koko.to_csv(r"C:\Users\Ryoooful\OneDrive\Desktop\koko.csv")
