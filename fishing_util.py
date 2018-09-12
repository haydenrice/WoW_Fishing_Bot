import pywinauto
from datetime import datetime,timedelta

def cast(coords=None):
    timestamp = datetime.now()
    pywinauto.mouse.wheel_click((coords if coords else (0,0)))
    print(f'Middle Click at {coords if coords else (0,0)}')
    return timestamp

def click(coords=None):
    timestamp = datetime.now()
    pywinauto.mouse.click(button='left', coords=(coords if coords else (0,0)))
    print(f'Left Click at {coords if coords else (0,0)}')
    return timestamp

def check_new_cast(last_cast_time, last_coords, current_coords):
    timestamp = datetime.now()-timedelta(seconds=3)
    new_cast = False
    new_cast_threshold = 20 # Pixels
    # Check if 3 seconds have passed
    if last_cast_time < (timestamp):
        last_loc_x = last_coords[0]
        last_loc_y = last_coords[1]
        new_loc_x = current_coords[0]
        new_loc_y = current_coords[1]
        # Check if x coord has changed by more than new_cast_threshold
        if last_loc_x > (new_loc_x + new_cast_threshold) or \
        last_loc_x < (new_loc_x - new_cast_threshold):
            new_cast = True
        # Check if y coord has changed by more than new_cast_threshold
        # elif last_loc_y > (new_loc_y + new_cast_threshold) or \
        # last_loc_y < (new_loc_y - new_cast_threshold):
        #     new_cast = True
    return new_cast
