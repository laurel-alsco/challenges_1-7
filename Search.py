# Author: Laurel Miller
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class Searches:
    def __init__(self, driver):
        self.driver = driver

    def find_car(self, make):
        wait = WebDriverWait(self.driver, 200)
        search = self.driver.find_element_by_id('input-search')
        search.send_keys(make)
        for button in self.driver.find_elements_by_xpath \
                ('//*[@id="search-form"]//button[@type = "submit" and @ng-click = "search()"]'):
            button.click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//tbody//tr')))

    def search_query():
        web = 'https://www.copart.com/public/lots/search'

        headers = {
            'authority': 'www.copart.com',
            'method': 'GET',
            'path': '/public/data/reCaptcha/secretKey',
            'scheme': 'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'access-control-allow-headers': 'Content-Type, X-XSRF-TOKEN',
            'cookie': 'g2usersessionid=c901d8adfa52c9b09d14dc2739a50a69; G2JSESSIONID=70DBCA544F3651BA6BF789EB74F22534-n2; userLang=en; visid_incap_242093=/TW3obSMRN6bsEqc4WNq7L6a6l0AAAAAQUIPAAAAAAB2PmYVq1PJSvAsIVjUks0i; copartTimezonePref=%7B%22displayStr%22%3A%22MST%22%2C%22offset%22%3A-7%2C%22dst%22%3Afalse%2C%22windowsTz%22%3A%22America%2FDenver%22%7D; timezone=America%2FDenver; g2app.locationInfo=%7B%22countryCode%22%3A%22USA%22%2C%22countryName%22%3A%22United%20States%22%2C%22stateName%22%3A%22Oregon%22%2C%22stateCode%22%3A%22OR%22%2C%22cityName%22%3A%22Milwaukie%22%2C%22latitude%22%3A45.44623%2C%22longitude%22%3A-122.63926%2C%22zipCode%22%3A%2297222%22%2C%22timeZone%22%3A%22-07%3A00%22%7D; s_fid=27658210A6DDA5CB-13F454C7377EA0F5; s_cc=true; s_vi=[CS]v1|2EF54D600503202C-6000118840005103[CE]; _ga=GA1.2.118881959.1575656129; _gid=GA1.2.628092170.1575656129; OAGEO=US%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; usersessionid=b8d4872aca78e4e741920941deb62716; OAID=2a2b0194f92604cfaed07fa1db2988c0; _fbp=fb.1.1575656129275.868248838; __gads=ID=c8073b0f0d19b565:T=1575656129:S=ALNI_MZ3E4h7Rj__KFFVBeneBjSU_JEQRw; s_sq=%5B%5BB%5D%5D; s_ppvl=public%253Ahomepage%2C21%2C21%2C784%2C710%2C783%2C1920%2C1080%2C1%2CL; s_ppv=public%253Ahomepage%2C64%2C64%2C784%2C710%2C783%2C1920%2C1080%2C1%2CL; incap_ses_617_242093=qTfUQSG7FErs7AtlgwaQCF2v6l0AAAAAmJF0EXCKEMjC0vcb60bqqA==; s_depth=1; s_pv=public%3Ahomepage; s_nr=1575661408366-Repeat; s_vnum=1578248128249%26vn%3D2; s_invisit=true; s_lv=1575661408367; s_lv_s=Less%20than%201%20day; _gat=1',
            'if-modified-since': 'Mon, 26 Jul 1997 05:00:00 GMT',
            'pragma': 'no-cache',
            'referer': 'https://www.copart.com/',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': 'ecb579e5-b599-4bfb-9011-baf3b216b157',
        }
        s = requests.Session()
        values = ['toyota camry', 'nissan skyline', 'honda civic', 'BMW', 'kia optima', 'dodge ram',
                  'chevrolet cobalt', 'dodge charger', 'subaru outback', 'porsche 911']
        for val in values:
            params = {'query': val}
            data = params
            file = open('PostData.txt', 'w')
            query = s.post(web, data=data, headers=headers)
            json_data = query.json()
            file.write(str(json_data))
            values = (json_data['data']['results']['totalElements'])
            print(values)


