import requests


class LeetCodeRequest:
    """
    用于发送LeetCode API请求的类。
    初始化时需要提供API请求的URL和请求头。
    """

    def __init__(self, url, headers):
        """
        初始化LeetCodeRequest类。
        参数:
        - url: API请求的URL。
        - headers: 请求的头信息，通常包含认证信息。
        """
        self.url = url
        self.headers = headers

    def send_request(self, query, variables, operation_name):
        """
        发送API请求并处理响应。

        参数:
        - query: GraphQL查询语句。
        - variables: 查询中使用的变量。
        - operation_name: 查询的操作名。

        返回:
        - 如果响应状态码为200，则返回响应的JSON数据。
        - 否则，打印错误信息并返回None。
        """
        # 准备API请求的数据
        data = {
            "query": query,
            "variables": variables,
            "operationName": operation_name
        }

        # 发送POST请求到LeetCode API
        response = requests.post(self.url, headers=self.headers, json=data)

        # 根据响应状态码处理响应
        if response.status_code == 200:
            return response.json()
        else:
            # 如果请求失败，打印错误信息并返回None
            print(f"请求失败，状态码: {response.status_code}")
            return None
