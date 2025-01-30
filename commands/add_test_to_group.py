import commands.base.base_command as base
import core.application_data as appdata
import helpers.helpers as helpers
import os

class AddTestToGroupCommand(base.BaseCommand):
    def __init__(self, params: list[str], app_data: appdata.ApplicationData):
        super().__init__(params,app_data)

    def execute(self):
        if helpers.validate_parameters_count(self._params,2):
            try:
                groupid = int(self._params[0])
                testid = self._app_data.add_test_to_group(groupid,self._params[1])
                if testid:
                    return f"Test #{testid} added to group #{self._params[0]}"
            except ValueError as verr:
                return f"Error occured while attempting to add Test #{self._params[1]} to group {self._params[0]}!" + os.linesep + verr.args[0]
        else:
            return "Wrong parameter count for AddTestGroup command!"

