import requests,ddt,unittest,json
data=[200,201,200,201]
@ddt.ddt
class DoubanTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def beij(self):
        cliner=requests.get('https://api.douban.com/v2/user/q')
        m=cliner.status_code
        return m
    @ddt.data(*data)
    def test1(self,data):
        m=self.beij()
        print(data)
        self.assertEqual(m,data)
if __name__ =='__main__':
    unittest.main()