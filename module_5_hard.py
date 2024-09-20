from time import sleep


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title              # заголовок видео
        self.duration = duration        # длина видео
        self.time_now = 0               # время текущей остановки видео
        self.adult_mode = adult_mode    # возврастное ограничение


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname    # логин
        self.password = password    # пароль
        self.age = age              # возраст


class UrTube:
    def __init__(self):
        self.videos = []            # список видео
        self.users = []             # список пользователей
        self.current_user = None    # текущий пользователь

    def add(self, *args):                               # добавление новых видео
        for i in args:                                  # перебираем список переданных видео
            is_video_exists = False                     # определяет наличие видео в списке
            for j in range(len(self.videos)):           # перебираем список существующих видео
                if i.title == self.videos[j].title:     # если видео существует
                    is_video_exists = True              # is_video_exists присваиваем значение True
                    break                               # завершаем цикл
            if not is_video_exists:                     # если видео нет, добавляем его в список
                self.videos.append(i)

    def get_videos(self, title_video):                  # поиск видео
        find_video = []                                 # создаем пустой список для найденных видео
        for i in range(len(self.videos)):               # перебираем список существующих видео
            if str(title_video).lower() in self.videos[i].title.lower():
                find_video.append(self.videos[i].title)
        return find_video                               # возвращаем список найденных видео

    def log_in(self, nickname, password):
        for i in range(len(self.users)):                # перебираем список пользователей
            if nickname == self.users[i].nickname and hash(password) == self.users[i].password:
                self.current_user = self.users[i]
                break

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        for i in range(len(self.users)):            # перебираем сохраненных пользователей
            if nickname == self.users[i].nickname:  # выходим если пользователь существует
                print(f'Пользователь {nickname} уже существует')
                return
        self.log_out()
        self.users.append(User(nickname, hash(password), age))  # добавляем нового пользователя
        self.log_in(nickname, password)

    def watch_video(self, title):
        if not self.current_user:       # проверяем наличие зарегистрироанного пользователя
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in range(len(self.videos)):                   # перебираем список видео
                if title == self.videos[i].title:               # если видео найдено
                    if self.videos[i].adult_mode:               # проверяем возрастное ограничение
                        if self.current_user.age < 18:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                            return
                    for time_v in range(self.videos[i].time_now, self.videos[i].duration):
                        self.videos[i].time_now = time_v+1          # показываем видео от time_now до duration
                        print(self.videos[i].time_now, end=' ')     # выводим секунды в одну строку
                        sleep(1)                                    # задержка
                    self.videos[i].time_now = 0                     # сбрасываем время просмотра
                    print('Конец видео')
                    return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
