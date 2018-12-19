import os, shutil
import json
import jsonpath

filename=input("输入文件位置\n")
file=open(filename,'r')

data=json.load(file)
#print(data)
#js=json.dumps(json.load(data))
fr=open('result.json','w',encoding='utf-8')
for v in data:
   # print(v)
    if v['_source']['layers']['ip']['ip.src']=="47.75.56.162":
        json.dump(v,fr,ensure_ascii=False,indent=4)
        print(v)
        #fr.write("\n")
    if v['_source']['layers']['ip']['ip.dst']=="47.75.56.162":
        json.dump(v,fr,ensure_ascii=False,indent=4)
        print(v)
    
