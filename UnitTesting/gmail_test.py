import unittest

def gmail(n):
    if ".com" in n and "@" in n:
        return True
    else:
        return False
    

class TestGmail(unittest.TestCase):
    def test_valid_gmail(self):
        self.assertTrue(gmail("example@gmail.cm"))
        self.assertTrue(gmail("user.name@domain.com"))

    def test_missing_dotcom(self):
        self.assertFalse(gmail("example@gmail"))

    def test_empty_string(self):
        self.assertFalse(gmail(""))

    
if __name__ == "__main__":
    unittest.main()
