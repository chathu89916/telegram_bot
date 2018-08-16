import configuration
import emojiList

def subscribeNotice():
    notice = """Hi,

The <b>BOT DEVELOPMENT TEAM</b> built a new commands to subscribe names instead of your username. When someone mention your username in a chat, you will received a message from <b>"""+configuration.botUsername+"""</b>. Now you can add more names by using subscribe feature like below.

/subscribe <i>subscribename</i>

E.g.

/subscribe <i>your_first_name</i>
/subscribe <i>your_last_name</i>
/subscribe <i>your_home_town</i>
/subscribe <i>your_university</i>

Likewise you can give one by one or more than a word at a same time by separating space or comma.

E.g.

/subscribe <i>your_first_name</i> <i>your_last_name</i> <i>your_home_town</i> <i>your_university</i>

or

/subscribe <i>your_first_name</i> , <i>your_last_name</i> , <i>your_home_town</i> , <i>your_university</i>

If you want to see the list of your subscribe names in <b>visually</b>, just use /subscribewindow command and manage your all subscribes names in one place. When someone calls you by your subscribe name it will be counted and will display in the /subscribewindow .

Thank You""" + emojiList.successFaceIcon

    return notice