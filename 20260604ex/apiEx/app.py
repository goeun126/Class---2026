import urllib.request
import datetime
import json

SERVICE_KEY = '4f30fa613b2dce14f7e3c6e61be185e93db21d6945c1971d8aae7f4b320f6aca'

def getReqeustURL(url):
    req = urllib.request.Request(url)

    
    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print(f'[{datetime.datetime.now()}]REQUEST COMMUNICATION SUCCESS!!')
            return res.read().decode('utf-8')
        
    except Exception as e:
        print(f'[{datetime.datetime.now()}]REQUEST COMMUNICATION FAIL!!')
        print(f'e:{e}')
        return None

def getTourismStatesItem(yyyymm, nat_cd, ed_cd):
    serviceURL = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameters = "?"
    parameters += "_type=json&"
    parameters += "NAT_CD=" + nat_cd + '&'
    parameters += "serviceKey=" + SERVICE_KEY + '&'
    parameters += "YM=" + yyyymm + '&'
    parameters += "ED_CD=" + ed_cd

    url = serviceURL + parameters
    res = getReqeustURL(url)
    if res == None:
        return None
    else:
        return json.loads(res)
        # json.loads()는 JSON 형식의 문자열을 (str)을 파이썬 애플리케이션에서 쉽게 사용할 수 있도록 변환함.
        # JSON 형식의 문자열을 (str) ----> dic 객체

def getTourismStatesService(nat_cd, ed_cd, nStaetYear, nEndYear):
    

    jsonResult = []
    result = []
    natName = ''
    isDataEnd = 0
    dataEND = f'{str(nEndYear)}{str(12)}'

    for year in range(nStaetYear, nEndYear + 1):    # 년도
        for month in range(1, 13):                  # 월
            if isDataEnd == 1:                      # 데이터가 없을경우 멈춤
                break

            yyyymm = f'{str(year)}{str(month):0>2}'
            jsonData = getTourismStatesItem(yyyymm, nat_cd, ed_cd)
            if jsonData['response']['header']['resultMsg'] == 'OK':
                
                # 데이터 끝 확인
                if jsonData['response']['body']['items'] == '':
                    isDataEnd = 1 # 데이터 끝 확인용 flag변수
                    dataEND = f'{str(year)}{str(month-1):0>2}'
                    print('DATA END!!')
                    break

                # json adta 확인
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ','')   # 중    국  -> 중국
                num = jsonData['response']['body']['items']['item']['num']   # 방문자수
                ed = jsonData['response']['body']['items']['item']['ed']   # 방한외래관광객
                print(f'[{natName}][{num}][{ed}]')

                jsonResult.append({
                    'nat_name':natName,
                    'nat_cd':nat_cd,
                    'yyyymm':yyyymm,
                    'visit_cut':num
                })

    return (jsonResult, natName, ed, dataEND)

def main():

    jsonResuit = []
    natName = ''

    print('----------------------------------------------')
    print('------- 국내 입국한 외국인 통계 데이터 -------')
    print('----------------------------------------------')

    nat_cd = input('국가 코드 입력[중국(112),일본(130),미국(275)]:')
    nStaetYear =  int(input('데이터 수집 시작 년도:'))
    nEndYear = int(input('데이터 수집 끝 년도:'))
    ed_cd = 'E' # E:입국 D:출국

    jsonResult, natName, ed, dataEND = getTourismStatesService(nat_cd, ed_cd, nStaetYear, nEndYear)

    if natName == '':
        print('데이터 수집 오류 서버 담당자 에게 문의 하세요')

    else:
        print('데이터 수집 성공')
        with open(f'./{natName}_{ed}_{nStaetYear}_{dataEND}.json', 'w', encoding='utf-8') as f:
            jsonFilb = json.dumps(jsonResuit, indent=4, sort_keys=True, ensure_ascii=False)
            f.writable.jsonFilb

if __name__=='__main__':
    main()