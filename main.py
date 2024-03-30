from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from lxml import html
import requests
import uvicorn



app = FastAPI()
hackernewsURL = "https://news.ycombinator.com/"



origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:80",
    "http://localhost:443",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def getLatestArticles():
    
    response = requests.get(hackernewsURL)
    

    if response.status_code == 200:
        
        # scraping logic !!
        page = html.fromstring(response.content)
        print(page)
        
        newsHeaders = [element.text for element in page.xpath("//span[@class='titleline']/a")]
        newsDictionary = {i + 1: text for i, text in enumerate(newsHeaders)}
        # removing \t\n
        newsDictionary = {key: value.strip() for key, value in newsDictionary.items()}
        # removing empty key-value like this ""
        newsDictionary = {key: value for key, value in newsDictionary.items() if value.strip() != ""}
        
        return newsDictionary
        


    else:
        return {"error" : "Failed to fetch data from Hackernews!!"}
    
if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)

