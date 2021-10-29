from discord.ext import commands
import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup as bs4

class MathCog(commands.Cog):

    def __init__(self, bot):
        load_dotenv()
        self.bot = bot

    @commands.group()
    async def math(self, ctx):
        """計算したりいろいろできるよ！ feat.WolframAlpha"""
        if ctx.invoked_subcommand is None:
            await ctx.send('```以下の形で入力してください\n1.math search 検索ワード:結果の画像\n2.math url 検索ワード:検索ページのURL```')

    @math.command()
    async def search(self, ctx, * ,index):
        try:
            url = 'http://api.wolframalpha.com/v2/query'
            params = {'appid' : os.environ['WA_KEY'],'translation' : 'true' , 'input' : index }
            req = requests.get(url=url , params=params)
            #await ctx.send(req.url) #確認用
            soup = bs4(req.text, 'lxml-xml')
            input = soup.find('pod').find('plaintext').text
            await ctx.send(f'入力:{input}')
            await ctx.send(soup.find('pod').find('img').get('src'))
            await ctx.send(soup.find('pod').next_sibling.next_sibling.find('img').get('src'))
        except:
            url = 'https://www.wolframalpha.com/input/'
            params = {'i' : index ,'lang' : 'ja'}
            req = requests.get(url=url, params=params)
            await ctx.send('検索に失敗しました')
            await ctx.send(f'こちらをご確認ください:{req.url}')
            return

    @math.command()
    async def url(self, ctx, *, index):
        url = 'https://www.wolframalpha.com/input/'
        params = {'i': index, 'lang': 'ja'}
        req = requests.get(url=url, params=params)
        await ctx.send(req.url)


def setup(bot):
    bot.add_cog(MathCog(bot))