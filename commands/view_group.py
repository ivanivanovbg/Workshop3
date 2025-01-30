import commands.base.base_command as base
import core.application_data as appdata
import helpers.helpers as helpers

class ViewGroup(base.BaseCommand):
    def __init__(self, params: list[str], app_data: appdata.ApplicationData):
        super().__init__(params,app_data)

    def execute(self):
        if helpers.validate_parameters_count(self._params,1):
            try:
                groupid = int(self._params[0])
                groupreport = self._app_data.view_group(groupid)
                return groupreport
            except ValueError as verr:
                return f"Invalid group id! Additional info : {verr.args[0]}"
        else:
            return "Wrong parameter count for ViewGroup command!"
