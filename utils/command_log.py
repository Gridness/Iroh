import datetime

def command_log(command_name, ctx):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'[IrohBot | {current_time}] \"{command_name}\" command was executed by {ctx.author}')