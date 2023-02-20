# from 패키지 이름 import 파일 이름 
from TreeWiki import TreeWikiMbtiCrawling


# 메인 함수
def main():
    # 파일 이름.클래스 이름
    mbtiCrawling = TreeWikiMbtiCrawling.TreeWikiMbtiCarwling()
    # 객체의 메소드 접근
    mbtiCrawling.treeWikiMainCrawling()


if __name__ == '__main__':
    main()
