import urllib.request
import json

from yt_concatenate.settings import API_KEY
from yt_concatenate.pipeline.steps.step import Step


class GetVideoList(Step):
    def process(self, inputs, data):                                              # inputs 是「字典」格式，目的是避免父類別 step.py 的參數過度延長。
        channel_id = inputs['CHANNEL_ID']

        base_video_url = 'https://www.youtube.com/watch?v='                 # 基底影片連結 (不用修改)
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'   # API endpoint: 向網站需求資料的連結

        # API 拿資料時使用的網址: API endpoint 加上 channel id，表示需要哪個頻道的影片，每個都是字典並透過 & 連接
        first_url = f'{base_search_url}key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url                                                     # 存成 url
        while True:
            inp = urllib.request.urlopen(url)                               # 透過 Python 內建套件 urllib.request，向 url 發送 request
            resp = json.load(inp)                                           # respond: 回傳結果

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)

            # 1. Too broad exception clause (捕捉錯誤的範圍太廣)
            # 2. 推估錯誤型別：從 first_url 的 maxResults=25 (一次最多取 25 個結果)，
            #    與 try: 的 pageToken (一頁一頁取資料，直到沒有為止 while True)
            # 3. 發生錯誤時才 break，錯誤是發生在 resp['nextPageToken']，resp 去找 nextPageToken 時錯誤 → 字典的 KeyError
            except KeyError:
                break

        print(len(video_links))                                             # 查看頻道內有幾個影片連結。
        print(video_links)                                                  # 頻道內的所有影片連結，以 list 裝起來。
        return video_links


# video_list = get_all_video_in_channel(CHANNEL_ID)
