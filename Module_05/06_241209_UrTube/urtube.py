from time import sleep


class User():
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname, self.password, self.age = nickname, password, age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'{self.nickname}, {self.age}y.o.'


class Video():
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title, self.duration = title, duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.__str__()

    def playing_process(self):
        for sec in range(self.time_now+1, self.duration+1):
            print(sec, end=' ', flush=True)
            sleep(1)
            self.time_now = sec
        self.time_now = 0
        print('Конец видео')


class UrTube():
    def __init__(self):
        self.users, self.videos, self.current_user = list(), list(), None

    def get_user(self, nickname: str) -> User:
        for user in self.users:
            if user.nickname.lower() == nickname.lower():
                return user

    def get_video(self, title: str) -> Video:
        for video in self.videos:
            if video.title.lower() == title.lower():
                return video

    def get_videos(self, request: str) -> list:
        result = list()
        for video in self.videos:
            if video.title.lower().__contains__(request.lower()):
                result.append(video)
        return result

    def log_in(self, nickname: str, password: str):
        user = self.get_user(nickname)
        if user != None:
            if user.password == hash(password):
                self.current_user = user
                return

        print('Неверное имя пользователя или пароль')

    def register(self, nickname: str, password: str, age: int):
        if self.get_user(nickname) != None:
            print(f'Пользователь {nickname} уже существует')
            return

        new_user = User(nickname.lower(), hash(password), age)
        self.users.append(new_user)
        self.current_user = self.users[-1]

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if self.get_video(video.title) == None:
                self.videos.append(video)

    def watch_video(self, title: str):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                video.playing_process()
                break
