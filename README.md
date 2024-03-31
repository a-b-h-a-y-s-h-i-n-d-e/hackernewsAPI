# FastAPI TechCrunch Scraper

This is a FastAPI application that scrapes the latest articles from TechCrunch.

## Features

- Fetches the latest articles from TechCrunch website.
- Returns the article titles in a dictionary format.

## Code to use this API

```
import requests

response = requests.get("https://hackernews-api-mu.vercel.app/")
print(response.json())

```