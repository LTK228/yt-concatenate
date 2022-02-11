from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):               # 1. 繼承 Step 抽象類別
    def process(self, inputs, data):        # 2. 覆寫 抽象方法
        for url in data:
            source = YouTube(url)

            # 下載字幕
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)

            # 將字幕存在檔案裡
            # save the caption to a file named Output.txt
            text_file = open("Output.txt", "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

            break                           # 只取第一個字幕，當作測試
