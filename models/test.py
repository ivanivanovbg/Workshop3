import models.constants.test_result as testresult
from models.test_run import TestRun


class Test:
    def __init__(self, id: int, description: str):
        self._id = id
        self._description = description
        self._test_runs: list[TestRun] = []

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def test_runs(self):
        return tuple(self._test_runs)

    @property
    def failed_runs(self)->int:
        return len([rn.test_result for rn in self._test_runs if rn.test_result == testresult.TestResult.FAIL])

    @property
    def passing_runs(self)->int:
        return len([rn.test_result for rn in self._test_runs if rn.test_result == testresult.TestResult.PASS])

    @property
    def total_runtime(self)->int:
        return sum([rn.runtime_ms for rn in self._test_runs])

    @property
    def average_runtime(self)->float:
        return self.total_runtime/len(self._test_runs)

    @property
    def shortinfo(self):
        return f"""#{self.id}. [{self.description}]: {len(self._test_runs)} runs"""

    @property
    def info(self):
        return f"""{self.shortinfo}
- Passing: {self.passing_runs}
- Failing: {self.failed_runs}
- Total runtime: {self.total_runtime}ms
- Average runtime: {self.average_runtime:.1f}ms"""

    def add_test_run(self, test_run: TestRun):
        self._test_runs.append(test_run)


