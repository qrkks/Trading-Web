from django.test import TestCase, Client

class ContactViewTest(TestCase):
    def setUp(self):
        # 设置测试客户端
        self.client = Client()

    def test_contact_view_regular_request(self):
        # 使用测试客户端发送GET请求
        response = self.client.get('/contact/')

        # 检查响应状态码
        self.assertEqual(response.status_code, 200)
        # 检查是否使用了正确的模板
        self.assertTemplateUsed(response, 'pages/contact.html')

    def test_contact_view_hx_request(self):
        # 发送HX请求
        response = self.client.get('/contact/', HTTP_HX_REQUEST='true')

        # 检查响应状态码
        self.assertEqual(response.status_code, 200)
        # 这里可以添加更多的检查，例如响应内容等

        # 检查响应内容是否包含特定的字符串或HTML元素
        # 例如，检查响应中是否包含特定的消息或HTML标签
        self.assertIn("contact us", response.content.decode())
        self.assertIn("15588639091", response.content.decode())

        # 或者使用 assertContains 检查响应是否包含特定的文本
        self.assertContains(response, "contact us", html=True)
        self.assertContains(response, "15588639091", html=True)

# 这里可以添加更多测试用例
