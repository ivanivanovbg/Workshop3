import core.application_data as appdata
import commands.end_cmd as end_cmd
import commands.base.base_command as base
import commands.add_test_group as addtestgroup
import commands.add_test_to_group as addtesttogroup
import commands.remove_test_group as removetestgroup
import commands.add_run_to_test as addruntotest
import commands.test_report as testreport
import commands.view_group as viewgroup
import commands.view_system as viewsystem
import core.engine as engine
END = "end".lower()
ADDTESTGROUP = "addtestgroup".lower()
REMOVETESTGROUP = "removegroup".lower()
ADDTEST = "addtest".lower()
ADDRUN = "addtestrun".lower()
TESTREPORT = "testreport".lower()
VIEWGROUP = "viewgroup".lower()
VIEWSYSTEM = "viewsystem".lower()

class CommandFactory:
    def __init__(self, data: appdata.ApplicationData):
        self._app_data = data
        self._eng = ""

    @property
    def eng(self):
        return self._eng

    @eng.setter
    def eng(self,value):
        if isinstance(value,engine.Engine):
            self._eng = value

    def create(self, input_line):

        cmd,*parameters = input_line.split()

        cmd = cmd.lower()

        if cmd == END:
            return end_cmd.EndCommand(parameters,self._app_data,self._eng)
        elif cmd == ADDTESTGROUP:
            return addtestgroup.AddTestGroupCommand(parameters,self._app_data)
        elif cmd == REMOVETESTGROUP:
            return removetestgroup.RemoveTestGroupCommand(parameters,self._app_data)
        elif cmd == ADDTEST:
            return addtesttogroup.AddTestToGroupCommand(parameters,self._app_data)
        elif cmd == ADDRUN:
            return addruntotest.AddRunToTestCommand(parameters,self._app_data)
        elif cmd == TESTREPORT:
            return testreport.TestReport(parameters,self._app_data)
        elif cmd == VIEWGROUP:
            return viewgroup.ViewGroup(parameters,self._app_data)
        elif cmd == VIEWSYSTEM:
            return viewsystem.ViewSystem(parameters,self._app_data)
        else:
            return base.BaseCommand([],self._app_data)
