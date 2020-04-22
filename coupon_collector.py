import requests
from bs4 import BeautifulSoup
import pandas as pd


title_list=[]
img_list=[]
link_list=[]



base_url="https://udemycoupon.learnviral.com/page/"
r=requests.get('https://udemycoupon.learnviral.com',headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
soup=BeautifulSoup(r.content, "html.parser")
page_num_class=soup.find_all("a", {"class":"page-numbers"})
page=page_num_class[-2].text.replace(",","")

for i in range(1,int(page)-1):
    url=base_url + str(i)
    print('Working on {%s} \n' %url)
    r=requests.get(url,headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    soup=BeautifulSoup(r.content, "html.parser")
    all_sec=soup.find_all("div", {"class":"item-holder"})
    for item in all_sec:
        try:
            heading=item.find("h3",{"class":"entry-title"})
            title_list.append(heading.text)
        except:
            title_list.append('None')
        try:
            img_div=item.find("div",{"class":"store-image"})
            img=img_div.find("img")
            img_list.append(img['src'])
        except:
            img_list.append("None")
        try:
            link=item.find("a", {"class":"coupon-code-link btn promotion"})
            link_list.append(link['href'])
        except:
            link_list.append('None')

    df=pd.DataFrame({"Title":title_list, "Img link": img_list, "Link":link_list})
    df.to_csv("output.csv")
    print('Done {%s} \n' %url)



