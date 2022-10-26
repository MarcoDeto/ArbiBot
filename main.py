from DeFi.biswap import *
from DeFi.vvs import *
from Exchange.cryptocom import *
from telegram import *
import asyncio

async def main():
    await initTelegram()
    telegram = await getChannel()
    while True:
        await get_biswap(telegram)

asyncio.run(main())