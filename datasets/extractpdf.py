import pdfplumber
import pandas as pd

pdf_path = "./fssai/2/GAZETTEammendments.pdf"  # Update path if needed

all_tables = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:
                # Fix: ensure column headers are unique
                headers = table[0]
                seen = {}
                unique_headers = []
                for h in headers:
                    if h in seen:
                        seen[h] += 1
                        unique_headers.append(f"{h}_{seen[h]}")
                    else:
                        seen[h] = 1
                        unique_headers.append(h)

                df = pd.DataFrame(table[1:], columns=unique_headers)
                all_tables.append(df)

# Merge all dataframes
final_df = pd.concat(all_tables, ignore_index=True)

# Save
final_df.to_csv("GAZETTEammendments.csv", index=False)
print("✅ Dataset created successfully!")
