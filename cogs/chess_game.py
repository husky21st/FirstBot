import discord
from discord.ext import commands

class ChessCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def chess(self, ctx):
        """chessできます"""
        if ctx.invoked_subcommand is None:
            await ctx.send('```以下の形で入力してください\n1.chess start: ゲームを始めます```')

    @chess.command()
    async def start(self, ctx):
        embed = discord.Embed(title='chess部屋が作られました', description='挑戦する人は⭕を押してください\nキャンセルする場合は❌を押してください', color=0x0000ff)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        #bot_message = await ctx.send('chess部屋が作られました\n挑戦する人は⭕を押してください\nキャンセルする場合は❌を押してください')
        bot_message = await ctx.send(embed=embed)
        for reaction in ['⭕', '❌']:
            await bot_message.add_reaction(reaction)




    @chess.error
    async def roll_error(self, ctx, error):
        await ctx.send('chess:error')
        with open('error_trig.dat', mode='w') as f:
            f.write('1')

def setup(bot):
    bot.add_cog(ChessCog(bot))