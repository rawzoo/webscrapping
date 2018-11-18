# import all required library

from bs4 import BeautifulSoup
import requests
import csv
import yaml

def scrap():
    #set the url
    url = "https://www.hindustantimes.com/top-news"
    
    #send a GET request to url
    resp=requests.get(url)
    
    # if HTTP response is OK
    if resp.status_code==200: 
        print("Successfully opened the web page") 
        print("The news are as follow :-\n") 
        
        # query the website and return the html to the variable ‘soup'
        soup=BeautifulSoup(resp.text,'html.parser')	
        
        
        news = []    # a list to store news 
        
        # Take out the <ul> of name and get its value
        table = soup.find("ul", attrs = {"class":"latest-news-bx more-latest-news more-separate"})
        
        # Iterate to each <div> tag
        for row in table.findAll("div",attrs = {"class":"media"}):
            
            new={}
            new['DATE']=row.span.text
            new['LINK']=row.a['href']
            new['HEADLINE']=row.img['title']
            
            # append the extracted data to news list
            news.append(new)
            
            # print data in fomatted way
            yaml.dump(news, default_flow_style=False).strip("/u")
            print(yaml.dump(news, default_flow_style=False).replace("\\",""))
            
        
        # create and open csv file
        f = open("sample.csv", "w")
        
        # write the fieldnames to each columns
        w = csv.DictWriter(f,fieldnames=['DATE','LINK','HEADLINE'])
        w.writeheader()
        
        # iterate to each news and append to csv file into rows
        for new in news:
            w.writerow(new)

# calling the function
scrap()
