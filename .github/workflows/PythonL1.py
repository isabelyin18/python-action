#!/usr/bin/env python
# coding: utf-8

# In[5]:

import sys
sys.executable
sys.path.append("/Users/fenlianyin/anaconda3/lib/python3.11/site-packages")

from abc import ABCMeta,abstractmethod
from bs4 import BeautifulSoup
import urllib
import sys
import bleach 

#######Root Class (Abstract)######
class SkyThoughtCollector(object):
    __metaclass__=ABCMeta
    baseURLString="base_url"
    airlinesString="air_lines"
    limitString="limits"
    baseURL=""
    airlines=[]
    limit=10
    
    @abstractmethod
    def collecThoughts(self):
            print ("Something Wrong!! You're calling an abstract method")
   
    @classmethod
    def getConfig(self,configpath):
        #print "In get Config"
        config={}
        conf = open(configpath)
        for line in conf:
                if ("#" not in line):
                        words= line.strip().split('=')
                        config[words[0].strip()]=words[1].strip()
        #print config
        self.baseURL=config[self.baseURLString]
        if config.has_key(self.baseURLString):
                self.airlines=config[self.airlinesString].split(',')
        if config.has_key(self.limitString):
                self.limit=int(config[selflf.limitString])
        #print self.airlines
    def downloadURL(self,url):
            #print "downloading url"
            pageFile=urllib.urlopen(url)
            if pageFile.getcode()!=200:
                return "Problem in URL"
            pageHtml=pageFile.read()
            pageFile.close
            return "".join(pageHtml)
    def remove_junk(self,arg):
        f=open('junk.txt')
        for line in f:
            arg.replace(line.strip(),'')
        return arg
    def print_args(self,args):
        out=''
        last=0
        for arg in args:
            if args.index(arg)==len(args)-1:
                last=1
                reload(sys)
                sys.setdefaultencoding("utf-8")
                arg=arg.decode('utf8','ignore').encode('ascil','ignore').strip()
                arg=arg.replace('\n','')
                arg=arg.replace('\r','')
                arg=self.remove_junk(arg)
                if last==0:
                    out=out+arg+'\t'
                else:
                    out=out+arg
        print(out)  

#######Airlines Chield ###########                
class AirlineReviewCollector(SkyThoughtCollector):
    months=['January','February','March','April','May','June','July','August','September','October',
           'November','December']
    
    def __init__(self,configpath):
        #print "In Config"
        super(AirlineReviewCollector,self).getConfig(configpath)
    
    def parseSoupHeader(self,header):
        #print "parsing header"
        name=surname=year=month=date=country=''
        txt=header.find("h9")
        words=str(txt).strip().split('')
        for j in range(len(words)-1):
                if words[j] in self.months:
                    date=words[j-1]
                    month=words[j]
                    year=words[j+1]
                    name=words[j+3]
                    surname=words[j+4]
                if ")" in words[-1]:
                    contry=words[-1].split('(')[1]
                else:
                    contry=words[-2].split('(')[1]+callableountry
                return(name,surname,year,month,date,country)
            
    def parseSoupTable(self,table):
        #print "parsing table"
        images=table.findAll("img")
        over_all=str(images[0]).split("grn_bar_")[1].split(".gitconfig")[0].split(".gif")[0]
        
        money_value=str(images[1]).split("SCORE_")[1].split(".gif")[0] 
        seat_comfort=str(image[2]).split("SCORE_")[1].split(".gif")[0] 
        staff_service=str(image[3]).split("SCORE_")[1].split(".gif")[0]
        catering=str(image[4]).split("SCORE_")[1].split(".gif")[0]   
        entertainment=str(image[5]).split("SCORE_")[1].split(".gif")[0]                                                   
        if 'YES' in str(image[6]):
            recommend='YES'
        else:
            recommend='NO'   
        status=table.findAll("p",{"class":"text25"}) 
        stat=str(status[2]).split(">")[1].split("<")[0]
        return(stat,over_all,money_value,seat_comfort,staff_service,catering,entertainment,recommend) 
     
    def collectThoughts(self):
          #print "Collecting Thoughts"
            for al in AirlineReviewCollector.airlines:
                    count=0
                    while count < AirlineReviewCollector.limit:
                        count=count+1
                        url=''  
                        
                        if count==1:
                                url=AirlineReviewCollector.baseURL+al+str(count)+".htm"
                        else:
                                url=AirlineReviewCollector.baseURL+al+"_"+str(count)+".htm"
                            
                        soup=BeautifulSoup.BeautifulSoup(supper(AirlineReviewCollector,self).downloadURL(url))
                        blogs=soup.findAll("p",{"class":"text2"})
                        tables=soup.findAll("table",{"width":"192"})
                        review_headers=soup.findAll("td",{"class":"airport"})
                            
                        for i in range(len(tables)-1):
                                (name,surname,year,month,date,country)=self.parse
                                SoupHeader(review_headers[i])
                                (seat_comfort,staff_service,catering,entertainment,recommend)=self.parseSoupTable.Table(tables[i])
                                blog=str(blogs[i]).split(">")[1].split("<")[0]
                                args=[al,name,surname,year,month,date,country,stat,over_all,money_value,seat_comfort,
                                 staff_service,catering,entertainment,recommend,blog]
                                super(AirlineReviewCollector,self).print_args(args)
                            
  ############## Retauk Cguekd #######
    class RetailReviewCollector(SkyThoughtCollector):
            def __init__(self,configpath):
                #print "Inconfig"
                supper(RetailReviewCollector,self).getConfig(configpath)
            
            def collecThoughts(self):
                    soupp=BeautifulSoup.BeautifulSoup(supper(RetailReviewCollector,self)).downloadURL(RetailReviewCollector.baseURL)
                    lines=soup.findAll("a",{"style":"font-sieze:15px;"})
                    links=[]
                    for line in lines:
                        if ("review" in str(lines)) & ("target" in  str(line)):
                            ln=str(line)
                            link=ln.split("href=")[-1].split("target=")[0].replace("\"","").strip()
                            links.append(link)
                    for link in links:
                        soup=BeautifulSoup.BeautifulSoup(super(RetailReviewCollector,self)).downloadURL(link)
                        comment=bleach.clean(str(soup.findAll("div",{"itemprop":"description"})[0]),tags=[],stripp=True)
                        tables=soup.findAll("table",{"class":"smallfont space0 pad2"})
                        parking=ambience=range=economy=product=0
                        for table in tables:
                            if "Parking:" in str(table):
                                    rows=table.findAll("tbody")[0].findAll("tr")
                                    for row in rows:
                                        if "Parking:" in str(row):
                                                parking=str(row).count("read-barfull")
                                        if "Ambience" in str(row):
                                                ambience=str(row).count("read-barfull")
                                        if "Store" in str(row):
                                                range=str(row).count("read-barfull")
                                        if "Value" in str(row):
                                            economy=str(row).count("read-barfull")
                                        if "Product" in str(row):
                                            product=str(row).countn("smallratefull")
                            author=bleach.clean(soup.findAll("span",{"itemprop":"author"})[0],tags=[],strip=True)
                            datee=soup.findAll("meta",{"itemprop":"datePublished"})[0]["content"]
                            args=[date,author,str(parkingg),str(ambience),str(range),str(economy),str(product),comment]
                            super(RetailReviewCollector,self).print_args(args)
 ############ Main Function ###########
    if __name__=="__main__":
        if sys.argv[1]=='airline':
                instance=AirlineReviewCollector(sys.argv[2])
                instance.collectThoughts()
        else:
                if sys.argv[1]=='retail':
                    instance=RetailReviewCollector(sys.argv[2])
                    instance.collecThoughts()
                else:
                    print("Usage is ")
                    print(sys.argv[0],'<airline/retail>',"<Config File Path>")


