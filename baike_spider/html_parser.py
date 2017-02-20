import re
import urllib.parse

from bs4 import BeautifulSoup


# 网页解析器

class HtmlParser(object):
    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            # 连接补全
            new_full_url = urllib.parse.urljoin(url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, url, soup):
        res_data = {'url': url}

        # class ="lemmaWgt-lemmaTitle-title"  标题
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # 简介
        # soup.find_all('div', class_='para', limit=1)
        summary_node = soup.find('div',class_='para')
        res_data['summary'] = summary_node.get_text()

        # 分类展示 basic-info cmn-clearfix
        other_node = soup.find('div', class_='basic-info cmn-clearfix')
        res_data['info'] = other_node.get_text()

        # 第一简介
        # other_node = summary_node.find_next('div',class_='para')
        other_node = soup.find_all('div',class_='para', limit=3)
        res_data['no'] = other_node[1].get_text() + other_node[2].get_text()

        return res_data
