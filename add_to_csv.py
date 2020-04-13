import re
import pandas as pd

sections = ["AYI", "AYJ"]
labs = ["lab05", "lab06", "lab07", "lab08"]

# participation based labs (these come later on in the semester)
part_based = []    

pattern = re.compile("^([a-zA-Z0-9]+)(\s+)(\d+\.\d+)")
for section in sections:
    for labnum in labs:
        score_map = {}
        with open(f"{section}_{labnum}.out") as f:
            data = f.readlines()
            for line in data:
                if pattern.match(line):
                    netid, score = tuple(line.split())
                    score = float(score)
                    if labnum in part_based:
                        score = 2.0
                    score_map[netid] = score
            data = pd.read_csv(f"{section}_grades.csv")
            for netid, score in score_map.items():
                data.loc[data['Username'] == netid, f"{labnum}_lab"] = score
            data.to_csv(f"{section}_grades.csv", index=False)