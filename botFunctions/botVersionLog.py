def botVesion():
    BOT_VERSION = """\n\n<b>What's New in Version 2.8</b>

* Introducing new feature call /subscribewindow to manage your all subscribes names instead of /subscribelist.

* Click the cross icon to remove the subscribe name easily.

* When someone calls you by your subscribe name it will be counted and you will see it from the /subscribewindow .

* It Can be subscribed more than one word at a time by separating space or comma(/subscribe name1 name2 | /subscribe name1 , name2)."""

    return BOT_VERSION

def changeLOG():
    changeLOG = """\n\n<b>Version 2.8</b>

* Introducing new feature call /subscribewindow to manage your all subscribes names instead of /subscribelist.

* Click the cross icon to remove the subscribe name easily.

* When someone calls you by your subscribe name it will be counted and you will see it from the /subscribewindow .

* It Can be subscribed more than one word at a time by separating space or comma(/subscribe name1 name2 | /subscribe name1 , name2).

<b>Version 2.7.1</b>

* Permission added for handle Photos and Voice( /photopermission , /voicepermission )

<b>Version 2.7</b>

* New 6 functions are introduced for admins ( /audiopermission , /videopermission , /documentpermission , /textpermission , /locationpermission , /contactpermission )

<b>Version 2.6</b>

* All the /all* commands are now working with reply messages and forward that message to particular users of groups.

* Now character limit is unlimited for your text messages.

<b>Version 2.5</b>

* You can change the permissions of the Bot when the bot is a admin of the group. Otherwise Bot doesn't change it.

* If the Bot is not in the database group table, Bot will left the chat automatically.

* Bugs are fixed in @all mention keyword.

<b>Version 2.4.2.2</b>

* When group is in the banned group list, even super admins are not able to add back bot to the group. Only Bot admin can add and remove that group from the banned group list.

<b>Version 2.4.2.1</b>

* When the Bot admin kicks out a group by using admin window, it will be moved into the banned group section.

<b>Version 2.4.2</b>

* It can be viewed all the group list which bot is the member of there and the banned group list

<b>Version 2.4.1</b>

* It can be viewed superadmin list using /adminwindow command and possible to remove them from there.

<b>Version 2.4</b>

* It can be handled all the groups and super admins by using Admin Window command( /adminwindow ).

<b>Version 2.3</b>

* Bot doesn't response for HHH(Hi, Hello, How are you?) in forwarded messages anymore.

* When the Bot is being added to the group, all the group admins' details will be saved into the database. Otherwise the Bot will prompt a warning message to START. 

* The group name will be in bold letters in the admin message when the Bot is being added to the group.

* Now the UNICODE data are saved into the database.

* Bot will send a message for all the group admins and super admins who are in the particular group, when the bot doesn't have the delete permission.

<b>Version 2.2</b>

* All the Super Admin commands can be used in bot private window only.
    
<b>Version 2.1</b>

* If someone mention you or your subscribe word in a reply text, you will be notified.
    
<b>Version 2.0</b>

* /subscribe, /unsubscribe and /subscribelist commands introduced ( just type / and follow the introduction ).

* Group admins can use /strickerpemission and /hhhpermission commands introduced ( just type / and follow the introduction ).
    
<b>Version 1.3.0</b>

* You can't play Games in groups anymore.

<b>Version 1.2.2</b>

* When someone mention you in a caption of a photo or reply to your message with a photo you can get it in high quality.

<b>Version 1.2.1</b>

* When you use stickers in group, it will be automatically deleted by the BOT.

<b>Version 1.1.0</b>

* When you reply to a message with a photo, video, audio, document, contact, voice or location it will be informed you as usual.

* If someone mention you in a caption of a photo, video, audio, document or voice that will be also informed. """

    return changeLOG