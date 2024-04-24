import os
import subprocess
import pandas as pd

# Replace with file path to timeseries parameters folder
CSV_FILE = "../Solar-Cell-Testing/data-1/pramod_020624/timeseries_parameters_020624"

# Store the contents of the csv file in a dataframe
data = pd.read_csv(CSV_FILE)
cell_data_dataframe = pd.DataFrame(data)

# Call powershell script and pass the values from the chosen entry
path = os.getcwd() + "/scripts/insert-data.ps1"
search_path = os.getcwd() + "/scripts/check-existence.ps1"

for index, row in cell_data_dataframe.iterrows():
    # When new questions are added to the form, there needs to be another argument passed to the script
    cli1 = f'pwsh -ExecutionPolicy Bypass -File "{search_path}" "{row[1]}" cr69a_sampledatas '
    subprocess.run(cli1, shell=True)
    # cli = f'pwsh -ExecutionPolicy Bypass -File "{path}" "{row[0]}" "{row[1]}" "{row[2]}" "{row[3]}" "{row[4]}" "{row[5]}" "{row[6]}" "{row[7]}" "{row[8]}" "{row[9]}" '
    # subprocess.run(cli, shell=True)