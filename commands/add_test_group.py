import commands.base.base_command as base
import core.application_data as appdata
import helpers.helpers as helpers

class AddTestGroupCommand(base.BaseCommand):
    def __init__(self, params: list[str], app_data: appdata.ApplicationData):
        super().__init__(params,app_data)

    def execute(self):
        if helpers.validate_parameters_count(self._params,1):
            groupid = self._app_data.add_test_group(self._params[0])
            return f"Group #{groupid} created"
        else:
            return "Wrong parameter count for AddTestGroup command!"

