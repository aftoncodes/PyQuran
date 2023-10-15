import requests
import json
import io
from threading import Thread
import pyglet

selected_reciter = []
surah_selection = 0
cls = lambda: print("\033c\033[3J", end='')


def select_reciter():
    global selected_reciter
    cls()
    print("""╔═╗─╔══╗───╔╗
║╬╠╦╣╔╗╠╦╦╦╣╠═╗╔═╦╗
║╔╣║║╚╝║║║╔╩╣╬╚╣║║║
╚╝╠╗╠═╗╠═╩╝─╚══╩╩═╝ v1.0 - With <3 by aftoncodes
──╚═╝─╚╝""")
    while True:
        url = "https://api.quran.com/api/v4/resources/recitations"

        payload = {}
        headers = {
            'Accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Create a dictionary to store reciters and their corresponding IDs
            reciters_dict = {}

            # Populate the dictionary with reciters and their IDs
            for i, recitation in enumerate(data['recitations'], start=1):
                reciter_name = recitation['reciter_name']
                reciters_dict[i] = {'name': reciter_name, 'id': recitation['id']}
                i_formatted = str(i).zfill(2)
                print(f"[{i_formatted}] {reciter_name: <30} {recitation['style'] if recitation['style'] else 'Not available'}")

            # Take user input
            selection = input("\nEnter the number corresponding to the reciter: ")

            # Check if the selection is valid
            if selection.isdigit():
                selection = int(selection)
                if 1 <= selection <= len(reciters_dict):
                    selected_reciter = reciters_dict[selection]
                    cls()
                    print("""╔═╗─╔══╗───╔╗
║╬╠╦╣╔╗╠╦╦╦╣╠═╗╔═╦╗
║╔╣║║╚╝║║║╔╩╣╬╚╣║║║
╚╝╠╗╠═╗╠═╩╝─╚══╩╩═╝ v1.0 - With <3 by aftoncodes
──╚═╝─╚\n""")
                    print(f"Selected reciter: {selected_reciter['name']}\n")
                    break
                else:
                    cls()
                    print("Invalid selection.")
            else:
                cls()
                print("Invalid input. Please enter a valid number.")

        else:
            print(f"Request failed with status code {response.status_code}.")
    


surah_list = """[001] Al-Fātiĥah      [002] Al-Baqarah      [003] Āli `Imrān      [004] An-Nisā
[005] Al-Mā'idah      [006] Al-'An`ām       [007] Al-'A`rāf       [008] Al-'Anfāl
[009] At-Tawbah       [010] Yūnus           [011] Hūd             [012] Yūsuf
[013] Ar-Ra`d         [014] Ibrāhīm         [015] Al-Ĥijr         [016] An-Naĥl
[017] Al-'Isrā        [018] Al-Kahf         [019] Maryam          [020] Ţāhā
[021] Al-'Anbyā       [022] Al-Ĥajj         [023] Al-Mu'minūn     [024] An-Nūr
[025] Al-Furqān       [026] Ash-Shu`arā     [027] An-Naml         [028] Al-Qaşaş
[029] Al-`Ankabūt     [030] Ar-Rūm          [031] Luqmān          [032] As-Sajdah
[033] Al-'Aĥzāb       [034] Saba            [035] Fāţir           [036] Yā-Sīn
[037] Aş-Şāffāt       [038] Şād             [039] Az-Zumar        [040] Ghāfir
[041] Fuşşilat        [042] Ash-Shūraá      [043] Az-Zukhruf      [044] Ad-Dukhān
[045] Al-Jāthiyah     [046] Al-'Aĥqāf       [047] Muĥammad        [048] Al-Fatĥ
[049] Al-Ĥujurāt      [050] Qāf             [051] Adh-Dhāriyāt    [052] Aţ-Ţūr
[053] An-Najm         [054] Al-Qamar        [055] Ar-Raĥmān       [056] Al-Wāqi`ah
[057] Al-Ĥadīd        [058] Al-Mujādila     [059] Al-Ĥashr        [060] Al-Mumtaĥanah
[061] Aş-Şaf          [062] Al-Jumu`ah      [063] Al-Munāfiqūn    [064] At-Taghābun
[065] Aţ-Ţalāq        [066] At-Taĥrīm       [067] Al-Mulk         [068] Al-Qalam
[069] Al-Ĥāqqah       [070] Al-Ma`ārij      [071] Nūĥ             [072] Al-Jinn
[073] Al-Muzzammil    [074] Al-Muddaththir  [075] Al-Qiyāmah      [076] Al-'Insān
[077] Al-Mursalāt     [078] An-Naba         [079] An-Nāzi`āt      [080] `Abasa
[081] At-Takwīr       [082] Al-'Infiţār     [083] Al-Muţaffifīn   [084] Al-'Inshiqāq
[085] Al-Burūj        [086] Aţ-Ţāriq        [087] Al-'A`lá        [088] Al-Ghāshiyah
[089] Al-Fajr         [090] Al-Balad        [091] Ash-Shams       [092] Al-Layl
[093] Ađ-Đuĥaá        [094] Ash-Sharĥ       [095] At-Tīn          [096] Al-`Alaq
[097] Al-Qadr         [098] Al-Bayyinah     [099] Az-Zalzalah     [100] Al-`Ādiyāt
[101] Al-Qāri`ah      [102] At-Takāthur     [103] Al-`Aşr         [104] Al-Humazah
[105] Al-Fīl          [106] Quraysh         [107] Al-Mā`ūn        [108] Al-Kawthar
[109] Al-Kāfirūn      [110] An-Naşr         [111] Al-Masad        [112] Al-'Ikhlāş
[113] Al-Falaq        [114] An-Nās"""

def fetch_audio_url(reciter_id, chapter_id):
    url = f"https://api.quran.com/api/v4/chapter_recitations/{reciter_id}"
    payload = {}
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        audio_files = data.get('audio_files', [])
        for audio in audio_files:
            if audio['chapter_id'] == chapter_id:
                return audio['audio_url']
        return f"Audio URL not found for chapter id: {chapter_id}"
    else:
        return f"Failed to fetch audio data for reciter id: {reciter_id}"
    

def select_surah():
    global surah_selection
    global selected_reciter
    print(surah_list)
    while True:
        try:
            surah_selection = int(input("\nEnter the number corresponding to the surah: "))
            if surah_selection >= 1 and surah_selection <= 114:
                print(fetch_audio_url(selected_reciter['id'], surah_selection))
                break
            else:
                cls()
                print(f"Selected reciter: {selected_reciter['name']}\n")
                print(surah_list)
                print(f"\nInvalid selection: Surah #{surah_selection} does not exist.")
        except ValueError:
            cls()
            print(f"Selected reciter: {selected_reciter['name']}\n")
            print(surah_list)
            print(f"\nNaN Error: Input was not a number")

def get_whole_quran():
    global selected_reciter
    url = f"https://api.quran.com/api/v4/quran/recitations/{selected_reciter['id']}"
    payload = {}
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        audio_files = data.get('audio_files', [])
        for audio in audio_files:
            r = requests.get(f'https://verses.quran.com/{audio["url"]}').content
            fileobject = io.BytesIO(r)
            music = pyglet.media.load("temp", file=fileobject)
            player = music.play()
            player.on_eos = pyglet.app.exit

            def input_test():
                input("[Press Enter to exit]")
                pyglet.app.exit()

            thread = Thread(target = input_test)

            thread.start()
            break

            pyglet.app.run()





    

if __name__ == "__main__":
    select_reciter()
    surah_or_whole = int(input("""Whole Qur'an or specific surah?
[1] Whole
[2] Surah
[?]: """))
    if surah_or_whole == 1:
        get_whole_quran()
    elif surah_or_whole == 2:
        select_surah()
        print(f"Getting chapter #{surah_selection}, this may take a while for longer chapters...")
        r = requests.get(fetch_audio_url(selected_reciter['id'], surah_selection)).content
        fileobject = io.BytesIO(r)
        music = pyglet.media.load("temp", file=fileobject)
        player = music.play()
        player.on_eos = pyglet.app.exit

        def input_test():
            input("[Press Enter to exit]")
            pyglet.app.exit()

        thread = Thread(target = input_test)

        thread.start()

        pyglet.app.run()