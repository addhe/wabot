# wabot
My Simple and Stupid Whatsapp bot

# let's setup our virtualenv for python
$ virtualenv -p python3 /tmp/wabot_virt_env

# let's activate our virtualend
$ source /tmp/wabot_virt_env/bin/activate

# let's install the requirement
$ pip install -r requirement.txt

# update your contact list and messages in this csv file
$ vim my_wa_contacts.csv 

# let's run the apps
$ python ./whatsapp.bot.py

notes:
- feel free to use any virtual environment technique and location
- feel free to add your virtual environment activation in your bash profile / zsh profile
- feel free to use any editor to edit the contact and messages
