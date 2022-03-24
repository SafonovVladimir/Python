import urllib.request

link = str(input('Введите адрес сайта: '))
# print(link)

def url_request(link):
    req = urllib.request.urlopen(link)
    # print(req)
    html = req.read()
    return html
