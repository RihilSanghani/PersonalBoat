import discord  # Import the Discord API wrapper
import os  # Import OS to access environment variables
from openai import OpenAI  # Import OpenAI API client

# Load secret tokens from environment variables
token = os.environ['DISCORD_TOKEN']  # Discord bot token
openai_token = os.environ['OPEN_AI_API_KEY']  # OpenAI API key

# Initialize the OpenAI client with API key
openAi_client = OpenAI(api_key=openai_token)


# Define a custom Discord client class
class MyClient(discord.Client):

    async def on_ready(self):
        """
        Event handler that triggers when the bot successfully connects to Discord.
        """
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        """
        Event handler that triggers when a message is sent in a Discord channel.
        The bot reads the message and responds using OpenAI.
        """
        # Prevent the bot from replying to itself
        if message.author == self.user:
            return

        channel = message.channel  # Get the channel where the message was sent

        try:
            # Send the user's message to OpenAI's ChatGPT API
            response = openAi_client.chat.completions.create(
                model="gpt-4o-mini",  # Use GPT-4o-mini model for response
                messages=[{"role": "user", "content": message.content}],  # User message
                temperature=1,  # Higher values make responses more random
                max_tokens=1000,  # Limit the response length to avoid long outputs
                top_p=1,  # Controls diversity of response (1 means max diversity)
                frequency_penalty=0,  # No penalty for repeating words
                presence_penalty=0  # No penalty for using new words
            )

            # Extract AI-generated response
            bot_reply = response.choices[0].message.content

            # Check if the response is longer than Discord's message limit (2000 characters)
            if len(bot_reply) > 2000:
                # If response is too long, split it into 2000-character chunks
                chunks = [
                    bot_reply[i:i + 2000]
                    for i in range(0, len(bot_reply), 2000)
                ]
                for chunk in chunks:
                    await channel.send(chunk)  # Send each chunk separately
            else:
                await channel.send(bot_reply)  # Send the AI response normally

        except Exception as e:
            # Handle errors (e.g., API failure, invalid response)
            print(f"Error: {e}")
            await channel.send("⚠️ Sorry, there was an error processing your request.")


# Set bot intents (enabling message content reading)
intents = discord.Intents.default()
intents.message_content = True  # Required for the bot to read messages

# Create an instance of MyClient with the specified intents
client = MyClient(intents=intents)

# Run the bot using the provided Discord token
client.run(token)
