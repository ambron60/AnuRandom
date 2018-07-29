import requests
from bs4 import BeautifulSoup as bs

base_url = "https://qrng.anu.edu.au/"
class AnuRandom(object):
    @staticmethod
    def get_random_numbers(num_type):
        if num_type == "BIN":
            url = base_url + "RawBin.php"
        elif num_type == "CHAR":
            url = base_url + "RawChar.php"
        elif num_type == "HEX":
            url = base_url + "RawHex.php"
        else:
            url = None

        page_data = requests.get(url).content
        return page_data

    @staticmethod
    def parse_type(html):
        result = bs(html, 'html.parser')
        return result.find('td').text

    def get_bin(self):
        return self.parse_type(self.get_random_numbers("BIN"))

    def get_char(self):
        return self.parse_type(self.get_random_numbers("CHAR"))

    def get_hex(self):
        return self.parse_type(self.get_random_numbers("HEX"))


if __name__ == "__main__":
    data = AnuRandom()
    print(data.get_bin())  # retrieve bit stream
