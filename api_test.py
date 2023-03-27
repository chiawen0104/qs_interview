import unittest
import requests
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# unit testing
class TestAPI(unittest.TestCase):

    def test_generate_image(self):
        # 測試正常情況下是否能夠產生圖片
        response = requests.get('http://localhost:8000/image?width=400&height=300')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'image/png')
        # 將回傳的二進制字串轉換成 PIL Image 物件
        img = Image.open(BytesIO(response.content))
        self.assertEqual(img.size, (400, 300))

    def test_invalid_params(self):
        # 測試當參數錯誤時是否會回傳錯誤訊息
        response = requests.get('http://localhost:8000/image?width=0&height=0')
        self.assertEqual(response.status_code, 400)
        response = requests.get('http://localhost:8000/image?width=400&height=0d')
        self.assertEqual(response.status_code, 400)
        response = requests.get('http://localhost:8000/image?width=a&height=b')
        self.assertEqual(response.status_code, 400)


# e2e testing
class TestAPIE2E(unittest.TestCase):

    def setUp(self):
        path = Service(r'./chromedriver')
        self.driver = webdriver.Chrome(service=path)

    def tearDown(self):
        self.driver.quit()

    def test_valid_params(self):
        # 測試傳遞有效的寬度和高度
        url = 'http://localhost:8000/image?width=400&height=300'
        self.driver.get(url)
        time.sleep(1.5)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        img = Image.open(BytesIO(response.content))
        self.assertEqual(img.size, (400, 300))

    def test_zero_params(self):
        # 測試傳遞寬度和高度等於0的情況
        url = 'http://localhost:8000/image?width=0&height=0'
        self.driver.get(url)
        time.sleep(1.5)
        response = requests.get(url)
        # print(response.text)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, 'Zero Parameters.')

    def test__invalid_params(self):
        # 測試傳遞無效的寬度和高度（字串、負數）
        url = 'http://localhost:8000/image?width=-300&height=abc123'
        self.driver.get(url)
        time.sleep(1.5)
        response = requests.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, 'Invalid Parameters.')


if __name__ == '__main__':
    unittest.main()
