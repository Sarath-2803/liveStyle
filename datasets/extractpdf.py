import camelot
import pandas as pd

pdf_path = "./fssai/2/GAZETTEammendments.pdf"  # Path to your PDF

# Try both 'stream' and 'lattice' and see which works better
tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')  # or flavor='lattice'

all_tables = [t.df for t in tables]  # List of DataFrames

# Merge all dataframes
final_df = pd.concat(all_tables, ignore_index=True)

# Save to CSV and JSON
final_df.to_csv("Food_Additives_Regulations.camelot.csv", index=False)
final_df.to_json("Food_Additives_Regulations.camelot.json", orient='records', lines=False)

print("✅ Camelot dataset created successfully!")
