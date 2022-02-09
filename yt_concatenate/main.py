from yt_concatenate.pipeline.steps.get_video_list import GetVideoList
from yt_concatenate.pipeline.steps.step import StepException

from yt_concatenate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

"""
g = GetVideoList()
g.process
d = DownCaption()
d.process
s = SearchForWord()
s.process
e = EditVideo()
e.process
"""


def main():
    inputs = {
        'CHANNEL_ID': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
        # DownCaption(),
        # SearchForWord(),
        # EditVideo(),
    ]

    p = Pipeline(steps)  # init 的時候
    p.run(inputs)  # 執行 class Pipeline 的 def run():


if __name__ == '__main__':
    main()
