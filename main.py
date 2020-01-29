from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget
import urllib
import requests
import sys

#공지를 제외시킨 게시글 리스트를 반환함
def ignore_notice(title_list):
    for i in title_list:
        if i.find("em", {"class":"icon_notice"}) or i.find("span", {"class":"reply_num"}):
            pass
        else:
            return i.text

#첫 번째 글의 제목을 반환함
def get_title():
    gallery = requests.get('http://gall.dcinside.com/mgallery/board/lists?id=aoegame', headers = headers)
    soup = BeautifulSoup(gallery.text, "html.parser")
    title_list = soup.select('.gall_list > tbody > tr > .gall_tit > a')
    #반환할 때에 리스트에서 공지를 제외시킬 필요가 있음
    return ignore_notice(title_list)

#메인
if __name__ == "__main__":
    headers = {'Referer':'https://www.dcinside.com/',
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    before_title = get_title()

    print(get_title())