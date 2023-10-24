import pandas as pd
from scidownl import scihub_download

df = pd.read_csv("your_csv_file.csv")  # Replace with the actual CSV file path

for doi in df["DOI"]:
    name = './paper/' + doi + '.pdf'
    
    try:
        scihub_download('https://doi.org/' + doi, paper_type='doi', out=name)
        print(f"Downloaded {doi}")
    except Exception as e:
        error_message = f"Error downloading {doi}: {str(e)}"
        print(error_message)
        
        # Log the error to a file
        with open('error_log.txt', 'a') as log_file:
            log_file.write(error_message + '\n')
