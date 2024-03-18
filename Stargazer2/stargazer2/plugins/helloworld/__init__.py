from nonebot import on_command
from nonebot.adapters.satori import Bot
from nonebot.adapters.satori.event import MessageEvent
from nonebot.adapters.satori.message import MessageSegment


matcher = on_command("test")

@matcher.handle()
async def handle_receive(bot: Bot, event: MessageEvent):
    await bot.send(event, MessageSegment.text("Hello, world!"))
    
    
help = on_command("help")
@help.handle()
async def handle_receive(bot: Bot, event: MessageEvent):
    await bot.send(event, MessageSegment.text("help, world!"))