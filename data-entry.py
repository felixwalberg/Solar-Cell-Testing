import pandas as pd 
import sqlite3 # included in standard python distribution
import os
import subprocess

# TODO: 
# Read parameters file back row-by-row and allow user to select which entries to add to dataverse
# Write to the csv and  add a column indicating which entries were actually added to dataverse
# Check for dataverse entries that are no longer supposed to be stored and remove them
# Avoid duplicates in the database
# Set up new table in dataverse



# Directory constants
DATA_DIRECTORY = '../Solar-Cell-Testing/data-1'
DATABASE = 'solar-cells.db'
TABLENAME = 'solar_cells'

# Iterate through directory and add all timeseries files to dataframe
cell_data_dataframe = pd.DataFrame()
for file in os.listdir(DATA_DIRECTORY):
    if file.startswith('pramod_') or file.startswith('seid_'):
        basetime = 0.0
        for file_in in os.listdir(DATA_DIRECTORY + "/" + file):
            basetime = 0.0
            if(os.path.isfile(DATA_DIRECTORY + "/" + file + "/" + "basetime.dat")):
                time_file = open(DATA_DIRECTORY + "/" + file + "/" + "basetime.dat", "r")
                basetime = time_file.readline()
            
            if(file_in.startswith('timeseries')) and not file_in.endswith("docx"):
                data = pd.read_csv(DATA_DIRECTORY + "/" + file + "/" + file_in)
                temp_df = pd.DataFrame(data)
                temp_df.insert(10, "Filename", file)
                temp_df.insert(11, "Time Base", basetime)
                cell_data_dataframe = pd.concat([cell_data_dataframe, temp_df])

#connect or create if doesn’t exist (same folder)
conn = sqlite3.connect(DATABASE)

cell_data_dataframe.rename(columns = {'Sample_Cell#':'Sample_Cell'}, inplace = True) 


# Call powershell script 
path = os.getcwd() + "/scripts/test3.ps1"
# path = "/Users/felixwalberg/UVM/UVM_Spring_2024/CatCoders\ Solar\ Cells\ Database/Solar-Cell-Testing/scripts/test3.ps1"

for index, row in cell_data_dataframe.iterrows():
    # Last column holds boolean for database insertion
    cli = f'pwsh -ExecutionPolicy Bypass -File "{path}" "{row[1]}" "{row[9]}" "{row[10]}"'
    print(cli)
    subprocess.run(cli, shell=True)





# Transfers dataframe to database
cell_data_dataframe.to_sql(name=TABLENAME, con=conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print(f"{len(cell_data_dataframe)} entries of sample data added to Solar Cell database")

# A file ends with .docx? Why is that different formatting? 