import unittest
from time import sleep

from modle.driver import Chrome


class MyTest(unittest.TestCase):

    def setUp(self):
        d = Chrome()
        self.driver = d.connect()
        sleep(7)

    def tearDown(self):
        self.driver.quit()