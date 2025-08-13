import os

input_data = os.path.join(os.getcwd(), "data_input")
data_output = os.path.join(os.getcwd(), "data_output")

# Step 1: Check input folder, create if missing
if not os.path.exists(input_data):
    os.makedirs(input_data)
    print(f"Folder '{input_data}' created. Please add .txt files to it.")
    exit()

os.makedirs(data_output, exist_ok=True)

summary = []

for filename in os.listdir(input_data):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_data, filename)
        output_file_path = os.path.join(data_output, filename)

        modified_lines = []
        line_count = 0
        word_count = 0

        with open(input_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            if line.lstrip().startswith("#"):
                # Keep comment lines unchanged in output but do not count
                modified_lines.append(line)
                continue
            line_count += 1
            word_count += len(line.strip().split())
            modified_line = line.replace("temp", "permanent")
            modified_lines.append(modified_line)

        with open(output_file_path, "w", encoding="utf-8") as f:
            f.writelines(modified_lines)

        summary.append(f"{filename}\t{line_count}\t{word_count}\n")

summary_file_path = os.path.join(data_output, "summary.txt")
with open(summary_file_path, "w", encoding="utf-8") as f:
    f.write("Filename\tLineCount\tWordCount\n")
    f.writelines(summary)

print(f"Processing complete. Check '{data_output}' for results.")
