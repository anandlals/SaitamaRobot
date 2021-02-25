import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import is_user_admin, user_admin
from SaitamaRobot.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'doraemon' 
EDIT_SLEEP = 1
#edit how many times in 'doraemon' 
EDIT_TIMES = 3

doraemon = [
            "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",
            "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴"
]



@user_admin
@run_async
def police(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Doraemon') 
    for x in range(EDIT_TIMES):
        msg.edit_text(police_siren[x%2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('Doraemon')


__help__ = """ For More information about Doraemon please visit our channel or contact me
"""

DORAEMON_HANDLER = DisableAbleCommandHandler("doraemon", doraemon)


dispatcher.add_handler(DORAEMON_HANDLER)

__mod_name__ = "Doraemon"
__command_list__ = ["doraemon"]
__handlers__ = [DORAEMON_HANDLER]
