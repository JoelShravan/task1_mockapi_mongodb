import requests
url='https://fruityvice.com/api/fruit/all'

def hit_url(url):
    response=requests.get(url)
    data=response.json()
    json_leng=len(data)
    head=list(data[0].keys())
    print(*head)
    print()
    for j in range(0,len(data)): 
     for i in head:
      print(data[j][i],end=' ')
     print() 
hit_url(url)