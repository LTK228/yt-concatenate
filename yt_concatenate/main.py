from yt_concatenate.steps.get_video_list import GetVideoList
from yt_concatenate.steps.step import StepException

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

steps = [
    GetVideoList(),
    DownCaption(),
    SearchForWord(),
    EditVideo(),
]

for step in steps:
    try:
        step.process()
    except StepException as e:
        print('Exception happened', e)
        break                            # 只要出錯，跳出迴圈！