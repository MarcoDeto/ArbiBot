from DeFi.pancake import get_pancake_finance
from DeFi.vvs import *
from Exchange.cryptocom import *
from telegram import *
import asyncio

async def main():
    await initTelegram()
    telegram = await getChannel()
    while True:
        await get_pancake_finance(telegram)

asyncio.run(main())