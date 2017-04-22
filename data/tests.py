from django.test import TestCase
from .naver import get_data_from_web, parse_html
from pymonad import Right


class CrawlingTest(TestCase):
    def test_get_data_from_web(self):
        result = get_data_from_web('005930')
        self.assertIsInstance(result, Right)
    
    def test_parse_html(self):
        html = """
        <html lang="ko">
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=euc-kr">
        <title>네이버 금융</title>
        <link rel="stylesheet" type="text/css" href="http://finance.naver.com/css/newstock.css?20170413023219">
        <link rel="stylesheet" type="text/css" href="http://finance.naver.com/css/common.css?20170413023219">
        <link rel="stylesheet" type="text/css" href="http://finance.naver.com/css/layout.css?20170413023219">
        <link rel="stylesheet" type="text/css" href="http://finance.naver.com/css/main.css?20170413023219">
        <link rel="stylesheet" type="text/css" href="http://finance.naver.com/css/newstock2.css?20170413023219">
        <link rel="stylesheet" type="text/css" href="http://finance.naver.com/css/newstock3.css?20170413023219">
        <link rel="stylesheet" type="text/css" href="http://finance.naver.com/css/world.css?20170413023219">
        </head>
        <body>
        <script language="JavaScript">
        function mouseOver(obj){
          obj.style.backgroundColor="#f6f4e5";
        }
        function mouseOut(obj){
          obj.style.backgroundColor="#ffffff";
        }
        </script>
                        <h4 class="tlline2"><strong><span class="red03">일별</span>시세</strong></h4>
                        <table cellspacing="0" class="type2">
                        <tr>
                        <th>날짜</th>
                        <th>종가</th>
                        <th>전일비</th>
                        <th>시가</th>
                        <th>고가</th>
                        <th>저가</th>
                        <th>거래량</th>
                        </tr>
                        <tr>
                        <td colspan="7" height="8"></td>
                        </tr>
                        <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                        <td align="center"><span class="tah p10 gray03">2017.04.21</span></td>
                        <td class="num"><span class="tah p11">2,038,000</span></td>
                        <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
                        24,000
                        </span>
                    </td>
                        <td class="num"><span class="tah p11">2,024,000</span></td>
                        <td class="num"><span class="tah p11">2,070,000</span></td>
                        <td class="num"><span class="tah p11">2,024,000</span></td>
                        <td class="num"><span class="tah p11">243,226</span></td>
                        </tr>
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.20</span></td>
                            <td class="num"><span class="tah p11">2,014,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
                        31,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,029,000</span></td>
                            <td class="num"><span class="tah p11">2,040,000</span></td>
                            <td class="num"><span class="tah p11">2,004,000</span></td>
                            <td class="num"><span class="tah p11">422,977</span></td>
                            </tr>
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.19</span></td>
                            <td class="num"><span class="tah p11">2,045,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
                        30,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,065,000</span></td>
                            <td class="num"><span class="tah p11">2,071,000</span></td>
                            <td class="num"><span class="tah p11">2,045,000</span></td>
                            <td class="num"><span class="tah p11">235,258</span></td>
                            </tr>
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.18</span></td>
                            <td class="num"><span class="tah p11">2,075,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
                        3,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,084,000</span></td>
                            <td class="num"><span class="tah p11">2,091,000</span></td>
                            <td class="num"><span class="tah p11">2,064,000</span></td>
                            <td class="num"><span class="tah p11">137,213</span></td>
                            </tr>
                        
                        
                    
                    
                    
                    
                    
            
                
                    
                        
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.17</span></td>
                            <td class="num"><span class="tah p11">2,078,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
                        23,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,100,000</span></td>
                            <td class="num"><span class="tah p11">2,104,000</span></td>
                            <td class="num"><span class="tah p11">2,076,000</span></td>
                            <td class="num"><span class="tah p11">104,495</span></td>
                            </tr>
                        <tr>
                        <td colspan="7" height="8"></td>
                        </tr>
                        <tr>
                        <td colspan="7" height="1" bgcolor="#e1e1e1"></td>
                        </tr>
                        <tr>
                        <td colspan="7" height="8"></td>
                        </tr>
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.14</span></td>
                            <td class="num"><span class="tah p11">2,101,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
                        20,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,108,000</span></td>
                            <td class="num"><span class="tah p11">2,113,000</span></td>
                            <td class="num"><span class="tah p11">2,088,000</span></td>
                            <td class="num"><span class="tah p11">109,257</span></td>
                            </tr>
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.13</span></td>
                            <td class="num"><span class="tah p11">2,121,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
                        26,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,083,000</span></td>
                            <td class="num"><span class="tah p11">2,123,000</span></td>
                            <td class="num"><span class="tah p11">2,083,000</span></td>
                            <td class="num"><span class="tah p11">180,816</span></td>
                            </tr>
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.12</span></td>
                            <td class="num"><span class="tah p11">2,095,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
                        15,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,093,000</span></td>
                            <td class="num"><span class="tah p11">2,097,000</span></td>
                            <td class="num"><span class="tah p11">2,085,000</span></td>
                            <td class="num"><span class="tah p11">165,498</span></td>
                            </tr>
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.11</span></td>
                            <td class="num"><span class="tah p11">2,080,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_down.gif" width="7" height="6" style="margin-right:4px;" alt="하락"><span class="tah p11 nv01">
                        17,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,097,000</span></td>
                            <td class="num"><span class="tah p11">2,097,000</span></td>
                            <td class="num"><span class="tah p11">2,079,000</span></td>
                            <td class="num"><span class="tah p11">143,458</span></td>
                            </tr>
                            <tr onMouseOver="mouseOver(this)" onMouseOut="mouseOut(this)">
                            <td align="center"><span class="tah p10 gray03">2017.04.10</span></td>
                            <td class="num"><span class="tah p11">2,097,000</span></td>
                            <td class="num">
                        <img src="http://imgstock.naver.com/images/images4/ico_up.gif" width="7" height="6" style="margin-right:4px;" alt="상승"><span class="tah p11 red02">
                        17,000
                        </span>
                    </td>
                            <td class="num"><span class="tah p11">2,097,000</span></td>
                            <td class="num"><span class="tah p11">2,097,000</span></td>
                            <td class="num"><span class="tah p11">2,075,000</span></td>
                            <td class="num"><span class="tah p11">142,827</span></td>
                            </tr>
                        <tr>
                        <td colspan="7" height="8"></td>
                        </tr>
                        </table>
                        <!--- 페이지 네비게이션 시작--->
                        <table summary="페이지 네비게이션 리스트" class="Nnavi" align="center">
                        <caption>페이지 네비게이션</caption>
                        <tr>
                        <td class="on">
                        <a href="/item/sise_day.nhn?code=005930&amp;page=1"  >1</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=2"  >2</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=3"  >3</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=4"  >4</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=5"  >5</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=6"  >6</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=7"  >7</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=8"  >8</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=9"  >9</a>
                        </td>
        <td>
                        <a href="/item/sise_day.nhn?code=005930&amp;page=10"  >10</a>
                        </td>

                        <td class="pgR">
                        <a href="/item/sise_day.nhn?code=005930&amp;page=11"  >
                        다음<img src="http://static.naver.net/n/cmn/bu_pgarR.gif" width="3" height="5" alt="" border="0">
                        </a>
                        </td>

                        <td class="pgRR">
                        <a href="/item/sise_day.nhn?code=005930&amp;page=526"  >맨뒤
                        <img src="http://static.naver.net/n/cmn/bu_pgarRR.gif" width="8" height="5" alt="" border="0">
                        </a>
                        </td>
                        </tr>
                        </table>
                        <!--- 페이지 네비게이션 끝--->
            <script type="text/javascript" src="http://finance.naver.com/js/lcslog.js?20170413023219"></script>
            <script type="text/javascript">
                lcs_do();
            </script>
        </body>
    
        """
        result = parse_html(html)
        self.assertIsInstance(result, Right)
        self.assertEqual(len(list(result.getValue())), 10)
