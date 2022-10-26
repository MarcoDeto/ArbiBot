from telethon import TelegramClient # pip install telethon
from telethon.errors import SessionPasswordNeededError

from config import TELEGRAM_API_HASH, TELEGRAM_API_ID, TELEGRAM_CHANNEL, TELEGRAM_PHONE, TELEGRAM_USERBNAME

client = TelegramClient(TELEGRAM_USERBNAME, TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def initTelegram():

    await client.start()
    print("Telegram Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(TELEGRAM_PHONE)
        try:
            await client.sign_in(TELEGRAM_PHONE, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))


async def getChannel():
    return await client.get_entity(TELEGRAM_CHANNEL)


async def test_message(telegram):
    await client.send_message(telegram, 'test_message')


async def sendMessage(telegram, subtitle, open_price, close_price, exchange, percent, buy_on_defi = False):
    
    title = '**🤑💰ARBITRAGGIO💰🤑\n'
    profit = 'PROFIT: ' + str(percent) + '% 🤑 **'

    openPrice = '\n\n**OPEN PRICE**: ' + str(open_price) + ' 🛒\n'
    if buy_on_defi == True:
        openPrice = openPrice + 'BUY ON DEFI\n'
    else:
        openPrice = openPrice + 'BUY ON ' + exchange + '\n'
        
    closePrice = '**CLOSE PRICE**: ' + str(close_price) + ' ✋🏼\n'
    if buy_on_defi == False:
        closePrice = closePrice + 'SELL ON DEFI\n'
    else:
        closePrice = closePrice + 'SELL ON ' + exchange + '\n'

    message = title + profit + subtitle + openPrice + closePrice

    await client.send_message(telegram, message)


