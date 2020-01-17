start_msg_to_user = '''Привет, это Stepik Media, портал видео посвященных программированию.
Введите 1, чтобы посмотреть видео;
Введите 2, чтобы посмотреть плейлист;
Введите 0 или exit, чтобы выйти.\n'''

videos = {
    0: {"id": 0,    "title": "Алгоритмы на Python 3. Лекция №1",                                    "video_link": "https://www.youtube.com/watch?v=KdZ4HF1SrFs&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=1"},
    1: {"id": 1,    "title": "Алгоритмы на Python 3. Лекция №2",                                    "video_link": "https://www.youtube.com/watch?v=ZgSx3yH7sJI&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=2"},
    2: {"id": 2,    "title": "Алгоритмы на Python 3. Лекция №3",                                    "video_link": "https://www.youtube.com/watch?v=b8m9uRMpKJk&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=3"},
    3: {"id": 3,    "title": "Алгоритмы на Python 3. Лекция №4",                                    "video_link": "https://www.youtube.com/watch?v=DvsCUI5FNnI&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=4"},
    4: {"id": 4,    "title": "Алгоритмы на Python 3. Лекция №5",                                    "video_link": "https://www.youtube.com/watch?v=3I6OjxoeSS8&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=5"},
    5: {"id": 5,    "title": "Уроки Python для начинающих | #1 - Программирование на Python",       "video_link": "https://www.youtube.com/watch?v=n0xtO0x81cg&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu"},
    6: {"id": 6,    "title": "Уроки Python для начинающих | #2 - Установка среды разработки",       "video_link": "https://www.youtube.com/watch?v=_fDwlrrDkZc&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=2"},
    7: {"id": 7,    "title": "Уроки Python для начинающих | #3 - Первая программа (синтаксис)",     "video_link": "https://www.youtube.com/watch?v=Q7ccXmziG-I&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=3"},
    8: {"id": 8,    "title": "Уроки Python для начинающих | #4 - Переменные",                       "video_link": "https://www.youtube.com/watch?v=j8AePyuLw38&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=4"},
    9: {"id": 9,    "title": "Уроки Python для начинающих | #5 - Условные операторы",               "video_link": "https://www.youtube.com/watch?v=tCSD-zNVkO4&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=5"},
    10: {"id": 10,  "title":   "Git - для новичков - #1 - основы",                                  "video_link": "https://www.youtube.com/watch?v=PEKN8NtBDQ0&list=PLY4rE9dstrJyTdVJpv7FibSaXB4BHPInb&index=1"},
    11: {"id": 11,  "title":    "Git - для новичков - #2 - первые коммиты",                         "video_link": "https://www.youtube.com/watch?v=9d5bJc8o7MA&list=PLY4rE9dstrJyTdVJpv7FibSaXB4BHPInb&index=2"},
    12: {"id": 12,  "title":    "Git - для новичков - #3 - работаем с github",                      "video_link": "https://www.youtube.com/watch?v=vFj2-bKGwkw&list=PLY4rE9dstrJyTdVJpv7FibSaXB4BHPInb&index=3"},
}

playlists = {
    0: {"title": "Алгоритмы на Python 3", "videos": [0, 1, 2, 3, 4]},
    1: {"title": "Уроки Python для начинающих", "videos": [5, 6, 7, 8, 9]},
    2: {"title": "Git - для новичков", "videos": [10, 11, 12]}
}

while True:
    user_command = input(start_msg_to_user)

    if user_command == '1':
        print("Выберите, какое видео, вы хотите посмотреть\n")
        for var in videos:
            print("{}.".format(videos[var]["id"]+1), videos[var]["title"])
        user_command = int(input())
        if (user_command - 1) in videos:
            print("Ваше видео: \n",
                  videos[user_command - 1]["title"]+"\n",
                  videos[user_command - 1]["video_link"]+"\n",
                  "Приятного просмотра!", end = "\n\n")
        else: print("Такого видео у нас нет, всего хорошего!", end = "\n\n")

    elif user_command == '2':
        print("Выберите, какой плейлист, вы хотите посмотреть\n")
        for var in playlists:
            print("{}.".format(var+1), playlists[var]["title"], "({} видео)".format(len(playlists[var]["videos"])))
        user_command = int(input())
        if (user_command - 1) in playlists:
            print(playlists[user_command-1]["title"]+":\n")
            cnt_numb = 1
            for var in playlists[user_command-1]["videos"]:
                print("{}.".format(cnt_numb), videos[var]["title"]+"\n", videos[var]["video_link"])
                print()
                cnt_numb += 1
            print("Приятного просмотра!", end = "\n\n")
        else: print("Такого плейлиста у нас нет, всего хорошего!", end = "\n\n")

    elif user_command == '0' or user_command == 'exit':
        break