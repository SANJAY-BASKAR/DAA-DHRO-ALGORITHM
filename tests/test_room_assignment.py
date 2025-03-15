import unittest
from dhro_algorithm import assign_rooms

class TestRoomAssignment(unittest.TestCase):
    def test_room_distribution(self):
        time_slots = {'Math': 0, 'Physics': 1}
        exams = {'Math': ['Alice', 'Bob'], 'Physics': ['Charlie']}
        rooms = assign_rooms(time_slots, exams)
        self.assertTrue(len(rooms) > 0)

if __name__ == '__main__':
    unittest.main()
