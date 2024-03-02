import pandas as pd 
import sqlite3 # included in standard python distribution
import os

# Directory constants
DATA_DIRECTORY = '../Solar-Cell-Testing/data-1'
DATABASE = 'solar-cells.db'

# Iterate through directory and add all timeseries files to dataframe
cell_data_dataframe = pd.DataFrame()
for file in os.listdir(DATA_DIRECTORY):
    if file.startswith('pramod') or file.startswith('seid'):
        for file_in in os.listdir(DATA_DIRECTORY + "/" + file):
            if(file_in.startswith('timeseries')) and not file_in.endswith("docx"):
                data = pd.read_csv(DATA_DIRECTORY + "/" + file + "/" + file_in)
                temp_df = pd.DataFrame(data)
                cell_data_dataframe = pd.concat([cell_data_dataframe, temp_df])

#connect or create if doesn’t exist (same folder)
conn = sqlite3.connect(DATABASE)

# Transfers dataframe to database
cell_data_dataframe.to_sql(name=DATABASE, con=conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print(f"{len(cell_data_dataframe)} entries of sample data added to Solar Cell database")



# A file ends with .docx? Why is that different formatting? 