import cv2, pywinauto, random, screen_cap, time, wow_hijack


# Path to WoW
PATH = "D:\Games\Blizzard\World of Warcraft\Wow.exe"
# OPTIONS
TRACKBARS = False

def bobber_screen_coords(bobber_location):
    screen_coords = (bobber_location[0], int(bobber_location[1]+(app_height/5*3)))
    return screen_coords

def main():
    ''' To Do
            - Restart the process
                + Generate random interval to restart
                    random.uniform(FLOAT, FLOAT) '''
    wow_running = wow_hijack.check_process()
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
            adjusted_window = (
            app_position.left, (app_position.top+(app_height/5*3)),
            app_position.right, app_position.bottom)
        except:
            print(f'[!] Can\'t connect to WoW instance.')
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
    # Distance in either x or y greater than this
    # won't trigger the catching method
    new_cast_threshold = 30
    while(True):
        try:
            # Retrieve video output and bobber location
            output, bobber_location = \
            screen_cap.generate_window(*adjusted_window)
            # If a bobber location is found
            if bobber_location != None:
                # Add to x if window doesn't start at X=0
                bobber_location_x = (bobber_location[0]+app_position.left)
                # Check for variance in Y coords to see if bobber dips
                upper_threshold = last_bobber_location[1] + 7
                lower_threshold = last_bobber_location[1] - 5
                # Compare Y coordinates
                if bobber_location[1] > upper_threshold or \
                bobber_location[1] < lower_threshold:
                    # If X coord changes more than new_cast_threshold
                    # no fish on the line yet
                    if last_bobber_location[0] > \
                    bobber_location[0] + new_cast_threshold or \
                    last_bobber_location[0] < \
                    bobber_location[0] - new_cast_threshold:

                        # Debug
                        print('New Cast')

                    else:
                        # This is where the code will go to catch the fish
                        # @ given X,Y coords, and then press the button to
                        # restart the fishing process

                        # Debug
                        print('Fish On')

                        # Potentially get this on a different thread
                        # Sleep for random amt of time
                        time.sleep(random.uniform(0.8,1.5))
                        # Get screen coords from window coords for mouse click
                        coords = bobber_screen_coords()
                        # Click at selected coordinates
                        # pywinauto.mouse.click(button='left', coords=(coords[0], coords[1]))

                        # Debug
                        print(bobber_location, last_bobber_location)
                        fish_on = True

                # Update last known bobber location
                last_bobber_location = bobber_location
            # Show video feed
            cv2.imshow('Fisherman', output)
            # Exit key == 'q'
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
