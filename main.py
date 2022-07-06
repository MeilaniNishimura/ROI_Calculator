import unittest
from ROI_calculator import Property, User
import uuid

class MakingTest(unittest.TestCase):

    def test_income(self):
        property = Property("lakehouse")
        property.income_info()
        self.assertEquals(property.total_income, property.total_income )

    def test_expenses(self):
        property1 = Property()
        property1.expenses_info()
        self.assertEquals(property1.total_expenses, property1.total_expenses)

unittest.main(MakingTest())