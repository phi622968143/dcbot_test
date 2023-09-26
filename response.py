import response
import discord

async def s_msg(msg,user_msg,is_private):
    try:
        response=response.handle_response(user_msg)
        await msg.author.send(response) if is_private else await msg.channel.send(response)
    except Exception as e:
        print(e)
def run_bot():
    token='MTE1NTg5NDcyNDkyMjcyNDQ1Mg.Gj1IMC.CrdHbtZTLZNdeY6ZjrkUiYevwqLlWYhxkLisLE'
    clinet=discord.Client()
    
    @clinet.event
    async def on_ready():
        print(f'{clinet.user} is no running')
    clinet.run(token)



