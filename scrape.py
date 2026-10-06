import requests
from bs4 import BeautifulSoup

def fetch_website_contents(url):
    if not url.startswith(("http","https")):
        url = "https://" + url
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
       return f"Could not fetch the website. Error: {e}"
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    for tag in soup(["script", "style", "nav", "footer", "header", "img", "input"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    return f"Title: {title}\n\nPage contents:\n{text}"

