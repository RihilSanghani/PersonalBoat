# This example requires the 'message_content' intent.

import discord
import os
from openai import OpenAI

# get secrect token
token = os.environ['DISCORD_TOKEN']
openai_token = os.environ['OPEN_AI_API_KEY']

openAi_client = OpenAI(api_key=openai_token)


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if (message.author == self.user):
            return

        # print(f'Message from {message.author}: {message.content}')
        channel = message.channel
        try:
            response = openAi_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": message.content
                }],
                temperature=1,
                max_completion_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0)

            bot_reply = response.choices[0].message.content

            if len(bot_reply) > 2000:
                chunks = [
                    bot_reply[i:i + 2000]
                    for i in range(0, len(bot_reply), 2000)
                ]
                for chunk in chunks:
                    await channel.send(chunk)
            else:
                await channel.send(bot_reply)

        except Exception as e:
            print(f"Error: {e}")
            await channel.send(
                "⚠️ Sorry, there was an error processing your request.")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
