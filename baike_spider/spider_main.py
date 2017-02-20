# 调度器，主入口
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager


class SpiderMain(object):
    # 分别对应：url管理器，下载器，分析/解析器，输出文件夹
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        # 先判断是否有新的url，然后获取新的url，进行下载、分析
        # 分析出价值数据和新的url，进行各种的归档
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('当前爬取第%s个连接' % count)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count >= 10:
                    break
                count += 1
            except:
                print('此链接爬取失败')

        # 输出数据
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/link?url=5SzXMk31CjoYkzMyTm12cXrBlRDmjSjYjzMUj--tOLKWJ1M0ttLY5sZjSwmslSF1PhaZX2zLxDviEnRVgbf5DJMS-ROzo2zBU3Xhm6J0e-3'
    # 创建对象，运行爬虫
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
