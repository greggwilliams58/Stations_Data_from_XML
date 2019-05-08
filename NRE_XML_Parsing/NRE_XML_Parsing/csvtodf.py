import pandas as pd

def csvtodf(filepath,filename):
    df = pd.read_csv(filepath+filename, delimiter=',', encoding ='latin-1')
    return df
