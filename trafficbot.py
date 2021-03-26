import urllib2
print ("Visitor bot by Saidur")
print ("------------------------------------------------")
 
url1 = raw_input("Enter URL(with http://):");
bar=int(input("Enter Visitor Number:"))
p11="http://www.webproxyusa.com/browse.php?u=";
p22="http://free-proxyserver.com/browse.php?u=";
p33="http://www.4freeproxy.com/browse.php?u=";
p44="http://www.pinproxy.com/browse.php?u=";
p55="http://covertproxy.com/browse.php?u=";
def view():
    url2=url1
    vt=bar
    p1=p11
    p2=p22
    p3=p33
    p4=p44
    p5=p55
    if(vt%2!=0 and vt%3==0):
        url=p1+url2;
    elif(vt%2 ==0 and vt%4==0):
        url=p2+url2;
    elif(vt%2 ==0 or vt%4 ==0):
        url=p4+url2;
    elif(vt%2 !=0 or vt%3 ==0):
        url=p5+url2;
    else:
        url=p3+url2;
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent',
'Mozilla/5.0')]
    usock = opener.open(url)
    url = usock.geturl()
    data = usock.read()
    usock.close()
    print("Site Visited")
a=0
while(a!=bar):
    a=a+1
    view() 
