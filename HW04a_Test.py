import unittest
from HW04a import GitHub

class GitHubTest(unittest.TestCase):
    def test1_correctinput(self):
        self.assertEqual(GitHub('richkempinski'), ['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: threads-of-life Number of commits: 1'])

    def test2_correctinput(self):
        self.assertEqual(GitHub('bcd2998'), ['Repo: SSW-567 Number of commits: 8', 'Repo: SSW567_HW02a-TriangleTesting Number of commits: 15'])

    def test3_invalidinput(self):
        self.assertEqual(GitHub('1'), 'This is not an account')

    def test4_invalidinput(self):
        self.assertEqual(GitHub(True), 'This is not an account')

    def test5_invalidinput(self):
        self.assertEqual(GitHub(21), 'This is not an account')

if __name__ == "__main__":
    unittest.main()
