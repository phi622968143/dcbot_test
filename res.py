import bot
import discord

async def s_msg(msg,user):
    try:
        response = bot.handle_response(user)
        await msg.channel.send(response)  # Send the response to the user in a private message
    except Exception as e:
        print(e)
def run_bot():
    token='MTE1NTg5NDcyNDkyMjcyNDQ1Mg.GijwwC.Y0FugfL3f95y-FyxHEHsrsVlpPCTyxZQVP9I0A'
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    @client.event
    async def on_message(message):  # Use on_message instead of on_msg
        if message.author == client.user:
            return
        await s_msg(message,message.content)
    client.run(token)



