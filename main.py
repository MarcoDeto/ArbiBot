from DeFi.vvs import *
from Exchange.cryptocom import *
from telegram import *
import asyncio

async def main():
    await initTelegram()
    telegram = await getChannel()
    while True:
        await get_vvs_finance(telegram)

asyncio.run(main())