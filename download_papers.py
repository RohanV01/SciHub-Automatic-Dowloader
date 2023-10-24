import pandas as pd
from scidownl import scihub_download

df = pd.read_csv("")

for doi in df["DOI"]:
    name='./paper/'+doi+'.pdf'
    scihub_download('https://doi.org/'+doi, paper_type='doi', out=name)