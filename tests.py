import unittest
import requests


class ApiTest(unittest.TestCase):
    API_URL = #"your http://<hostname>:<port>"
    ALL_IMAGES_INFO_URL = "{}/image".format(API_URL)
    IMAGE_PREWIEW = "{}/images/".format(API_URL)


    def _get_image_url_for_prewiew(self, image_name):
        """Вспомогательная функция для формирования url картинки"""
        return "{}/{}".format(ApiTest.IMAGE_PREWIEW, image_name)

    def _get_image_url_for_delete(self, arg):
        """Вспомогательная функция для формирования url картинки"""
        return "{}?filename={}".format(ApiTest.ALL_IMAGES_INFO_URL, arg)

    def test_get_all_images_info(self):
        """Тестируем GET http://<hostname>:<port>/image"""
        r = requests.get(ApiTest.ALL_IMAGES_INFO_URL)
        self.assertEqual(r.status_code, 200)

    def test_prewiew_image(self):
        """Тестируем http://<hostname>:<port>/images/<image name>.jpg"""
        valid_image_name = #your valid image from 'images' folder
        invalid_image_name = #invalid image name
        r = requests.get(self._get_image_url_for_prewiew(valid_image_name))
        fail = requests.get(self._get_image_url_for_prewiew(invalid_image_name))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(fail.status_code, 404)

    def test_post_image(self):
        """Тестируем POST http://<hostname>:<port>/image"""
        r = requests.post(ApiTest.ALL_IMAGES_INFO_URL, json=# your JSON with base64 string)
        self.assertEqual(r.status_code, 201)

    def test_delete_image(self):
        """Тестируем http://<hostname>:<port>/image?filename=<filename>.jpg"""
        valid_arg = #your valid image from 'images' folder
        invalid_arg = #invalid image name
        r = requests.delete(self._get_image_url_for_delete(valid_arg))
        fail = requests.delete(self._get_image_url_for_delete(invalid_arg))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(fail.status_code, 400)
