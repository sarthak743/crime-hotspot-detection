import csv
from pathlib import Path

dataset_path = Path("LAPD_NIBRS_Offenses_Dataset_20261022.csv")

with dataset_path.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)

    columns = next(reader)
    sample_rows = [next(reader) for _ in range(5)]

print(f"Dataset: {dataset_path.name}")
print(f"Columns: {len(columns)}")
print("\nColumn names:")

for column in columns:
    print(f"- {column}")

print("\nFirst 5 records:")
for row in sample_rows:
    print(row)
