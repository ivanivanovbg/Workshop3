import commands.base.base_command as base
import core.application_data as appdata
import helpers.helpers as helpers

class AddRunToTestCommand(base.BaseCommand):
    def __init__(self, params: list[str], app_data: appdata.ApplicationData):
        super().__init__(params,app_data)

    def execute(self):
        if helpers.validate_parameters_count(self._params,3):
            try:
                testid = int(self._params[0])
                runtime = int(self._params[2])
                self._app_data.add_run_to_test(testid,self._params[1],runtime)
                return "TestRun registered"
            except ValueError as verr:
                return f"Error occurred when attempting to add Test Run {verr.args[0]}"
        else:
            return "Wrong parameter count for AddTestGroup command!"
