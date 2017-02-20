from urllib import request


# 网页下载器

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        try:
            response = request.urlopen(url,timeout=10)
            if response.getcode() != 200:
                return None
            return response.read()
            # return response.read().decode('UTF-8')  Py3中默认是u8
        except:
            print('下载异常')
            return None
