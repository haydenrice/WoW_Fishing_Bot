import cv2, fishing_util, pywinauto, random, screen_cap, time, wow_hijack
from datetime import datetime,timedelta

PATH = "D:\\Games\\Blizzard\\World of Warcraft\\Wow.exe"
FISHING_ENABLED = False
TRACKBARS = False
SHOW_VIDEO_FEED = True
NEW_CAST_THRESHOLD = 20

def bobber_screen_coords(bobber_location, app_height, app_position):
    ''' Returns the bobber x,y screen coordinates in a tuple.
        Takes into account window x,y offset if not fullscreen.
            ARGS:       bobber_location (tuple(X,Y))
            RETURNS:    screen_coords (tuple(X,Y)) '''
    screen_coords = (int(bobber_location[0]+ app_position.left),int(bobber_location[1]+(app_height/5*3)))
    return screen_coords

def main():
    wow_running = wow_hijack.check_process(["World of Warcraft", "WorldOfWarcraft", "Wow.exe"])
    print(f'[+] Finding WoW application.')
    if wow_running:
        try:
            # Connect to WoW
            app = wow_hijack.connect_app(PATH)
            # Get window position and height
            app_position = wow_hijack.get_app_pos(app)
            app_height = app_position.height()
            # Fishing only requires the bottom 2/5 of the screen
            # Adjust the window to 2/5 of the height
            adjusted_window = (app_position.left,(app_position.top+(app_height/5*3)),app_position.right, app_position.bottom)
        except Exception as e:
            print(f'[!] Can\'t connect to WoW instance.: {e}')
            print('[!] Exiting.')
            exit()
    else:
        print(f'[!] Can\'t find WoW instance running.')
        print('[!] Exiting.')
        exit()
    # Set up trackbars ( if you want to )
    if TRACKBARS:
        screen_cap.setup_trackbars()
    # Arbitrary value
    last_bobber_location = (0,0)
    last_cast = datetime.now()
    while(True):
        try:
            # Retrieve video output and bobber location
            mask, output = screen_cap.generate_window(*adjusted_window)
            bobber_location = screen_cap.find_bobber(mask, output)
            if SHOW_VIDEO_FEED:
                cv2.imshow('FishingBot Feed', output)
            # If a bobber location is found
            if bobber_location:
                # If X coord changes more than new_cast_threshold
                new_cast = fishing_util.check_new_cast(NEW_CAST_THRESHOLD, last_cast,last_bobber_location, bobber_location)
                if new_cast:
                    print('[+] New cast detected.')
                else:
                    # Check for variance in Y coords to see if bobber dips
                    upper_threshold = last_bobber_location[1] + 7
                    lower_threshold = last_bobber_location[1] - 5
                    # Compare Y coordinates
                    if bobber_location[1] > upper_threshold or bobber_location[1] < lower_threshold:
                        # This is where the code will go to catch the fish
                        # @ given X,Y coords, and then press the button to
                        # restart the fishing process
                        if datetime.now() > (last_cast+timedelta(seconds=3)):
                            # Debug
                            print('[+] Fish On!')
                            if FISHING_ENABLED:
                                # Potentially get this on a different thread
                                # Sleep for random amt of time
                                time.sleep(random.uniform(0.8,2.15))
                                # Get screen coords from window coords for mouse click
                                coords = bobber_screen_coords(bobber_location,app_height,app_position)
                                # Click at selected coordinates
                                fishing_util.click(coords)
                                # Sleep for random amt of time
                                time.sleep(random.uniform(1.5, 3.3))
                                last_cast = fishing_util.cast(coords)
                # Update last known bobber location
                last_bobber_location = bobber_location
            # Exit key == 'q'
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
