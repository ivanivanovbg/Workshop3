import commands.base.base_command as base
import core.application_data as appdata
import helpers.helpers as helpers

class TestReport(base.BaseCommand):
    def __init__(self, params: list[str], app_data: appdata.ApplicationData):
        super().__init__(params,app_data)

    def execute(self):
        if helpers.validate_parameters_count(self._params,1):
            try:
                testid = int(self._params[0])
                return self._app_data.test_report(testid)
            except ValueError as verr:
                return f"Invalid test id! Additional info : {verr.args[0]}"
        else:
            return "Wrong parameter count for TestReport command!"
