  # INSTRUCTIONS:
  # FOLLOW ALL OF THESE, IF YOU GET STUCK, DM ME
  
  ## [Watch video guide](https://www.youtube.com/watch?v=CNln4hB72wc&feature=youtu.be)

  
  ## STAGE 1 - Set up your gmail account
 ##### Purpose: 
 Allow the script access to read your emails to get the verification codes. Without this, it will not function
 
  1.  Go to https://console.cloud.google.com/apis/dashboard
  2.  In the blue bar at the top, click `Select a project` then `New Project`
  3.  Pick a name (something like 'MegaCreator')
  4.  In the left hand sidebar, go to `APIs and Services`
  5.  In this window, under the search bar click `+ ENABLE APIS AND SERVICES`
  6.  Search for `Gmail API` and then select Gmail API from the search results
  7.  Click `Enable` (if it's already enabled, click `Manage`)
  8.  Again on the left sidebar, go to `Credentials`
  9.  On the right hand side, click the white button `CONFIGURE CONSENT SCREEN`
  10. Choose `External` (Internal isn't available for free accounts) and `CREATE`
  11. Fill in this screen with App Name (Mega Accounts), your email from the dropdown, 
      And at the very bottom under `Developer contact information`, enter your email again

  12. Save and continue
  13. On the `OAuth consent screen`, click `Publish`
  14. Back on the `Credentials` tab from the left sidebar
  15. Under the search bar, click `+ CREATE CREDENTAILS`
  16. In the popup, choose `OAuth Client ID`
  17. Choose `Desktop App` as the application type
  18. Name it (anything you want), and click Create
  19. You now get a `Client ID` and `Client Secret`
     
### NEVER EVER EVER EVER give these to anyone. ONLY put them in this script.

  20. Click the *download* button to download a .json file, and name it `credentials.json`
  21. Put this file in the same folder as this script.

#### NOTE - on first run, your browser will open and ask you to authorise your gmail account. Make sure you choose your primary email from the list and make sure the name of the app is what you named it in step 18

#### YOU MAY GET A WARNING '`GOOGLE HASN'T VERIFIED THIS APP`' - Click '`Advanced`' at the bottom left, Then at the bottom, `Go to [name you chose in step 18]` e.g. `Go to Mega Accounts (unsafe)`
  Finally, choose `Continue'`


## STAGE 2 - Set up your system
   1. Download [this file](https://raw.githubusercontent.com/Troubled-Mind/Account-Creator/main/Mega-Account-Creator.py) and put it in a folder you can easily access
   2. Install the latest Python if you don't have it already
   3. In the folder this tool is in, download Megatools from your system
      Downloads can be found here: https://megatools.megous.com/builds/builds/
      Extract everything inside to the folder, and name it `megatools`
   4. Create a txt file called "emails" which you can put all of the emails in
      This text file should be in the SAME PLACE as Mega-ACcount-Creator.py
   5. Open command prompt/terminal in this folder and run the two commands below:    
      `pip install google-api-python-client`    
      `pip install oauth2client`    

      If you don't have pip, download this file below, and open command prompt to the folder it is in
      and run `python get-pip.py` 
      https://bootstrap.pypa.io/get-pip.py
  


## STAGE 3 - Set up the script
1. On line 94, set the name your account will use in mega. 
      All accounts share the same name. 
 2. On line 95, set the password you want to use for ALL mega accounts created
 3. On line 93, set the PATH to the megatools folder
 4. Open `emails` txt file and add the account emails you want creating *WITHOUT* @gmail.com
      Example file picture: https://i.imgur.com/zSECSzv.png

   5. Run the script `python Mega-Account-Creator.py` in the terminal
   6. Note- the script MAY stop at `Getting link from email`
      If this happens, simply stop and restart the script 
		(Stop by using "ctrl+c" and start by running the command again)


###         DO NOT MODIFY ANYTHING ELSE
.... unless 👀

##### If you're receiving Mega emails in a language other than english, replace the words "Best Regards" with whatever Mega use for your language :) 
