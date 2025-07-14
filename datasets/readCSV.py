import pandas as pd

# Try reading CSV with utf-8
try:
    df = pd.read_csv('Food_Additives_Regulations.camelot.csv', encoding='utf-8')
except UnicodeDecodeError:
    # If utf-8 fails, try ISO-8859-1 (Latin-1)
    df = pd.read_csv('Food_Additives_Regulations.camelot.csv', encoding='ISO-8859-1')

# Print the first 5 rows
print(df.head())
