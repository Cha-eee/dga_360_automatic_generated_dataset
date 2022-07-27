import csv
import datetime
import pandas as pd
import os

yesterday = datetime.datetime.now() + datetime.timedelta(-1)
date = yesterday.strftime('%x')
date = date.replace('/', '-')

#更改前一天数据名称

path = 'D:/Projects/Improving-dga-based-malicious-domain-classifiers-with-natural-language-procesing-master/'
name_dga = str(path) +'dga.csv'
new_name_dga = str(path) + 'dga' + str(date) + '.csv'
if os.path.exists(name_dga):
    os.rename(name_dga, new_name_dga)

path_dataset = 'D:/Projects/Improving-dga-based-malicious-domain-classifiers-with-natural-language-procesing-master/dataset/'
name_families = str(path_dataset) + 'DGA-families'
new_name_families = new_name_dga = str(path_dataset) + 'DGA-families' + str(date)
if os.path.exists(name_families):
    os.rename(name_families, new_name_families)

#txt转换成csv

csvFile = open("./dga.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("dga.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

#csv文件内容格式转换

data = pd.read_csv("./dga.csv", header=None, names=["family", "domain", "date0", "time0", "date1", "time1"])
data = data.drop(columns='date0')
data = data.drop(columns='time0')
data = data.drop(columns='date1')
data = data.drop(columns='time1')
data = data.drop(data.index[0:17], inplace=False)
data = data.to_csv("./dga.csv", index=None)
data = pd.read_csv("./dga.csv", header=None,
                   names=["family", "domain", "VT_scan", "isNXDomain", "perNumChars", "VtoC", "lenDomain", "SymToChar",
                          "TLD", "family_id", "class"])
data = data.drop(data.index[0], inplace=False)
lendomain = []
tld = []
Class = []
for index, row in data.iterrows():
    lendomain.append(len(row['domain']))
    tld.append(row['domain'].split(".")[1])
    Class.append(1)
data['lenDomain'] = lendomain
data['TLD'] = tld
data['class'] = Class
family_dict = {"abcbot": 1, "antavmu": 2, "bamital": 3, "banjori": 4, "bigviktor": 5, "blackhole": 6, "ccleaner": 7, "chinad": 8, "conficker": 9,
               "copperstealer": 10, "cryptolocker": 11, "dircrypt": 12, "dmsniff": 13, "dyre": 14, "emotet": 15, "enviserv": 16, "feodo": 17, "flubot": 18,
               "fobber_v1": 19, "fobber_v2": 20, "gameover": 21, "gspy": 22, "kfos": 23, "locky": 24, "m0yv": 25, "madmax": 26, "matsnu": 27, "mirai": 28,
               "monerominer": 29, "murofet": 30, "mydoom": 31, "necro": 32, "necurs": 33, "ngioweb": 34, "nymaim": 35, "omexo": 36, "padcrypt": 37,
               "proslikefan": 38, "pykspa_v1":39, "pykspa_v2_real":40, "pykspa_v2_fake": 41, "qadars": 42, "qakbot": 43, "ramnit": 44, "ranbyus": 45, "rovnix": 46,
               "shifu": 47, "shiotob": 48, "simda": 49, "suppobox": 50, "symmi": 51, "tempedreve": 52, "tinba": 53, "tinynuke": 54, "tofsee": 55,
               "tordwm": 56, "vawtrak": 57, "vidro": 58, "virut": 59, "wauchos": 60, "xshellghost": 61}
data["family_id"] = data['family'].map(family_dict)

data=data.sort_values(by="family_id", ascending=True)
data = data.to_csv("./dga.csv", index=None)



#csv文件切分

file = pd.read_csv("./dga.csv", header=0)
levels = file["family_id"].unique()
new_family_dict = {v : k for k, v in family_dict.items()}
os.mkdir('./dataset/DGA-families/')
for level in levels:
    f = open('./dataset/DGA-families/'+str(new_family_dict[level])+'.csv', "a")
    f.write("")
    f.close()
    new_file = file[file['family_id']==level]
    new_file.to_csv("./dataset/DGA-families/"+str(new_family_dict[level])+".csv", index=False)





