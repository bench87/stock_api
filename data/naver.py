from bs4 import BeautifulSoup
from stock_api.decorators import either_decorator
from requests import get
from datetime import datetime


@either_decorator
def get_data_from_web(company_number):
    """
    네이버로 부터 시세를 받아 옵니다.
    :param company_number: 종목번호
    :return: str
    """
    return get('http://finance.naver.com/item/sise_day.nhn?code={}&page=1'.format(company_number)).text


@either_decorator
def parse_html(html):
    """
    네이버 주식 시세 html을 파싱하여 파이썬 리스트로 리턴합니다.
    :param html: str
    :return: list [[], [], ...]
    """
    soup = BeautifulSoup(html)
    trs = soup.findAll('tr', {'onmouseover': 'mouseOver(this)'})
    return map(lambda x: [_parse_date(x)], trs)
    

def _parse_date(tr):
    """
    날짜를 파싱하여 datetime object로 변환합니다.
    :param tr: Tag
    :return: datetime
    """
    txt_date = tr.select('td span')[0].text
    return datetime.strptime(txt_date, '%Y.%m.%d')


def get_data_frame(company_number):
    return get_data_from_web(company_number) >> parse_html
