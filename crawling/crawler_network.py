import requests
import json


def get_url_image(url, web_server):
    res = requests.get(url)
    if res.status_code == 200:
        list_url = []
        obj = res.json()
        data = obj['preview']['imagePlaceHoldersPreview']
        for element in data:
            if element['imageLibraryId'] is not None:
                count = 1
                while True:
                    path_url = f'{web_server}/api/Libraries/{element["imageLibraryId"]}/Elements/Position/{count}'
                    path = requests.get(path_url).json()
                    if path is None:
                        break
                    link = f'{web_server}{path["Path"]}'
                    if link not in list_url:
                        list_url.append(link)
                    count += 1

                pass
            else:
                for index, path in json.loads(element['dynamicImagesPath']):
                    link = f'{web_server}{path}'
                    if link not in list_url:
                        list_url.append(link)
            print(f'{len(list_url)} url complete')
        return list_url
    else:
        print(res.status_code)

link = 'https://app.customily.com/api/Product/GetProduct?productId=557b1737-37ec-46e4-be17-2365f550a400&clientVersion=3.6.9'
web = 'https://app.customily.com'
list = get_url_image(link, web)
for x in list:
    print(x)
print('len:', len(list))
