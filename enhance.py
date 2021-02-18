import os
from emojipasta.emojify import emojify
data = {}

for root, dirs, files in os.walk('docs/pvme-guides'):
     for file in files:
        with open(os.path.join(root, file), "r", encoding='utf-8') as auto:
            data[os.path.join(root, file)] = auto.readlines()

for guide in data.values():
    for i, line in enumerate(guide):
        if "<" in line or ">" in line or line.startswith("*") or line == "":
            pass
        else:
            if line != "\n":
                guide[i] = emojify(line)
                print(guide[i])

for fpath, flines in data.items():
    with open(fpath, "w", encoding='utf-8') as file:
        file.writelines(flines)