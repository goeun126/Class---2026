import urllib.request
import datetime
import json

# NAVER 데이터 수집에 필요한 출입증
client_id = '1JpN61biLGVpu23H0EBN'
client_secert = 'XHNI8GJKHu'

# NAVER 에서 데이터를 가져오는녀셕
# 출입증 역할
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secert)

    # 안전장치 설치
    try:
        response =  urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')
            # print(f'response data:{response.read().decode('utf-8')}')
            # decode란 바이트(bytr) 코드를 문자열(string)로 변환해주는것.
            return response.read().decode('utf-8')
        
    # 에러날 씨 컴퓨터를 멈추지말고 조용히 알려주고 빈손으로 돌아오라는 뜻
    except Exception as e:
        print(f'[{datetime.datetime.now()}]Error:{e}')
        return None

# NAVER 심부름 하는 아이 / 뉴스 보관소를 가서 상세 지도 가져옴
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'    # news.json
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode == None:
        return None

    # 이버가 통째로 던져준 길고 복잡한 글자더미를, 
    # 파이썬이 쓰기 좋게 '서랍장(딕셔너리/리스트)' 형태로 예쁘게 분리수거해서 돌려 주는 역할
    else:
        return json.loads(responseDecode)

# NAVER 뉴스 덩어리에서 제목,날짜 같은 알맹이만 쏙쏙 골라내는 요약본
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({
        'cnt':cnt,
        'title':title,
        'description':description,
        'org_link':org_link,
        'link':link,
        'pDate':pDate
    })

# 시작점
def main():
    node = 'news'         # 크롤링 하는 대상
    srcText = input('검색어 입력: ')
    cnt = 0
    jsonResult = [] 

    # 주소조립
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    # print(f'jsonResponse{jsonResponse}')
    # print(f'jsonResponse total:{jsonResponse['total']}')
    # print(f'jsonResponse items 0:{jsonResponse['items'][0]}')
    # print(f'jsonResponse items 0:{jsonResponse['items'][0]['title']}')
    # print(f'jsonResponse items 0:{jsonResponse['items'][0]['title']['description']}')

    while jsonResponse != None and jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

    # 파일로 저장(날씨_naver_news.json)
    with open(f'{srcText}_naver_{node}.json', 'w', encoding='utf8') as f:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)

if __name__=='__main__':
    main()