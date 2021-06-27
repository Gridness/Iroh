import discord

def build_embed(client, title, description, color, has_author, has_footer, footer_text):
    embed = discord.Embed(title=title, description=description, color=color)
    if has_author:
        embed.set_author(client.user)
    if has_footer:
        embed.set_footer(text=footer_text)
    return embed