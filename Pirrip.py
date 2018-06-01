import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    chance = random.randint(1,100)
    if message.content.startswith('/steal hat'):
        userid = message.author.id
        if userid != '429825738485792776':
            if message.content != '/steal hat again':
                if chance <= 25:
                    await client.send_typing(message.channel)
                    await asyncio.sleep(2)
                    await client.send_message(message.channel, '/steal hat again')
    elif message.content.startswith('/look a hat'):
        if chance <= 25:
            await client.send_message(message.channel, 'Ooh, a hat! :3')
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, '/steal hat')
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, '/steal hat again')
        else:
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, 'What hat? :3')
    elif message.content.startswith('/irritate Sigma'):
        taunt = ['Hehehe :3',
                 'My sneaky skills cannot fail! :3',
                 'Beholds my irritating abilities! :3',
                 'Sigma who? :3']
        srandom = random.SystemRandom()
        if chance <= 10:
            await client.send_message(message.channel, srandom.choice(taunt))
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, '/steal hat')
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, '/steal hat again')
        elif chance <= 20 and chance > 10:
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, 'Who, dear Miggy-ma? :3')
        elif chance <= 30 and chance > 20:
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, 'I\' like to see *you* irritate dear Miggy-ma! :3')
        elif chance <= 40 and chance > 30:
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, 'But I already have his hat! :3')
        elif chance <= 90 and chance > 40:
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, 'I\'d rather irritate you! :3')
        elif chance > 90:
            await client.send_typing(message.channel)
            await asyncio.sleep(2)
            await client.send_message(message.channel, 'Sigma who? :3')
    elif message.content.startswith('/help'):
        await client.send_typing(message.channel)
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'Help? What is? I do not understand :3')
    elif message.content.startswith('/stalk Alice'):
        userid = message.author.id
        if userid == '398479091549863936':
            if chance <= 50:
                await client.send_typing(message.channel)
                await asyncio.sleep(2)
                await client.send_message(message.channel, 'I helps! :3')
            else:
                await client.send_typing(message.channel)
                await asyncio.sleep(2)
                await client.send_message(message.channel, 'I stalks you insteads! :3')
    elif message.content.startswith('/irritate Matt'):
        userid = message.author.id
        if userid == '398479091549863936':
            if chance <= 50:
                await client.send_typing(message.channel)
                await asyncio.sleep(2)
                await client.send_message(message.channel, 'I helps! :3')


client.run('NDI5ODI1NzM4NDg1NzkyNzc2.DaMdfw.Sz1D2StTxDaSE8lUNH2M5YjWC_8')