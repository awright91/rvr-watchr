import requests
from bs4 import BeautifulSoup
from rivers.models import River


class UpdateRiver():
    def __init__(self, url, current_level=0):
        self.url = url
        self.current_level = current_level

    def make_initial_request(self):
        try:
            soup_request = requests.get(self.url)
            content = soup_request.content
            soup = BeautifulSoup(content, 'html.parser')
            return soup
        except requests.exceptions.ConnectionError:
            requests.status_code = "Could Not Find URL"
            return ''


    def get_new_level(self, soup):
        new_table = soup.find_all('tr', class_='row-1')

        for idx, table in enumerate(new_table):
            if idx == 2:
                for idx, child in enumerate(table.children):
                    if idx == 3:
                        for idx, c in enumerate(child):
                            if idx == 5:
                                full_text_level = c.get_text().split()
                                txt_level = full_text_level[0]
                                self.current_level = float(txt_level)

        return self.current_level




def runUpdate():

    rivers = River.objects.all()

    for river in rivers:
        newUpdate = UpdateRiver(river.url)
        newSoup = newUpdate.make_initial_request()
        newUpdate.get_new_level(newSoup)
        river.current_level = newUpdate.current_level
        river.save()
        print("the river: {} had an old level of : {} and the new level is {}".format(river.name, river.current_level, newUpdate.current_level))
