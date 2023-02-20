import logging
# TODO
# 1. 로그 색상 변경
# 2. 파일 상대 경로로 변경

class TreeWikiLog:
    # 전역변수로 사용할 변수 선언
    def __init__(self):
        # Logging 설정
        self.mbtiLogger = logging.getLogger(__name__)
        self.mbtiLogger.setLevel(logging.DEBUG)

        # format 설정
        self.mbtiFormat = logging.Formatter('[%(asctime)s] [%(module)s] [%(levelname)s] : %(message)s ', '%Y-%m-%d %H:%M:%S')

        # Console Logging 설정
        console_hander = logging.StreamHandler()
        console_hander.setLevel(logging.INFO)
        console_hander.setFormatter(self.mbtiFormat)
        self.mbtiLogger.addHandler(console_hander)

        # file Logging 설정
        file_Handler = logging.FileHandler('Carwling.log')
        file_Handler.setLevel(logging.DEBUG)
        file_Handler.setFormatter(self.mbtiFormat)
        self.mbtiLogger.addHandler(file_Handler)

    def getLogging(self):
        return self.mbtiLogger