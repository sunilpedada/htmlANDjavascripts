import requests
import json
import pandas
data=requests.get("https://opentdb.com/api.php?amount=1")
json_data=data.json()
dict_data=dict(json_data)
print(dict_data)
sets=dict_data["results"][0]
detais=[]
for hadings in sets:
    detais.append([hadings,sets[hadings]])
pandpro=pandas.DataFrame(detais,index=None,columns=["key","value"])
pandpro.to_excel("details.xlsx")
