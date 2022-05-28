# ******** SEMANA 6 ***********
#Created on Tue May 27 11:50:22 2022  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS

# importe estos 3 módulos, ya están instalados en colab
import requests
import io
import pandas as pd 

url = "https://raw.githubusercontent.com/RODRIGOGALLEGO2463/mintic/main/CUPSs.csv"
download = requests.get(url).content
data = pd.read_table(io.StringIO(download.decode(encoding="ascii", errors="ignore")) ,sep=';') # En algunos casos es importante codificarlo en utf-8
print(data.head()) #display(data)
print(data)