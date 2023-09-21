from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):

        testLat = 5
        testLon = 5

        testPosition = Position(testLat, testLon)
        self.assertEqual(testPosition.lat, testLat)
        self.assertEqual(testPosition.lon, testLon)
        #ARBITRARY_NAME = "MyName"
        #testobj = Character(ARBITRARY_NAME)
        #self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_isValid(self):
        testLat = -1
        testLon = 10

        testPosition = Position(testLat, testLon)
        self.assertFalse(testPosition.isValid())

        testLat = 5
        testLon = 5
        testPosition = Position(testLat, testLon)
        self.assertTrue(testPosition.isValid())