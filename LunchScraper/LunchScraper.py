import datetime
from bs4 import BeautifulSoup
import urllib3


class LunchScraper:

    def download_page_from_url(self, url):
        user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
        http = urllib3.PoolManager(1, headers=user_agent)
        urllib3.disable_warnings()
        content = http.request('GET', url).data

        return content


    def extract_menu_list(self, url, menu_list):
        content = self.download_page_from_url(url)
        soup = BeautifulSoup(content,  "html.parser")

        for section in (soup.find_all("td",  {"class": "td_title"})):
            menu_list.append(section.text.strip())

        return menu_list


    def get_day_number(self):
        return datetime.datetime.today().weekday()


    # print the week menu
    def print_week_menu(self, menu_list):
        print("")
        print("------- Veckans meny ------------------------------")
        
        dayNumber = self.get_day_number()
        
        for x in range(dayNumber, 5):
            y = len(menu_list) - (5 - x)
            if x == 0:
                print("Måndag: " + menu_list[y])
            elif x == 1:
                print("Tisdag: " + menu_list[y])
            elif x == 2:
                print("Onsdag: " + menu_list[y])
            elif x == 3:
                print("Torsdag: " + menu_list[y])
            elif x == 4:
                print("Fredag: " + menu_list[y])
            else:
                print()


    # print standing meny
    def print_standing_menu(self, menu_list):
        print("")
        print("------- Stående meny ------------------------------")
        dayNumber = self.get_day_number()
        upper_range = len(menu_list)
        #Print whole menu except last elements. They are depending on day of week.
        #When Monday, skip 5 elements and only skip the last when friday.
        for x in range(0, upper_range - (5 - dayNumber)):
            print(str(x) + '. ' + menu_list[x])


def main():
        url = "https://frilaget.gastrogate.com/lunch/"
        
        menu_list = []
        lunchscraper = LunchScraper()

        #Extract menu from website.
        menu_list = lunchscraper.extract_menu_list(url, menu_list)

        #Print menu
        lunchscraper.print_week_menu(menu_list)
        lunchscraper.print_standing_menu(menu_list)


if __name__ == "__main__":
    main()



