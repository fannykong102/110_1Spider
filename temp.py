import requests

r = requests.get("https://cloud.hakka.gov.tw/Pub/Opendata/DTST20171100025.json")
list_data = r.json()["NewDataSet"]["Table"]

fp= open("data_20211021.csv", "w")

head = ""
for key in list_data[0]:
    head = head + str(key) + ","
fp.write(head)

for i in list_data:
    data = ""
    for key in i:
        data += str(i[key]) + ","
    data += "\n"
    fp.write(data)
        

fp.close()
    
