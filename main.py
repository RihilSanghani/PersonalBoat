# This example requires the 'message_content' intent.

import discord
import os
from openai import OpenAI

# get secrect token
token = os.environ['DISCORD_TOKEN']
openai_token = os.environ['OPEN_AI_API_KEY']
project_key = os.environ['PROJECT_KEY']
org_id = os.environ['ORG_ID']


openai_client = OpenAI(api_key=openai_token)


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user: # if message is from bot
            return
            
        print(f'Message from {message.author}: {message.content}')
        channel = message.channel
        
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": message.content
            }],
            response_format={"type": "text"},
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
        print(response)
        await channel.send(response.choices[0].message.content)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
