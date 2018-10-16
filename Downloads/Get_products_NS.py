# -*- coding: UTF-8 -*-
import requests
import json

out = open("/home/hardt/Dropbox/club_mobili_html/API/images.txt", "a") #LOCAL FISICO MEU PC

temp = []

def copy_NS_database():
    url = "https://api.tiendanube.com/v1/753712/products?per_page=200"
    headers = {
        'Authentication': "bearer 3ef42057093c10412ab323dbd120ead57ee220fc",
        'Cache-Control': "no-cache"
        }
    response = requests.get(url, headers=headers).json()
    data = json.loads(json.dumps(response))

    
    #data2 = json.dump(data,f,indent=4)



    data2 = json.dumps(data, sort_keys=True, indent=4)

    for produtos in data:
        for variantes in produtos["variants"]:
            if (variantes["sku"] != None and ((str(variantes["sku"]))[0:7]) not in temp):
                if (str(variantes["sku"]))[8:12] != "0000":
                    a = ((str(variantes["sku"]))[0:7])
                    temp.append(a)
                    
                    if produtos["images"] != []:
                        #print produtos["images"][0]["src"]
                        out.write(a)
                        out.write(";")
                        out.write(produtos["images"][0]["src"])
                        out.write('\n')
copy_NS_database()