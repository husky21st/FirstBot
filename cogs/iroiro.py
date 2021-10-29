from discord.ext import commands
import random
import sys
from dotenv import load_dotenv
import os


class IroiroCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        load_dotenv()

    @commands.command()
    async def stop(self, ctx):
        if ctx.author.id == int(os.environ['ADMIN_ID']) + 0: #debug
            await ctx.send('停止します')
            await self.bot.close()
            await self.sys.exit()
        else:
            await ctx.send('実行権限がありません')

    @commands.command()
    async def what(self, ctx, *, index):
        """なんでもWikiでしらべるよ！(全てとは言っていない)"""
        url = 'https://ja.wikipedia.org/wiki/'
        await ctx.send(url+index)

    @what.error
    async def roll_error(self, ctx, error):
        await ctx.send('何か入力してくださいーーー')
        with open('error_trig.dat', mode='w') as f:
            f.write('1')

    @commands.command()
    async def roll(self, ctx, dice):
        """サイコロを投げれるよ！それ以上でも以下でもないよ！"""
        try:
            rolls, limit = map(int, dice.split('d'))
        except:
            await ctx.send('NdNで入力してにぇ！')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @roll.error
    async def roll_error(self, ctx, error):
        await ctx.send('=roll NdN　で入力してにぇ！')
        with open('error_trig.dat', mode='w') as f:
            f.write('1')


def setup(bot):
    bot.add_cog(IroiroCog(bot))