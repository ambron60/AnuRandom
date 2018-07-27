import requests
from bs4 import BeautifulSoup as bs

base_url = "https://qrng.anu.edu.au/"


class AnuRandom(object):
    def get_random_numbers(self, type):
        if type == "BIN":
            url = base_url + "RawBin.php"
        elif type == "CHAR":
            url = base_url + "RawChar.php"
        elif type == "HEX":
            url = base_url + "RawHex.php"

        data = requests.get(url).content
        return data

    def get_bin(self):
        return self.parse_type(self.get_random_numbers("BIN"))

    def get_char(self):
        return self.parse_type(self.get_random_numbers("CHAR"))

    def get_hex(self):
        return self.parse_type(self.get_random_numbers("HEX"))

    def parse_type(self, html):
        result = bs(html, 'html.parser')
        return (result.find('td').text)


if __name__ == "__main__":
    data = AnuRandom()
    # print(data.get_bin())
