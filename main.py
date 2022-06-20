import requests
from bs4 import BeautifulSoup
import json

#yo chai just total_page access garana. But, this can be optimize
url= "https://bg.annapurnapost.com/api/search?title=%E0%A4%AC%E0%A4%9C%E0%A5%87%E0%A4%9F&page=1"
r = requests.get(url)
print(r.status_code)
htmlContent =r.content
#print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

title=soup.title
# print(title)
data= json.loads(htmlContent)
total_page=data['data']['totalPage']

# print(original[0])
# print(data['data']['items'][0])


# if we can to keep track of every execution of python file then, yeslae kun page ma previous iteration stopped vako ho track garcha.
#deriving page_count from previous requests:
# f = open("track_page.txt", "r")
# page_count = int(f.read())
# # print(page_count)
# f.close()

page_count=1
total_article=0

# https://bg.annapurnapost.com/api/search?title=%E0%A4%AC%E0%A4%9C%E0%A5%87%E0%A4%9F&page=8
original=[] #empty list for storing all articles:

def scraping(page_count, total_article):
    
  while page_count < total_page:
    parameters = {'page': page_count}
    # url= 'https://bg.annapurnapost.com/api/search', params=parameters
    r = requests.get('https://bg.annapurnapost.com/api/search?title=%E0%A4%AC%E0%A4%9C%E0%A5%87%E0%A4%9F', params=parameters)
    print(r.url)
    print(r.status_code)
    
    #if 1st request ma error ayo vane, go to next page:
    if r.status_code != 200:
      page_count =+1
      scraping(page_count,total_article)

    htmlContent =r.content
    #print(htmlContent)
    soup = BeautifulSoup(htmlContent, 'html.parser')
    data= json.loads(htmlContent)
    
    # print(len(data['data']['items']))
    for x in data['data']['items']:
    
      original.append(x)
      total_article += 1
      

    if total_article > 30: #for atleast 30 article:
      break
    page_count += 1

#end of scraping function:

#calling scraping function:
scraping(page_count,total_article)
# print("page count", page_count)
final_json_object = json.dumps(original)

# Writing to news.json
with open("news.json", "w") as outfile:
    outfile.write(final_json_object)

# print(original)



