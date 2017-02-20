class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write("<body>")
        fout.write("<table border='1' cellpadding='0' cellspacing='0'>")

        # py默认编码ASCI
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data["title"])
            # py3中。默认编码已经是u8不需要
            # fout.write("<td>%s</td>" % data["summary"].encode("UTF-8"))
            fout.write("<td>%s</td>" % data["summary"])
            fout.write("<td>%s</td>" % data["info"])
            fout.write("<td>%s</td>" % data["no"])
            fout.write("<td>%s</td>" % data["url"])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
