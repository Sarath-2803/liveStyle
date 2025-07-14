import pandas as pd

# Try common delimiters like ',', ';', '\t', '|'
with open('GAZETTEammendments.csv', 'r', encoding='utf-8') as f:
    sample = f.read(1024)
    print(repr(sample))  # print raw characters to look for weird symbols
