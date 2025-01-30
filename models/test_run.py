from models.constants.test_result import TestResult
import sqlite3
import os

class TestRun:
    def __init__(self, test_result: str, runtime_ms: int):
        if test_result not in [TestResult.PASS, TestResult.FAIL]:
            raise ValueError('Invalid test result value')

        self._test_result = test_result
        self._runtime_ms = runtime_ms
        self._dbid = 0

    @property
    def test_result(self):
        return self._test_result

    @property
    def runtime_ms(self):
        return self._runtime_ms

    def to_db(self):
        conn = sqlite3.connect("./database/testreport.db")
        curs = conn.cursor()
        conns = f"INSERT INTO testruns(tresult,runtime) VALUES('{self._test_result}','{self._runtime_ms}')"
        curs.execute(conns)
        conn.commit()
        self._dbid = curs.lastrowid
        conn.close()
