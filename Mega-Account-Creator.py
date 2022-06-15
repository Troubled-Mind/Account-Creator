# -----------------------------------------------------------------------------------
#
#                    Mega-Account-Creator
#                       by TroubledMind
#
# -----------------------------------------------------------------------------------
#  Please note: this ONLY works with @gmail.com email addresses
#
#  INSTRUCTIONS:
#  FOLLOW ALL OF THESE, IF YOU GET STUCK, DM ME
#  
#  STAGE 1 - Set up your gmail account
#      purpose: Allow the script access to read your emails to get the verification codes
#      without this, it will not function
# 
#  1.  Go to https://console.cloud.google.com/apis/dashboard
#  2.  In the blue bar at the top, click "Select a project" then "New Project"
#  3.  Pick a name (something like 'MegaCreator')
#  4.  In the left hand sidebar, go to "APIs and Services"
#  5.  In this window, under the search bar click "+ ENABLE APIS AND SERVICES"
#  6.  Search for "Gmail API" and then select Gmail API from the search results
#  7.  Click "Enable" (if it's already enabled, click "Manage")
#  8.  Again on the left sidebar, go to "Credentials"
#  9.  On the right hand side, click the white button "CONFIGURE CONSENT SCREEN"
#  10. Choose "External" (Internal isn't available for free accounts) and CREATE
#  11. Fill in this screen with App Name (Mega Accounts), your email from the dropdown, 
#      And at the very bottom under 'Developer contact information' your email again
#
#  12. Save and continue
#  13. On the OAuth consent screen, click 'Publish'
#  14. Back on the "Credentials" tab from the left sidebar
#  15. Under the search bar, click "+ CREATE CREDENTAILS"
#  16. In the popup, choose "OAuth Client ID"
#  17. Choose "Desktop App" as the application type
#  18. Name it (anything you want), and click Create
#  19. You now get a Client ID and Client Secret
#     
#      NEVER EVER EVER EVER give these to anyone. ONLY put them in this script.
#
#  20. Click the download button to download a .json file, and name it "credentials.json"
#  21. Put this file in the same folder as this script.
#
#  NOTE - on first run, your browser will open and ask you to authorise your gmail account
#  make sure you choose your primary email from the list and make sure the name of the app is what you named it in step 18
#  YOU MAY GET A WARNING 'GOOGLE HASN'T VERIFIED THIS APP' - Click 'Advanced' at the bottom left
#  Then at the bottom, 'Go to [name you chose in step 18]' e.g. 'Go to Mega Accounts (unsafe)'
#  Finally, choose 'Continue'
#
#
#	STAGE 2 - Set up your system
#   1. Install the latest Python if you don't have it already
#   2. In the folder this tool is in, download Megatools from your system
#      Downloads can be found here: https://megatools.megous.com/builds/builds/
#      Extract everything inside to the folder, and name it `megatools`
#
#   3. Open command prompt/terminal in this folder and run the two commands below:
#      `pip install google-api-python-client`
#      `pip install oauth2client`
#
#      If you don't have pip, download this file below, and open command prompt to the folder it is in
#      and run `python get-pip.py` 
#      https://bootstrap.pypa.io/get-pip.py
#  
#
#
#	STAGE 3 - Set up the script
#	1. On line 94, set the name your account will use in mega. 
#      All accounts share the same name. 
# 	2. On line 95, set the password you want to use for ALL mega accounts created
#   3. On line 93, set the PATH to the megatools folder
#   4. Open "emails.txt" and add the account emails you want creating WITHOUT @gmail.com
#      Example file picture: https://i.imgur.com/zSECSzv.png

#   5. Run the script `python Mega-Account-Creator.py` in the terminal
#   6. Note- the script MAY stop at `Getting link from email`
#      If this happens, simply stop and restart the script 
#		(Stop by using "ctrl+c" and start by running the command again)
#
#
#         DO NOT MODIFY ANYTHING ELSE
# -----------------------------------------------------------------------------------

from subprocess import PIPE, run
import re, time, base64
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
SCOPES = "https://www.googleapis.com/auth/gmail.modify"
#SCOPES = "https://mail.google.com"

# the folder that megatools is stored in
emails = []
path = "D:/Users/TroubledMind/Documents/Mega-Creator/megatools/"
accountName = "YOUR ACCOUNT NAME HERE"
password = "YOUR PASSWORD HERE"


# create a command to run command line tools
def out(command):
	result = run(command, universal_newlines=True, shell=True, capture_output=True)
	return result.stdout

# function to read emails.txt to array
def readFile():
	file = open('emails.txt')
	emails = file.readlines()
	emails = [e.replace('\n','') for e in emails]
	file.close()
	return emails

# function to register accounts
def register(email, name, password):
	#command to register mega account
	register = path + "megatools reg --register --email " + email + " --name " + name + " --password " + password
	#store output from above command to get the verificationCode1
	output = out(register) 
	#print(output)
	verificationCode1 = re.search("megatools reg --verify (.*) @LINK@", output).group(1)
	return verificationCode1

# function to read your gmail inbox, and get the correct verification code for the email that was requested
def getVerificationCodeFromEmail(email):
	# try and connect to inbox, otherwise, authorise via browser
	store = file.Storage('token.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
		creds = tools.run_flow(flow, store)
	service = build('gmail','v1',http=creds.authorize(Http()))
	# read inbox
	resultsSize = 0
	i = 0
	while(resultsSize == 0) or (i < 5):
		results = service.users().messages().list(userId='me', labelIds = ['INBOX'], q = 'from:welcome@mega.nz,subject:Mega Email Verification Required').execute()
		if(results['resultSizeEstimate'] > 0):
			resultsSize = results['resultSizeEstimate']
		i = i + 1
		if(i == 5):
			break
		break
	if(resultsSize == 0):
		return ''
	messages=results.get('messages',[])
	messageBody = ''	
	
	# find message in inbox
	for message in messages:
		msg = service.users().messages().get(userId='me', id=message['id']).execute()
		resultsSize = 0
		# wait for the body length to be > 0
		while(resultsSize == 0):
			if(msg['payload']['parts'][0]['body']['size'] > 0):
				resultsSize = 1
		messageBody = msg['payload']['parts'][0]['body']['data']

		# decode the message and find the link
		messageBodyDecoded = base64.b64decode(messageBody)
		messageBodyDecoded = messageBodyDecoded.decode("utf-8")
		messageBodyDecoded = messageBodyDecoded.replace("\r\n", "__")
		emailVerificationLink = re.search(":____(.*)____Best regards", messageBodyDecoded)
		emailVerificationLink = emailVerificationLink.group(1)
		service.users().messages().trash(userId='me', id=message['id']).execute()
		return emailVerificationLink


# function to verify email once code from first command and email inbox are read
def verify(firstVerificationCode, emailVerificationLink, email):
	#verification command once all are received
	verify = path + "megatools reg --verify " + firstVerificationCode + " " + emailVerificationLink
	output = out(verify)
	print("    " + email + " -> " + output)
	
def deleteEmailFromTxtFile(email):
	with open('emails.txt', 'r') as f:
		lines = f.readlines()
	with open('emails.txt', 'w') as f:
		for line in lines:
			if(email not in line):
				f.write(line)
	
def writeEmailToTxtFile(email, password):
	with open('MegaAccounts.txt', 'a') as f:
		f.write(email + "@gmail.com, " + password + "\n")

# Main program

emails = readFile()
for email in emails:
	print("-------- Current Email: " + email + "@gmail.com --------")
	firstVerificationCode = register(email + "@gmail.com", accountName, password)
	print("    Got verification code...")
	print("    Waiting 5s for verification email...")
	time.sleep(5)
	print("    Getting link from email...")
	i = 0
	emailVerificationLink = ''
	while (emailVerificationLink == '') :
		i = i + 1
		emailVerificationLink = getVerificationCodeFromEmail(email + "@gmail.com")
	print("    Got link!")
	print("    Verifying account...")
	verify(firstVerificationCode, emailVerificationLink, email + "@gmail.com")
	print("    Deleting " + email + " from .txt file")
	deleteEmailFromTxtFile(email)
	print("    Adding " + email + " to MegaAccounts.txt file")
	writeEmailToTxtFile(email, password)
	emailVerificationLink = ''
	firstVerificationCode = ''
	print("  ")
	print("  ")
print("------------------------------------")
print("Script complete! Check MegaAccounts.txt for all accounts which were created successfully.")
print("------------------------------------")


