from bs4 import BeautifulSoup
from paths import stop_words_path

with open(stop_words_path, 'r') as f:
    file = f.read()

soup = BeautifulSoup(file, 'xml')
stop_words_tags = soup.find_all('word')
stop_words_list = [sw.get_text() for sw in stop_words_tags]
