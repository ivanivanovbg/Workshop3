import commands.base.base_command as base
import core.application_data as appdata
import helpers.helpers as helpers

class RemoveTestGroupCommand(base.BaseCommand):
    def __init__(self, params: list[str], app_data: appdata.ApplicationData):
        super().__init__(params,app_data)

    def execute(self):
        if helpers.validate_parameters_count(self._params,1):
            try:
                groupid = int(self._params[0])
                result = self._app_data.remove_group_by_id(groupid)
                if result:
                    return f"Group #{groupid} removed"
                else:
                    return f"Group #{groupid} cannot be removed, please contact pop@armenia.com!"
            except ValueError as err:
                return f"Invalid group id provided : {err.args[0]} !"
        else:
            return "Wrong parameter count for AddTestGroup command!"

