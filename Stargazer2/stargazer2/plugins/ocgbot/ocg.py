
import nonebot 
from nonebot import on_command,on_keyword
from nonebot.params import CommandArg
from nonebot.typing import T_State
from nonebot.adapters.satori import Bot
from nonebot.adapters.satori.event import *
from nonebot.adapters.satori.message import *


search_card = on_command("查卡", aliases={"ck", "CK"})

@search_card.handle()
async def _(bot: Bot, event: Event, state: T_State, args: Message = CommandArg()):
    await bot.send(event, MessageSegment.text("Hello, world!"))
    
randomCard = on_command('随机一卡', aliases={'抽一张卡'})
async def _(bot: Bot, event: Event, state: T_State):
    groupSession = None
    sessionId = None
    if isinstance(event, PrivateMessageEvent):
        sessionId = 'user_' + str(event.user_id)
        userType = 'private'
    if isinstance(event, PublicMessageEvent):
        groupSession = 'group_' + str(event.group_id)
        sessionId = 'user_' + str(event.sender.user_id)
        userType = 'group'
    try:
        userType = 'SU' if (str(event.user_id) in nonebot.get_driver().config.superusers) else userType
        pm.CheckPermission(sessionId, groupSession, userType)
    except PermissionError as e:
        await randomCard.finish(str(e))
    try:
        js = getRandomCard()
        pm.UpdateLastSend(sessionId)
    except Exception as e:
        await randomCard.finish("咿呀？卡组被送进异次元了呢~")
    await send3(js, randomCard)
