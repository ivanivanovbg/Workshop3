import commands.base.base_command as base
import core.application_data as appdata
import core.engine as engine

class EndCommand(base.BaseCommand):
    def __init__(self, params: list[str], app_data: appdata.ApplicationData,eng):
        if isinstance(eng,engine.Engine):
            super().__init__(params,app_data)
            print(eng.spill_the_beans())
            exit()
        else:
            raise ValueError("Invalid engine provided for end command!")
