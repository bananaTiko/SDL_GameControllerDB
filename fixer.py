# read the input file
with open("gamecontrollerdb.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []

for line in lines:
    line = line.rstrip("\n")  # remove newline

    # ignore comment lines
    if line.startswith("#") or line.strip() == "":
        output_lines.append(line)
        continue

    # find last comma
    if line.endswith(","):
        line = '"' + line[:-1] + '",'
    else:
        line = '"' + line + '"'

    output_lines.append(line)

# write back to file or a new file
with open("gamecontrollerdb_fixed.txt", "w", encoding="utf-8") as f:
    for line in output_lines:
        f.write(line + "\n")
