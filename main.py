import requests, datetime, argparse
from bs4 import BeautifulSoup as bs

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t","--today",action="store_const", const="True")
    parser.add_argument("-m","--tomorrow",action="store_const", const="True")
    parser.add_argument("-y","--yesterday",action="store_const", const="True")

    arg = parser.parse_args()

    if arg.today:
        pars(dayPars = 0)
    elif arg.tomorrow:
        pars(dayPars = 1)
    elif arg.yesterday:
        pars(dayPars = -1)
    else:
        pars()

def pars(dayPars = 0, monthPars = 0, yearPars = 0):

    dt_now = datetime.datetime.today()
    date = dt_now.date()

    day = dayPars + date.day
    month = monthPars + date.month
    year = yearPars + date.year

    url = "http://wap.anosov.ru/rasp.php?d=" + str(year)+ "-"+ str(month) + "-" + str(day) + "&g=%C8%D1-21"
    # print(url)
    request = requests.get(url)
    soup = bs(request.text, "html.parser")
    teme = soup.find_all("p")
    print(date)
    print(teme[0].text)


if __name__ == "__main__":
    main()