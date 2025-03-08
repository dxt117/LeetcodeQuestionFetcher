# -*- coding: utf-8 -*-
from config.config import URL, QUERY_TITLE_SLUG
from config.headers import HEADERS
from leetcode_request import LeetCodeRequest


# 导入生成的 headers.py 文件


# 将header.txt请求头信息转换为 Python 字典，并保存到 headers.py 文件中
def header_convert():
    # 初始化一个空字典来存储请求头信息
    headers = {}

    # 打开包含请求头信息的文本文件，以读取模式打开
    with open('header.txt', 'r', encoding='utf-8') as file:
        # 逐行读取文件内容
        for line in file:
            # 跳过以 'POST' 开头的行，因为这是请求行而不是请求头
            if line.startswith('POST'):
                continue
            # 检查行中是否包含冒号，以此判断是否为有效的请求头行
            if ':' in line:
                # 按冒号分割行内容，得到键和值
                key, value = line.split(':', 1)
                # 去除键和值两端的空白字符
                key = key.strip()
                value = value.strip()
                # 将处理后的键值对添加到 headers 字典中
                headers[key] = value

    with open('../config/headers.py', 'w', encoding='utf-8') as output_file:
        # 写入字典的变量名和左花括号
        output_file.write("HEADERS = {\n")
        # 遍历 headers 字典中的键值对
        for key, value in headers.items():
            # 跳过 Accept-Encoding
            if key == "Accept-Encoding":
                continue
            # 对值中的双引号进行转义处理
            value = value.replace('"', '\\"')
            # 写入键值对，确保键和值都用双引号包裹
            output_file.write(f'    "{key}": "{value}",\n')
        # 写入字典的右花括号
        output_file.write("}")


# =================================================测试生成的 headers 是否可以正常请求======================================

# 调用 header_convert 函数进行转换
header_convert()
# 初始化请求
lc_request = LeetCodeRequest(URL, HEADERS)

# 请求参数  测试获取第一题的标题
parameter = {
    "categorySlug": "all-code-essentials",
    "skip": 0,
    "limit": 1,
    "filters": {}
}
# 发送测试请求
# 查询操作名：problemsetQuestionList
response_title_slug = lc_request.send_request(QUERY_TITLE_SLUG, parameter, "problemsetQuestionList")

# 获取题目标题
titleSlug = response_title_slug['data']['problemsetQuestionList']['questions'][0]['titleSlug']
# 打印标题
print("\033[92m生成请求头配置成功\033[0m")
