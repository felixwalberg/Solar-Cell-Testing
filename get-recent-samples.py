import os
import subprocess
import pandas as pd

# This formatting is to display all the columns, otherwise pandas limits the ones displayed
# pd.set_option('display.max_columns', None)

# The table name value should reflect the variable created when the user starts the Jupyter Notebook
search_path = os.getcwd() + "/scripts/recent-entries.ps1"
table_name = 'cr69a_sampledatav2s'

# This variable determines how many of the samples are returned
num_samples = 3

# Execute the PowerShell script as a subprocess, passing the table name, which returns the num_samples most recent values.
cli1 = f'pwsh -ExecutionPolicy Bypass -File "{search_path}" "{table_name}" {num_samples}'
result = subprocess.run(cli1, shell=True, capture_output=True, text=True)

# String manipulation on the results
result = result.stdout.strip()
result = result.splitlines()
for string, index in zip(result, range(0,len(result))):
    result[index] = string.split(',')

# Create dataframe and display results
recent_values = pd.DataFrame(columns=result[0])

for row in range(1, len(result)):
    recent_values = recent_values._append(pd.Series((result[row]), index=recent_values.columns), ignore_index=True)

# The results are displayed in the order of most recently entered according to cr69a_entry_date_and_time
print(recent_values)

# Turn sample names into a list for the form
samples = recent_values['Sample ID'].tolist()


