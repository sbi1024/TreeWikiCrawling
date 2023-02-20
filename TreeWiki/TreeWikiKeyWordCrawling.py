# from 패키지 이름 import 파일 이름
from util import TreeWikiLogging

class TreeWikiKeyWordCarwling:
    # 전역변수로 사용할 변수 선언
    def __init__(self):
        # Log 객체 선언 → debug 이상 레벨 선언
        self.Log = TreeWikiLogging.TreeWikiLog()
        self.Log = self.Log.getLogging()

