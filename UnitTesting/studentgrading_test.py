def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
import unittest

class TestGrading(unittest.TestCase):
    def test_grades(self):
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(85), "B")
        self.assertEqual(get_grade(75), "C")
        self.assertEqual(get_grade(65), "D")
        self.assertEqual(get_grade(50), "F")
        
        self.assertNotEqual(get_grade(65), "A")
        self.assertNotEqual(get_grade(50), "B")

if __name__ == '__main__':
    unittest.main()
