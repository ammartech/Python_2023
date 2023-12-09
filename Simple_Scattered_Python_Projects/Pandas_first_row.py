import pandas as pd

# Step 1: Install Pandas (if not already installed)
# You can skip this step if you have Pandas installed.

# Step 2: Import Pandas
# Pandas should be imported at the beginning of your script.

# Step 3: Read the Excel File
file_path = 'A_p.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Step 4: Access and Print the Header Using a For Loop
header = df.columns

for column_name in header:
    print(column_name)  # This assumes the header contains Arabic text

