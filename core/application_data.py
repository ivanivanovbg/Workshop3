import models.test_group as testgroup
import models.test as test
import models.test_run as testrun
import os

class ApplicationData:
    last_testid=0
    last_groupid=0

    @classmethod
    def get_next_groupid(cls):
        cls.last_groupid +=1
        return cls.last_groupid

    @classmethod
    def get_next_testid(cls):
        cls.last_testid +=1
        return cls.last_testid

    def __init__(self):
        self._test_groups: list[testgroup.TestGroup] = []

    @property
    def groups(self):
        return tuple(self._test_groups)

    def add_test_to_group(self,tgid:int,tdesc:str)->bool|int:
        tgroup = self.find_groups_by_id(tgid)
        if not tgroup:
            return False
        else:
            new_test = test.Test(self.get_next_testid(),tdesc)
            tgroup[0].add_test(new_test)
            return new_test.id


    def add_test_group(self,tgname:str):
        groupid = self.get_next_groupid()
        self._test_groups.append(testgroup.TestGroup(groupid,tgname))
        return groupid

    def add_run_to_test(self,testid:int,rundesc:str,runtime:int):
        trun = testrun.TestRun(rundesc,runtime)
        fresult = False
        for group in self._test_groups:
            if group.add_run_to_test(testid,trun):
                trun.to_db()
                fresult = True
        return fresult

    def view_group(self,groupid:int):
        group = self.find_groups_by_id(groupid)
        if group:
            return group[0].info
        else:
            return "Error : group not found!"

    def view_system(self):
        return f"Test Reporter System ({len(self._test_groups)} test groups)"+os.linesep+os.linesep.join(["  "+grp.shortinfo for grp in self._test_groups])

    def test_report(self,testid:int):
        for group in self._test_groups:
            for rep_test in group.tests:
                if rep_test.id == testid:
                    return rep_test.info
        return "Invalid test id !"

    def find_groups_by_id(self,uid:int)->list[testgroup.TestGroup]|bool:
        tglist = [tg for tg in self._test_groups if tg.id == uid]
        if len(tglist) == 1:
            return tglist
        elif len(tglist) > 1:
            return False
        return False

    def remove_group_by_id(self,uid:int)->bool:
        groups = self.find_groups_by_id(uid)
        if not groups:
            return False
        else:
            for group in groups:
                self._test_groups.remove(group)
            return True
