#!/usr/bin/env python
# coding: utf-8

# In[36]:


import requests
from bs4 import BeautifulSoup
import pandas

list1=[]

for page in range(0,30,10):
    
    r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="+str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c= r.content

    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    x=all[0].find("h4",{"class":"propPrice"}).text
    

    
    for item in all:
        d={}

        d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        
        try:
            d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"]=None
        
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").strip()
        try:
            d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"]=None



        try:
            d["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"]=None

        try:
            d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None

        try:
            d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None

        for column_group in item.find_all("div",{"class":"columnGroup"}):
            for fg , fn in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in fg.text :
                    d["Lot Size"]=fn.text

        list1.append(d)
df=pandas.DataFrame(list1)
df.to_csv("output.csv")
        



