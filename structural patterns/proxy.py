import uuid
from abc import ABC

class Video(ABC):
    def __init__(self, id: int, url: str) -> None:
        self.id = id
        self.url = url

    def load(self) -> str:
        return f'Loading the video from the path: {self.url}.'
    
    def play(self) -> str:
        return f'Playing the data from a video with #ID: {self.id}.'

class ProxyVideo(ABC):
    def __init__(self, id: int, url: str) -> None:
        self.id = id
        self.url = url
        self.video = None

    def play(self) -> None:
        if not self.video:
            self.video = Video(self.id, self.url)
            print(self.video.load())

        print(self.video.play())
        print('\n')


class YouTube(ABC):
    def __init__(self) -> None:
        self.cache = dict()

    def play_video(self, name: str, url=None) -> None:
        if name not in self.cache:
            self.cache[name] = ProxyVideo(uuid.uuid4(), url)

        self.cache[name].play()

    def play_all_videos(self) -> None:
        print('Start loading all the cached video...')
        for proxy_video in list(self.cache.values()):
            proxy_video.play()



if __name__ == '__main__':
    youtube_platform = YouTube()
    youtube_platform.play_video('Band of Brothers Theme', 'https://www.youtube.com/watch?v=dcNUUCZ4y1U')

    youtube_platform.play_video('Band of Brothers Theme')
    youtube_platform.play_all_videos()