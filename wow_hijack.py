import psutil
from pywinauto.application import Application


def check_process():
    print('[+] Checking for WoW Instance..')
    wow_process_names = ["World of Warcraft", "WorldOfWarcraft", "Wow.exe"]
    running = False
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if any(p.name() in s for s in wow_process_names):
            print(f'Found Instance: {p.name()}')
            running = True
    return running

def connect_app(path_to_app):
    wow_running = check_process()
    if wow_running:
        try:
            # Use if the application needs to be started
            app = Application().connect(path=path_to_app)
        except (ProcessNotFound, AppNotConnected) as err:
            print(f'[!] Could not establish connection to \
            {path_to_app}:\n\t{err}')
        if app:
            print(f'[+] Connected to application at:\n\t{path_to_app}')
            return app
        else:
            return None

def get_app_pos(app_object):
    position = app_object.WorldOfWarcraft.rectangle()
    return position

def press_key(app_object, hotkey):
    app_object.WorldOfWarcraft.type_keys(str(hotkey))
    print(f'Key(s) Pressed: "{hotkey}"')
