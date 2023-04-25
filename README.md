### mastodon-thegx-blocker
Mastodon-thegx-blocker is a Python script that will search for new follows by accounts with 'thegx' and block them. 

This is an instance level admin only script (the admin:read and admin:right privileges


You can set it up to run as a cron job to block the accounts as they appear. 

### First Things
Setup your config.
Set your account credentials in the config.ini and run the script.

site = https://example.com 

#### User ####
This script needs to be ran with an account that has moderation privileges. 
```
bot_username = someemail@example.com (Mastodon account user)
bot_password = botspassword (User password)
```

After first run, pytooter_clientcred.secret will be created in your run folder. 
```
#client_id = this will be noted in pytooter_clientcred.secret line 1
#client_secret = this will be noted in pytooter_clientcred.secret line 2
#oauth = this will be noted after you add the above two and re-run
```

After first run, open newly created pytooter_clientcred.secret file in your run folder. Add _client_ID_ and _client_secret=_ to your config file and remove the hashes. Save the config file.

Rerun and copy and paste your _oauth_ code as shown in the terminal.

### Setup Cron job
To run the script every 5 minutes, edit/open the cron file: crontab -e
 Add following entry:
 ```
 */5 * * * * python3 /path/to/mastodon-thegx-blocker.py
 ```
  Save and exit

If running Windows, you can rename main.py to main.pyw and set it up to run silently on a regular schedule with Task Scheduler.
