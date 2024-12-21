from leetcode_request import LeetCodeRequest
from config import URL, HEADERS, QUERY_DESCRIPTION, QUERY_TITLE_SLUG
from utils import remove_replace_tags, add_empty_paragraph, check_and_download_img, write_to_cfile

if __name__ == '__main__':
    # 初始化请求
    lc_request = LeetCodeRequest(URL, HEADERS)

    # 根据题目id查题目标题
    # TODO 每次生成题目，ID需要修改（否则题目内容不会改变）
    question_num_id = 10
    # 查询参数
    variables_title_slug = {
        "categorySlug": "all-code-essentials",
        "skip": question_num_id - 1,
        "limit": 1,
        "filters": {}
    }
    # 发送请求
    # 查询操作名：problemsetQuestionList
    response_title_slug = lc_request.send_request(QUERY_TITLE_SLUG, variables_title_slug, "problemsetQuestionList")
    # 获取题目标题
    titleSlug = response_title_slug['data']['problemsetQuestionList']['questions'][0]['titleSlug']

    # 根据题目标题查题目描述
    variables_description = {
        "titleSlug": titleSlug
    }
    # 发送请求
    # 查询操作名：questionDetail
    response_description = lc_request.send_request(QUERY_DESCRIPTION, variables_description, "questionDetail")
    # 获取题目描述
    translated_content = response_description["data"]["question"]["translatedContent"]
    # 提取不同语言示例代码 0.c++ 1.java 2.python 3.python3 4.c 5.c# 6.JavaScript
    # 在此以提取4.c代码模板为例
    # TODO 生成不同语言代码，需要修改对应的下标
    c_code_template = response_description["data"]["question"]["codeSnippets"][4]['code']
    # 移除标签
    translated_content = remove_replace_tags(translated_content, 'pre', 'p')
    # 添加空行
    translated_content = add_empty_paragraph(translated_content)

    # 题目以及文件名
    # 每次生成题目，文件名需要修改（否则会覆盖原文件内容） 在此设置根据id 生成文件名
    question_name_id = f"question0{question_num_id}"
    # 写入到指定文件
    file_dir = f".\\LeetCode\\questions\\{question_name_id}"
    file_dir_img = file_dir + "\\img"
    # 检测内容是否包含img标签，如果有则下载图片到本地
    translated_content = check_and_download_img(translated_content, file_dir_img)
    # 将内容整理为C语言文档注释格式
    formatted_content = []
    lines = translated_content.splitlines()
    for line in lines:
        formatted_content.append(f" * {line}")
    formatted_content = "\n".join(formatted_content)
    # 将内容写入c文件
    # TODO 此处需要修改，这里写入的是c文件，不同语言注释不同，需要编写对应文件
    c_file_name = file_dir + "\\" + question_name_id + ".c"
    write_to_cfile(c_file_name, formatted_content, c_code_template)
