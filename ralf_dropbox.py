import sys
import dropbox

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# Access token
TOKEN = 'ACCESS TOKEN OBTAINED FROM DROPBOX DEVELOPERS WEBSITE'


# LOCALFILE = '/home/ishanware77/Desktop/vac_agendas.txt'
# BACKUPPATH = '/vac_agendas.txt'  # Keep the forward slash before destination filename


# Uploads contents of LOCALFILE to Dropbox
def backup(dbx, LOCALFILE, BACKUPPATH):
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


# Adding few functions to check file details
def checkFileDetails(dbx):
    print("Checking file details")

    for entry in dbx.files_list_folder('').entries:
        print("File list is : ")
        print(entry.name)


# def execute():
#    mail_instance = imapclient.IMAPClient('imap-mail@outlook.com', ssl=True)
#    mail_instance.login('system_ralf@outlook.com', 'system_ralf')
#    mail_instance.select_folder('INBOX')


# Run this script independently
if __name__ == '__main__':
    # Check for an access token
    if len(TOKEN) == 0:
        sys.exit(
            "ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

    try:
        checkFileDetails(dbx)
    except Error as err:
        sys.exit("Error while checking file details")

    print("Creating backup...")
    # Create a backup of the current settings file
    backup(dbx)

    print("Done!")
