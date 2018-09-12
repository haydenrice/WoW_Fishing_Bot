# WoW_Fishing_Bot

### Description:
  A fishing bot for World of Warcraft that will automate casting, finding your bobber, and clicking the bobber when a fish is on.


### Setup:
  #### 1. Change WoW Settings
  
  * Change to windowed mode.
      - I have found that windowed mode generally works better for whatever reason.
  * Lower graphics settings to 1
      - Finding the bobber works by filtering out parts of the video feed. The less clutter, the better.
  * Make sure liquid detail is set to 'Low'
      - Filtering works better when set to low as it tends to make the water surface more opaque (less clutter underwater).
  
![WoW Settings](https://github.com/raidensan91/WoW_Fishing_Bot/blob/master/var/Settings.PNG)

  #### 2. Remove WoW Interface
  
  * The WoW interface can be removed in-game by pressing 'ALT + Z'.
      - This removes more clutter so that the program has an easier time recognizing the bobber.
##### Enabled:
![UI Enabled](https://github.com/raidensan91/WoW_Fishing_Bot/blob/master/var/UI_Enabled.PNG)
##### Disabled:
![UI Disabled](https://github.com/raidensan91/WoW_Fishing_Bot/blob/master/var/UI_Disabled.PNG)

  #### 3. Change Camera Angle
  
  * The bot utilizes the bottom 3/5 of the active game window to monitor for the bobber. Angle your screen as shown for best results:
  
![Camera Angle](https://github.com/raidensan91/WoW_Fishing_Bot/blob/master/var/Camera_Angle.PNG)
