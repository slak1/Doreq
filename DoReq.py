import requests ,sys  ,os ,importlib
arg=sys.argv;
if len(arg)<4:
    print('DoReq4.py NamePythonModule')
    sys.exit();
arg1=arg[1];
if arg1[len(arg1)-3:]=='.py': arg1=arg1[:-3];

reqMod=importlib.import_module(arg1)  #import (arg1) as reqMod

class datas():
    def __init__(self):
        self.url='';
        self.data=None;
        self.headers=None;
        self.response=None;
        self.login=None;
        self.passw=None;

dane=datas();
dane=reqMod;

dane.url= reqMod.headers["Origin"];
dane.login=arg[2];
dane.passw=arg[3];
#dane.data=reqMod.data;
#dane.headers=reqMod.headers;

print(dane.headers)

def Readln(filepath):
   global dane
   filepath=filepath+'.py'
   with open(filepath) as fp:
    line = fp.readline()
    while line:
     l=line.strip(); dl=len(l);
     if l[:8]=='response':
        a=l.find('\'')+1
        b=l.rfind('\'')
        return l[a:b]
     line = fp.readline()


def main():
 global dane

 def seeData():
  global dane
  for key, value in dane.data.items():
     print(key, '----------', value )
  print("____________________________________")


 def transf():
  global dane
  for key, value in dane.data.copy().items():
    x=len(value);
    if x>1 :
       postfix = value[x-1:x]
       #print(value, value[x-1:x] )
       if postfix=='^':
        #print(dane.data[key])
        dane.data[key]=value[:x-1]
        print(key,"-------",dane.data[key])
  print("-------END TRASFORM---------")


 print(dane.data)
 transf();
 seeData()
 #print (Readln(arg1))

if __name__ == '__main__':
    main()
    print (Readln(arg1))
    #sys.exit();
    with requests.Session() as s:
     #s.get(dane.url, auth=('admin', 'zlotko14n'))
     s.get(dane.url, auth=(dane.login, dane.passw))
     #r = s.post(dane.url+'/apply.cgi', headers=dane.headers, data=dane.data)
     #r = dane.response;
     r = s.post(Readln(arg1), headers=dane.headers, data=dane.data)

     #print(r.text)
     print('Zapis')
     with open("DoReq5.html", "wb") as f:
      f.write(r.content)
