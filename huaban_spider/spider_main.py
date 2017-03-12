import json
import os
import re

from urllib import request


class HuaBanCrawler(object):
    def __init__(self):
        # 设置存放路径以及根url
        self.homeUrl = "http://huaban.com/boards/3191393"
        self.h = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/56.0.2924.87 Safari/537.36 '
        }
        self.images = []
        if not os.path.exists("./images"):
            os.makedirs("./images")

    def get_image_info(self, num=30):
        # 得到图片信息 ，存到数组中
        self.__process_data(self.__load_homePage())
        while len(self.images) <= num:
            print("当前获取到的数量：" + str(len(self.images)))
            self.__process_data(self.load_more(self.images[-1]["id"]))
        return self.images

    def down_images(self):

        print("开始下载图片，共：{0} 张".format(len(self.images)))
        for num, i in enumerate(self.images):
            print("下载第{0}张：{1}....".format(num + 1, i['id']))
            try:
                response = request.urlopen(i["url"], timeout=10)
                if response.getcode() != 200:
                    return None
            except:
                print('下载异常')
                return None
            imageName = os.path.join("./images", i["id"] + "." + i["type"])
            self.__save_image(imageName, response.read())

    def __process_data(self, htmlPage):
        # 从html提取信息
        prog = re.compile(r'app\.page\["board"\].*')
        appPins = prog.findall(htmlPage)
        if not appPins:
            return None
        appPins = appPins[0].split('app.page["board"] = ')[-1]
        result = json.loads(appPins[:-1])
        for i in result['pins']:
            info = {}
            info['id'] = str(i['pin_id'])
            info['url'] = "http://img.hb.aicdn.com/" + i["file"]["key"] + "_fw658"
            if 'image' == i["file"]["type"][:5]:
                info['type'] = i["file"]["type"][6:]
            else:
                info['type'] = 'NoName'
            self.images.append(info)

    def __save_image(self, imageName, content):
        # 保存图片
        with open(imageName, 'wb') as fp:
            fp.write(content)

    def __load_homePage(self):
        # 加载第一页
        req = request.Request(self.homeUrl, headers=self.h)
        return request.urlopen(req).read().decode('UTF-8')

    def load_more(self, lastId):
        # ajax加载更多
        newUrl = self.homeUrl + "?izzi2w9s&max=" + lastId + "&limit=20&wfl=1"
        req = request.Request(newUrl, headers=self.h)
        return request.urlopen(req).read().decode('UTF-8')


if __name__ == '__main__':
    hc = HuaBanCrawler()
    hc.get_image_info(200)
    print('解析完成，开始下载...')
    hc.down_images()
