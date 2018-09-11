import psutil
from pywinauto.application import Application


def check_process():
    ''' Searches for running World of Warcraft instance within
        list of currently running processes.
            RETURNS:        running (Boolean) '''
    print('[+] Checking for WoW Instance..')
    wow_process_names = ["World of Warcraft", "WorldOfWarcraft", "Wow.exe"]
    running = False
    # Check for process name match in wow_process_names
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if any(p.name() in s for s in wow_process_names):
            print(f'Found Instance: {p.name()}')
            running = True
    return running

def connect_app(path_to_app):
    ''' Connects to World of Warcraft instance at file location.
            ARGS:       path_to_app (Path to application on file system)
            RETURNS:    app (pywinauto.Application object) or None '''
    try:
        # Attach Python to World of Warcraft instance
        app = Application().connect(path=path_to_app)
    except (ProcessNotFound, AppNotConnected) as err:
        print(f'[!] Could not establish connection to \
        {path_to_app}:\n\t{err}')
    # If connection is successful, return app object
    if app:
        print(f'[+] Connected to application at:\n\t{path_to_app}')
        return app
    else:
        return None

def get_app_pos(app_object):
    ''' Retrieve the app left, top, right, and bottom edge coordinates.
            ARGS:       app_object (pywinauto.Application Object)
            RETURNS:    tuple(LEFT, TOP, RIGHT, BOTTOM) '''
    position = app_object.WorldOfWarcraft.rectangle()
    return position

def press_key(app_object, hotkey):
    ''' Press desired hotkey(s) within an app instance.
            ARGS:       app_object (pywinauto.Application Object)
                        hotkey (string) '''
    app_object.WorldOfWarcraft.type_keys(str(hotkey))
    print(f'[+] Key(s) Pressed: "{hotkey}"')
