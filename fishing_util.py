import pywinauto
from datetime import datetime,timedelta

def cast(coords=None):
    ''' Casts the fishing pole by clicking the middle mouse button (scrollwheel)
        at specified coordinates and returns the time of the cast.
            ARGS:       (optional) coords (tuple (X,Y)) 
            RETURNS:    timestamp (datetime object) '''
    timestamp = datetime.now()
    pywinauto.mouse.wheel_click((coords if coords else (0,0)))
    print(f'Middle Click at {coords if coords else (0,0)}')
    return timestamp

def click(coords=None):
    ''' Clicks the left mouse button at specified coordinates and returns 
        the time of the click.
            ARGS:       (optional) coords (tuple (X,Y)) 
            RETURNS:    timestamp (datetime object) '''
    timestamp = datetime.now()
    pywinauto.mouse.click(button='left', coords=(coords if coords else (0,0)))
    print(f'Left Click at {coords if coords else (0,0)}')
    return timestamp

def check_new_cast(new_cast_threshold, last_cast_time, last_coords, current_coords):
    ''' Checks if more than 3 seconds have passed since the last cast, 
        and then checks to see if the x coordinate of the bobber is more than
        new_cast_threshold away from its previous location.
            ARGS:       new_cast_threshold (int)
                        last_cast_time (datetime object)
                        last_coords (tuple (X,Y))
                        current_coords (tuple (X,Y))
            RETURNS:    new_cast (boolean) '''
    new_cast = False
    # Check if 3 seconds have passed
    timestamp = datetime.now()-timedelta(seconds=3)
    if last_cast_time < (timestamp):
        last_x,last_y = last_coords
        new_x,new_y = current_coords
        # Check if x coord has changed by more than new_cast_threshold
        if last_x > (new_x + new_cast_threshold) or last_x < (new_x - new_cast_threshold):
            new_cast = True
    return new_cast
