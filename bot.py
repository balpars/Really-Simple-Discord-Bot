import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# A fake token by token-generator
# in production use a real token and hide it with environment variables instead
TOKEN = "lJUXmqM6oFay3jgjv5jVwYuHG7EWeoFPsDkvJHtRkG6qDi91yFY0WoMPX61HpEWB"

@client.event
async def on_message(message):

    # Prevents answering itself to avoid loops
    if message.author == client.user:
        return

    # Checks if the message is sent to its DM
    if isinstance(message.channel,discord.DMChannel):
        
        if message.content == 'flag':
            await message.channel.send("No flag for you :D")
            return

        if message.content == '!help':
            await message.channel.send("Sure! But first send me the flag!")
            return
        
        if 'hi' in message.content or 'hello' in message.content:
            await message.channel.send(f"Hello {message.author.name}!")
            return


client.run(TOKEN)
