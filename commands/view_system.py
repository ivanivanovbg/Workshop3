import commands.base.base_command as base
import core.application_data as appdata
import helpers.helpers as helpers

class ViewSystem(base.BaseCommand):
    def __init__(self, params: list[str], app_data: appdata.ApplicationData):
        super().__init__(params,app_data)

    def execute(self):
        if helpers.validate_parameters_count(self._params,0):
            try:
                systemreport = self._app_data.view_system()
                return systemreport
            except ValueError as verr:
                return f"Something happened :( See additional info : {verr.args[0]}"
        else:
            return "Wrong parameter count for ViewSystem command! Accepts zero parameters!"
