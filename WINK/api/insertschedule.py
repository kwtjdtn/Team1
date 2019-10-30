from bs4 import BeautifulSoup

from login.models import UserScheduleDB


def scheduleDB(id,page):




    userSchdule = UserScheduleDB.objects.all()
    userSchdule = userSchdule.filter(student_code=id)
    # print(userSchdule)
    if str(userSchdule) == '<QuerySet []>':

        html = page
        soup = BeautifulSoup(html, 'html.parser')
        soup.prettify(formatter=lambda s: s.replace('&nbsp', ''))
        notices = soup.findAll('td', attrs={'rowspan': '2'})
        notices2 = soup.findAll('td', attrs={'rowspan': '3'})
        # for n in notices:
        #     print(n.text)
        result = ""
        for n in notices2:
            # print(n.text)
            result += n.text

        blank = result[0]
        result = result.replace(blank, '#')
        result = result[1:]
        # print(result)
        result += '!'
        word = ''

        count = 0
        dataA = ''
        dataB = ''
        dataC = ''
        dataD = ''
        dataE = ''
        dataF = ''
        # print(result)
        temp = ''
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
                        # print(dataA)
                        # print(dataB)
                        # print(dataC)
                        # print(dataD)
                        # print(dataE)
                        # print(dataF)
                        # print(dataG)
                        dbInstance = UserScheduleDB(student_code=id, time=dataA, A=dataB, B=dataC,
                                                    C=dataD,
                                                    D=dataE,
                                                    E=dataF, F=dataG)
                        dbInstance.save()

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

                        # print(dataA)
                        # print(dataB)
                        # print(dataC)
                        # print(dataD)
                        # print(dataE)
                        # print(dataF)
                        # print(dataG)
                        dbInstance = UserScheduleDB(student_code=id, time=dataA, A=dataB, B=dataC,
                                                    C=dataD,
                                                    D=dataE,
                                                    E=dataF, F=dataG)
                        dbInstance.save()

                word = ''