# RALF(IMAPclient-Dropbox-API-Integration)
allows your computer to upload files on your Dropbox account when you send the location of the file through your email 

#HOW TO USE

    clone the repository


1. SETUP AN EMAIL ACCOUNT FOR YOUR SYSTEM , PREFERRABLY AN OUTLOOK ACCOUNT.

(THIS CODE MAY NOT WORK WITH GMAIL DUE TO GOOGLE'S NEW SECUIRITY GUIDELINES DUE TO WHICH I DID NOT USE GOOGLE DRIVE IN THE FIRST PLACE AND USED DROPBOX INSTEAD.)

2.SETUP A DROPBOX ACCOUNT IF YOU DO NOT HAVE ONE, THEN GO TO https://www.dropbox.com/developers/apps.
   STEP 1.  Create an app in your Dropbox account

    Go to https://www.dropbox.com/developers/apps/create
    Authorize, if you weren’t.
    Choose Dropbox API on the first step.
    Choose Full Dropbox access on the second.
    Give your app a name. That name will become a folder in your Dropbox account.
    Push ‘Create app’ button.

    Dropbox API token
    Scroll down to ‘OAuth 2’ block and hit ‘Generate’ button near ‘Generated access token’ text.
      WARNING: Never share this Oauth token with anyone since it provides complete access to your account.
      
    Now copy this token and paste this in place of accesstoken variable text in the ralf_dropbox.py file 
    
3.TYPE IN YOUR SYSTEM EMAIL ID AND PASSWORD IN THE imap.py file.
  ALSO ADD YOUR EMAILID, WHICH YOU WILL BE USING TO SEND EMAILS TO YOUR SYSTEM EMAIL.

4.USE THE time.py TO RUN THE imap.py FILE EVERY 10 MIN OR SETUP A CRONTAB TASK IF YOU ARE USING LINUX.
  
  FOR CRONTAB:
  
      crontab -l
      chmod u+x /path/imap.py
      crontab -e
 use nano text editor and type in 
 
      */10 * * * * /path/to/imap.py
      
      
 
 
 YOU ARE ALL DONE!!!!
 
 PS:
 
 FORMAT OF EMAIL.
 
    ofcourse the mail must be to your system-email(goes without saying)
    leave the body blank and type in the path to the file in the subject.
    some thing like this 
        /home/ishanware77/Desktop/1.txt in the subject.
        
        
        
        
  DON'T FORGET TO GIVE A STAR IF YOU LIKE THE IDEA
      
      
    
    
       
    
    
  
    
    
    
    
   
  
    
