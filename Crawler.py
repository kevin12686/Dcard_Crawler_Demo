import os, requests, json


def dcard_picture(dcard_api_url='https://www.dcard.tw/_api/', picture_url='https://i.imgur.com/',
                  forums='forums/pet/posts?popular=false', save_dir='./media/',
                  keyword='', limit=5):
    if os.path.exists(save_dir) is False:
        os.mkdir(save_dir)
    count = 0
    json_list = json.loads(requests.get(dcard_api_url + forums).text)
    target_id = list()
    for each in json_list:
        if keyword == '' or each['title'].find(keyword) != -1:
            target_id += [str(each['id'])]
    for each in target_id:
        if count >= limit:
            break
        url_list = json.loads(requests.get(dcard_api_url + 'posts/' + each).text)['media']
        for obj in url_list:
            url = obj['url']
            name = url.split(picture_url)[1]
            if limit == -1 or count < limit:
                count += 1
                print('Downloading ' + name)
                with open(save_dir + name, 'wb') as file:
                    file.write(requests.get(url).content)
            else:
                break
    print('Finish')


if __name__ == '__main__':
    dcard_picture(keyword='')
