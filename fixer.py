input_file = "gamecontrollerdb.txt"
output_file = "gamecontrollerdb_fixed.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []

for line in lines:
    line = line.rstrip("\n")

    # Ignore comments or empty lines
    if line.startswith("#") or line.strip() == "":
        output_lines.append(line)
        continue

    # Wrap in quotes before the last comma
    if line.endswith(","):
        line = f'"{line[:-1]}",'
    else:
        line = f'"{line}"'

    # Add 3 tabs at the start
    line = "\t\t\t" + line
    output_lines.append(line)

with open(output_file, "w", encoding="utf-8") as f:
    for line in output_lines:
        f.write(line + "\n")
