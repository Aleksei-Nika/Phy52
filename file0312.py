import requests
import json
import os

API_URL = "https://api.jamendo.com/v3.0/tracks/"
LIMIT = 10
MOOD_TAGS = {
    "1": ("радостное", "pop"),
    "2": ("спокойное", "chill"),
    "3": ("энергичное", "rock"), 
    "4": ("грустное", "ambient"), 
    "5": ("сосредоточенное", "classical"),
}
CLIENT_ID = '25aece0e'

def requst_tracks(params):
    default_params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'limit': LIMIT,
        'audioformat': 'mp31'
    }
    full_params = {**default_params, **params}
    try:
        response = requests.get(API_URL, params = full_params)
        response.raise_for_status()
        data = response.json()
        if data["headers"]['status'] == "success":
            return data['results']
        else:
            print(f'Error: {data['headers']['error_massege']}')
            return []
    except requests.exeptions.RequstException as e:
        print(e)
        return []
    except json.JSONDecodeError:
        print('ошибка обработки ответов')
        return []
    
def display_tracks_get_choice(tracks):
    if not tracks:
        print('Треки не найдены')
        return None
    print('Найдены композиции: ')
    display_list = []
    for i, track in enumerate(tracks):
        title = track.get('name', 'название неизвестно')
        artist = track.get('artist_name', 'неизвестный исполнитель')
        print(f'{i+1}. {title} - {artist}')
        display_list.append(track)
    print('М - чтобы вернуться в главное меню')
    while True:
        choise = input(f'Введите номер композиции или "М": ').strip().lower()
        if choise == 'm' or choise == 'м':
            return None
        try:
            t_i = int(choise) - 1
            if 0 <= t_i < len(display_list):
              return display_list[t_i]
            else:
                print('Введите коректный номер композиции')
        except ValueError:
            print('введите номер или "М"')

def search_by_name():
    query = input('\nВведите название композиции или артиста: ').strip()
    if not query:
        print('запрос не может быть пустым')
        return
    params = {'name' : query}
    tracks = requst_tracks(params)
    if tracks:
        selected_track = display_tracks_get_choice(tracks)
        handle_track(selected_track)

def select_by_mood():
    for key, (mood, tag) in MOOD_TAGS.items():
        print(f'{key}. {mood}')
    print('М - чтобы вернуться в главное меню')
    while True:
        choise = input('выберите номер или "М": ').strip().lower()
        if choise == 'm' or choise == 'м':
            return
        if choise in MOOD_TAGS:
            mood_name, tag = MOOD_TAGS[choise]
        params = {'tags': tag}
        tracks = requst_tracks(params)
        if tracks:
            selected_track = display_tracks_get_choice(tracks)
            handle_track(selected_track)
        break
    else:
        print('Введите число или из списка или "М"')

def handle_track(track):
    if track is None:
        return
    download_link = track.get('audiodownload')
    if download_link:
        print('Ссылка на трек: ')
        print(download_link)
    else:
        print('ссылка недоступна')
    input('нажмите enter чтобы вернуться в главное меню')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Выберите действие:')
        print('1. Поиск по названию/исполнителю')
        print('2. Подборка по настроению')
        print('0. Выход и приложения')
        choise = input('Ваш выбор: ').strip()
        if choise == '1':
            search_by_name()
        elif choise == '2':
            select_by_mood()
        elif choise == '0':
            break
        else:
            print('некорректный выбор')
            input('нажмите enter чтобы продолжить')

main()