from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import json
from urllib import parse

# from 패키지 이름 import 파일 이름
from util import TreeWikiLogging



class TreeWikiMbtiCarwling:
    # 전역변수로 사용할 변수 선언
    def __init__(self):
        # Log 객체 선언
        self.Log = TreeWikiLogging.TreeWikiLog()
        self.Log = self.Log.getLogging()

        # 나무위키 주소 값
        self.treeWikiPreUrl = "https://namu.wiki/w/"
        # keyword 값 선언
        self.keyword = ["한소희","박보영","유라","혜리" , "차승원" , "김우빈"]
        # headers 값 선언
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        # mbti text (EX ) mbit 항목) selector 값
        self.mbtiTextElement = "#VIVXXZe6L > div.a0c386b2 > div > div > div.t6-tWlbV > div:nth-child(4) > div:nth-child(4) > div > div > div > div > div > div > div > div > div:nth-child(9) > div > div > div > div > div:nth-child(1) > div > div.qYoqha5U.I-ibKx\+f > table > tbody > tr:nth-child(13) > td:nth-child(1) > div > strong"
        # 실제 인원 mbti 값 ( EX ) ESFJ ) selecttor 값
        self.mbitElement = "#VIVXXZe6L > div.a0c386b2 > div > div > div.t6-tWlbV > div:nth-child(4) > div:nth-child(4) > div > div > div > div > div > div > div > div > div:nth-child(9) > div > div > div > div > div:nth-child(1) > div > div.qYoqha5U.I-ibKx\+f > table > tbody > tr:nth-child(13) > td:nth-child(2) > div > a.DCLJQsNO"
        # 전역적으로 사용할 soup 선언
        self.soup = ""

    # crawling main 진입 점
    # → 이 메소드만 호출해서 크롤링 진행 할 예정
    def treeWikiMainCrawling(self):
        for index, keyword in enumerate(self.keyword):
            # 나무위키 html 값 선언
            treeWikiHtml = self.getTreeWikiHtml(keyword)
            # BeautifulSoup 를 사용하기 위해 파싱 진행
            self.soup = bs(treeWikiHtml, "html.parser")
            # mbit 항목 데이터 확인
            mbtiText = self.getTreeWikiMbtiText()
            if str(mbtiText).__eq__("MBTI"):
                # mbit 데이터 확인
                mbti = self.getTreeWikiMbti()
                # 결과값 출력
                self.Log.info(str(index + 1) + " → " + keyword + " (" + mbtiText + " 항목 존재" + ") " + ": " + mbti)
                self.Log.debug(str(index + 1) + " → " + keyword + " (" + mbtiText + " 항목 존재" + ") " + ": " + mbti)
            else :
                # 결과값 출력
                self.Log.info(str(index + 1) + " → " + keyword + " (" + "MBTI 항목 미 존재" + ") " + ": " + "MBTI 항목이 존재 하지 않음.")
                self.Log.debug(str(index + 1) + " → " + keyword + " (" + "MBTI 항목 미 존재" + ") " + ": " + "MBTI 항목이 존재 하지 않음.")



    # mbti 항목 데이터
    def getTreeWikiMbtiText(self):
        # soup를 통해 , mbti 항목 데이터 추출
        mbtiText = self.soup.select_one(self.mbtiTextElement).text
        # 결과값(mbtiText) 리턴
        return mbtiText

    # mbti 데이터
    def getTreeWikiMbti(self):
        # soup를 통해 , mbti 데이터 추출
        mbti = self.soup.select_one(self.mbitElement).text
        # 결과값(mbti) 리턴
        return mbti

    # 나무위키 html 데이터를 리턴해주는 메소드 선언
    def getTreeWikiHtml(self,keyword):
        # url = 나무위키 기본 주소값 + 검색하고자 하는 키워드값의 인코딩
        url = self.getTreeWikiUrl(keyword)
        # request 요청값에 header 값 추가
        urlRequest = Request(url, headers=self.headers)
        # 받은 결과값 decode 하여 확인
        result = urlopen(urlRequest).read().decode("utf-8")
        # 결과값(result) 리턴
        return result

    # 접근 하고자 하는 나무위키 url 주소를 계산
    def getTreeWikiUrl(self, keyword):
        # 요청값의 keyword 값을 통해 encoding (UTF-8) 진행
        encodeUrl = parse.quote(keyword)
        # 진짜 크롤링 하고자 하는 페이지 URL 추출
        result = self.treeWikiPreUrl + encodeUrl
        # 결과값(result) 리턴
        return result

