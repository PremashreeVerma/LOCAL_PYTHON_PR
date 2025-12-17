import pandas as pd
from pathlib import Path

# Use file paths relative to this script so the script works
# whether run from workspace root or the Pandas_Prac folder.
BASE = Path(__file__).resolve().parent

try:
	dl = pd.read_csv(BASE / "Book_CSV.csv")
	ds = pd.read_json(BASE / "emp.json")
except Exception as e:
	print("Error reading data files:", e)
	raise

print("printed dl=csv")
print(dl)
print("printed ds=json")
print(ds)
print("pandas is successfully imported")