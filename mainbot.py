from discord.ext import commands
from dotenv import load_dotenv
import os
import traceback

INITIAL_EXTENSIONS = [
    'cogs.iroiro',
    'cogs.wolfram_alpha',
    'cogs.chess_game',
]

class MyBot(commands.Bot):

    def __init__(self, command_prefix):
        super().__init__(command_prefix,help_command=None)    #継承 /help:None->commands.DefaultHelpCommand()

        for cog in INITIAL_EXTENSIONS:  #Cog取得
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()   #エラー処理

    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')
        with open('error_trig.dat', mode='w') as f:
            f.write('0')



if __name__ == '__main__':
    bot = MyBot(command_prefix='./')
    load_dotenv()

    @bot.event
    async def on_command_error(ctx,ex):
        with open('error_trig.dat') as f:
            s = f.read()
            if s == '0':
                await ctx.send( f"{ctx.message.content} というコマンドは存在しません")
            else:
                with open('error_trig.dat', mode='w') as f:
                    f.write('0')

    @bot.event
    async def on_reaction_add(payload):
        print('***')
        print(payload)
        print('*')
        print(payload.channel_id)
        print('***')




    bot.run(os.environ['TOKEN']) # kido-