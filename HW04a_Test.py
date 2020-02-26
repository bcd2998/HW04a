import unittest, json
from unittest.mock import patch, Mock
import HW04a
class GitHubTest(unittest.TestCase):
    @patch('HW04a.GitHub')
    def test1_correctinput(self, mockGithubFunc):
        mockGithubFunc.return_value = ['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: threads-of-life Number of commits: 1']
        self.assertEqual(HW04a.GitHub('richkempinski'), ['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: threads-of-life Number of commits: 1'])
        # print(result)
        # self.assertEqual(GitHub('richkempinski'), ['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: threads-of-life Number of commits: 1'])
    @patch('HW04a.GitHub')
    def test2_correctinput(self, mockGithubFunc):
        mockGithubFunc.return_value = ['Repo: SSW-567 Number of commits: 8', 'Repo: SSW567_HW02a-TriangleTesting Number of commits: 15']
        self.assertEqual(HW04a.GitHub('bcd2998'), ['Repo: SSW-567 Number of commits: 8', 'Repo: SSW567_HW02a-TriangleTesting Number of commits: 15'])

    #     self.assertEqual(GitHub('bcd2998'), ['Repo: SSW-567 Number of commits: 8', 'Repo: SSW567_HW02a-TriangleTesting Number of commits: 15'])
    @patch('HW04a.GitHub')
    def test3_invalidinput(self, mockGithubFunc):
        mockGithubFunc.return_value = 'This is not an account'
        self.assertEqual(HW04a.GitHub('bubblyBoo'), 'This is not an account')
    
    @patch('HW04a.GitHub')
    def test4_invalidinput(self, mockGithubFunc):
        mockGithubFunc.return_value = 'This is not an account'
        self.assertEqual(HW04a.GitHub('True'), 'This is not an account')

if __name__ == "__main__":
    unittest.main()
