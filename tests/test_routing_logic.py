__author__ = 'gsibble'

import unittest
from sure import this

from helpers import routing_logic

class TestRoutingLogic(unittest.TestCase):

    def setUp(self):
        self.group_of_75 = [x for x in xrange(0, 75)]
        self.group_of_76 = [x for x in xrange(0, 76)]
        self.group_of_37 = range(0, 37)
        self.group_of_42 = range(0, 42)

    def test_routing_of_75_numbers(self):
        routes_of_25 = routing_logic.determine_routes(self.group_of_75)
        this(routes_of_25).should.equal([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]])
        routes_of_25_with_1 = routing_logic.determine_routes(self.group_of_76)
        this(routes_of_25_with_1).should.equal([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74],[75]])

    def test_routing_of_37_numbers(self):
        routes_of_37 = routing_logic.determine_routes(self.group_of_37)
        this(routes_of_37).should.equal([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [35], [36]])
        print routes_of_37

    def test_routing_of_42_numbers(self):
        routes_of_42 = routing_logic.determine_routes(self.group_of_42)
        this(routes_of_42).should.equal([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [40], [41]])