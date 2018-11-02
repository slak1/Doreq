import requests ,sys  ,os ,importlib
arg=sys.argv;
if len(arg)<4:
    print('DoReq.py PythonFromCurlFile login pass')
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
        #print(key,"-------",dane.data[key])
  #print("-------END TRASFORM---------")

 print(dane.data)
 transf();
 seeData()

if __name__ == '__main__':
    main()
    with requests.Session() as s:
     s.get(dane.url, auth=(dane.login, dane.passw))
     r = dane.response;

     #print(r.text)
     print('Output html from: ',dane.url,"DoReq-Output.html")
     with open("DoReq-Output.html", "wb") as f:
      f.write(r.content)
