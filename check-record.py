import os
import subprocess


search_path = os.getcwd() + "/scripts/check-existence.ps1"

sample_id = input(str("Enter the sample id you wish to add data for: "))

valid_tables = ["cr69a_pets", "cr69a_sampledatas"]
for num, table in zip(range(0,len(valid_tables)),valid_tables):
    print(str(num) + ' ' + table)

table_name = int(input("Enter the index for the table name you are accessing: "))

while(table_name < 0 or table_name >= len(valid_tables)):
    print("Invalid index, select one of the listed options")
    for num, table in zip(range(0,len(valid_tables)),valid_tables):
        print(str(num) + ' ' + table)
    table_name = int(input("Enter the index for the table name you are accessing: "))


cli1 = f'pwsh -ExecutionPolicy Bypass -File "{search_path}" "{sample_id}" {valid_tables[table_name]} '
result = subprocess.run(cli1, shell=True, capture_output=True, text=True)

allow_entry = False
result = result.stdout.strip()
confirmation = ''
while(not allow_entry):
    # Check if entry was not found
    if(result == "Invalid"):
        print(f"Sample {sample_id} was not found in table {table_name}, please enter a new sample or enter the metadata first.")
        sample_id = input(str("Enter the sample id you wish to add data for: "))
        for num, table in zip(range(0,len(valid_tables)),valid_tables):
            print(str(num) + ' ' + table)
        table_name = int(input("Enter the index for the table name you are accessing: "))
    else:
        print(result)
        confirmation = input(str("Y/N: "))
        if(confirmation.upper() == "Y"):
            print(f"Calling insertion script with {sample_id} sample")
            allow_entry = True
        else:
            sample_id = input(str("Enter the sample id you wish to add data for: "))
            for num, table in zip(range(0,len(valid_tables)),valid_tables):
                print(str(num) + ' ' + table)
            table_name = int(input("Enter the index for the table name you are accessing: "))
    cli1 = f'pwsh -ExecutionPolicy Bypass -File "{search_path}" "{sample_id}" {valid_tables[table_name]} '
    result = subprocess.run(cli1, shell=True, capture_output=True, text=True)
    result = result.stdout.strip()

if(allow_entry):
    print("This is where you would call the other script within the Jupyter Notebook")



