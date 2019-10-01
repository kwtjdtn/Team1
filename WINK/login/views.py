
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your tests here.

from selenium import webdriver
from bs4 import BeautifulSoup


def index(request):
    return render(request,'login/wink.html')
#######chrome option
from login.models import UserScheduleDB, UserScheduleDB

path = 'C:/chromedriver.exe'  # ex. C:/downloads/chromedriver.exe
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(path, chrome_options=options)
###############chrome option end
def Login(request):
    #####check having data
    model_instance = UserScheduleDB.objects.all()
    model_instance = model_instance.filter(student_code='20153159')
    queryset = len(str(model_instance))


    if(queryset==13):
        driver.get('https://ktis.kookmin.ac.kr/')
        driver.implicitly_wait(3)
        id = request.POST['id']
        pw = request.POST['pw']
        driver.execute_script("document.getElementsByName('txt_user_id')[0].value=\'" + id + "\'")
        # time.sleep(1)
        driver.execute_script("document.getElementsByName('txt_passwd')[0].value=\'" + pw + "\'")
        # time.sleep(1)

        driver.find_element_by_xpath(
            '/html/body/form[1]/table/tbody/tr/td/table/tbody/tr[4]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input').click()
        driver.implicitly_wait(3)
        try:
            driver.get('https://ktis.kookmin.ac.kr/kmu/ucb.Ucb0164rAGet01.do')
            html = driver.page_source

            soup = BeautifulSoup(html, 'html.parser')
            soup.prettify(formatter=lambda s: s.replace('&nbsp', ''))
            notices = soup.findAll('td', attrs={'rowspan': '2'})
            notices2 = soup.findAll('td', attrs={'rowspan': '3'})
            # for n in notices:
            #     print(n.text)
            result = ""
            for n in notices2:
                print(n.text)
                result += n.text

            blank = result[0]
            result = result.replace(blank, '#')
            result = result[1:]
            print(result)
            result += '!'
            word = ''

            count = 0
            dataA = ''
            dataB = ''
            dataC = ''
            dataD = ''
            dataE = ''
            dataF = ''
            dataG = ''
            dataH = ''
            for i in result:
                if i != '#':
                    word += i
                else:
                    if word == '':
                        word = 'blank'
                        if count == 0:
                            dataA = word
                            count += 1
                        elif count == 1:
                            dataB = word
                            count += 1
                        elif count == 2:
                            dataC = word
                            count += 1
                        elif count == 3:
                            dataD = word
                            count += 1
                        elif count == 4:
                            dataE = word
                            count += 1
                        elif count == 5:
                            dataF = word
                            count += 1
                        elif count == 6:
                            dataG = word
                            count = 0
                            # print(dataA+dataB+dataC+dataD+dataE+dataF)
                            print(dataA)
                            print(dataB)
                            print(dataC)
                            print(dataD)
                            print(dataE)
                            print(dataF)
                            print(dataG)

                            dbInstance = UserScheduleDB(student_code='20153159', time=dataA, A=dataB, B=dataC, C=dataD,
                                                        D=dataE,
                                                        E=dataF, F=dataG)
                            dbInstance.save()

                        # print(word)


                    else:

                        if count == 0:
                            dataA = word
                            count += 1
                        elif count == 1:
                            dataB = word
                            count += 1
                        elif count == 2:
                            dataC = word
                            count += 1
                        elif count == 3:
                            dataD = word
                            count += 1
                        elif count == 4:
                            dataE = word
                            count += 1
                        elif count == 5:
                            dataF = word
                        elif count == 6:
                            dataG = word
                            count = 0

                            print(dataA)
                            print(dataB)
                            print(dataC)
                            print(dataD)
                            print(dataE)
                            print(dataF)
                            print(dataG)
                            # print(dataA + dataB + dataC + dataD + dataE + dataF)
                            dbInstance = UserScheduleDB(student_code='20153159', time=dataA, A=dataB, B=dataC, C=dataD,
                                                        D=dataE,
                                                        E=dataF, F=dataG)
                            dbInstance.save()
                        # print(word)
                        word = ''
            return HttpResponseRedirect('/admin/')
        except:
            return HttpResponseRedirect('/login/')


    ##not first login
    else:
        return HttpResponseRedirect('/admin/')



