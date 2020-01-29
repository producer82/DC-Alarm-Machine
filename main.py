from bs4 import BeautifulSoup
import urllib
import requests

def get_title():
    gallery = requests.get('http://gall.dcinside.com/mgallery/board/lists/?id=apistogramma&page=1', headers = headers)
    soup = BeautifulSoup(gallery.text, "html.parser")
    title_list = soup.select('.gall_list > tbody > tr > .gall_tit > a')
    first_title = title_list[4].text

    return first_title

if __name__ == "__main__":
    headers = {'Referer':'https://www.dcinside.com/',
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    before_title = get_title()

    while(1):
        if(before_title != get_title()):
            print("새로운 글 올라옴")
            before_title = get_title()


    