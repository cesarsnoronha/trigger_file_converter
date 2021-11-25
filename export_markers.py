import pandas as pd

# Adjust here
filename = 'Desktop/NIRS_triggers/2021-11-12_001_lsl.tri'
interval = 3
condition = 2
outname = 'out.txt'

# Reading all data
df = pd.read_csv(filename, header=None, delimiter=';')

df_filtered = df[df[2] == condition] # Filter rows of an certain condition
sel_rows = list(range(0, len(df_filtered), interval)) # Selected rows
df_filtered.reset_index(inplace=True)
final_markers = df_filtered.loc[sel_rows]

with open(outname, 'w') as f:
    for idx, row in final_markers.iterrows():
        bin_cond = format(row[2], '#010b').replace('0b', '') # Generate bin
        line = [row[1]+1] + list(bin_cond[::-1]) # Generate line to put in outfile
        print(line)
        f.write('\t'.join(str(x) for x in line) + '\n')

