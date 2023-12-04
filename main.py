import requests

stuffList = ["img1", "img2", "img3"]
stuffList = list(range(1, 3))
byType = 0
baseurl = "https://example.com/"


if byType==0:
  # subs.txt used
  file = open("subs.txt", "r")
  subs = file.read().split("\n")
  print(subs)
  file.close()
  
  for r in subs:
    r = r.split(" ", 1)[0]
  
    if "." in r:
      response = requests.get(baseurl+r)
      open(r, "wb").write(response.content)
      
elif byType==1:
  # smth with numbers used
  x = 0
  
  while x <= len(stuffList):
    j = str(stuffList[x]).zfill(0)
    response = requests.get(baseurl + j + ".fileEnd")
    open(("" + j + ".fileEnd"), "wb").write(response.content)
    x += 1

elif byType==2:
  # list used
  for r in stuffList:
    response = requests.get(baseurl + r + ".fileEnd")
    open((r  + ".fileEnd"), "wb").write(response.content)
  
