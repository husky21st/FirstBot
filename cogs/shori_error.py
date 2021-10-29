from discord.ext import commands
from .iroiro import IroiroCog

class ShorishoriCog(IroiroCog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__(roll)

    @roll.error
    async def roll_error(self, ctx, error):
        await ctx.send('=roll NdNで入力してにぇ！')



def setup(bot):
    bot.add_cog(ShorishoriCog(bot))