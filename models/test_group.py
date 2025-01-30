from models.test import Test
import models.test_run as testrun
import os


class TestGroup:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name
        self._tests: list[Test] = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def tests(self):
        return tuple(self._tests)

    @property
    def shortinfo(self):
        return f"#{self.id}. {self.name} ({len(self._tests)} tests)"

    @property
    def info(self):
        return self.shortinfo +os.linesep + os.linesep.join(f"  {c_test.shortinfo}" for c_test in self._tests)

    def add_test(self, test: Test):
        self._tests.append(test)

    def add_run_to_test(self,tid:int,trun:testrun.TestRun):
        for test in self._tests:
            if test.id == tid:
                test.add_test_run(trun)
                return True
        return False

    def test_report(self,tid:int):
        for test in self._tests:
            if test.id == tid:
                return test.info()

