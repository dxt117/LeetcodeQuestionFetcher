import requests
import json
# re 模块提供了正则表达式的相关功能，用于字符串的匹配、搜索、替换等操作。
import re
# time 模块提供了与时间相关的函数，用于获取当前时间、等待一段时间等。
import time
# os 模块提供了与操作系统交互的功能，如文件、目录等。
import os

# 请求的URL
url = "https://leetcode.cn/graphql/"

# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "gr_user_id=c5b2ee93-faaa-49c4-baee-e6f0ca114786; _bl_uid=nFl2Oyp0e26nRzstn139wde8wbRq; a2873925c34ecbd2_gr_last_sent_cs1=117-hk; csrftoken=HnfqM4i4h3GONDVaogNxUtA9on2ondHxIQz5cQREGkpP5wg2DDkzV2YwkaQqPoTu; tfstk=fKHoBrXF-bPSfWC0mIyWTpRcF0RYFgwQR2BLJJUegrzbpbK7Jy0n5VVEeDezKy0El_FLJz3Dxqus2WerKj6nfDMJVJK7F0wQLFL9B9mSVJZCskrtK-P4bk9day5yZQ5rQFL9BKnKkDpwW437H650Arrz4_rymZrQu65r8zPVulq_LJyE8oo4AkBU8TrU0-zbYJzE8JlPI_ztLfk2yQxuPJrp_AquZyXLo9mI3OF77T4Vp9Uuq7fm4rXFLxcX_YJ_zCsYR8US2u0BCTwztfiLx4vlU2mshqqq7pXTzmit67My9OFgnzVIU0YkKmD3r5kziMBij8ZE8WcXSOEuejViEbtCu0uTrfySvGY-m5c01oPVx_y-6cHQ_YJl5rF_x4Ux7dW03WSPXs5wRSBQ0HHVO6Nzco4tJG5Y6R8RiGKDm1nQaoZ_WnxcO6Nzco49mnftd7rbfPC..; sl-session=OYNxWR4AU2ccdWePypy9zQ==; LEETCODE_SESSION=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiNjgzMjMzMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDQ1OGIyZmUzOGY3YzYyZmI4NGM0ZmU1ZGJhZTU5NDMwNzAxN2NlM2JmZWMxYmEwNjJmMDlkNTljMmE1OGQxMyIsImlkIjo2ODMyMzMyLCJlbWFpbCI6IiIsInVzZXJuYW1lIjoiMTE3LWhrIiwidXNlcl9zbHVnIjoiMTE3LWhrIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY24vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy8xMTctaGsvYXZhdGFyXzE3MDIzMDc5NTIucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsImRldmljZV9pZCI6ImM4NzhlODhlNTM5ZWE1MWE2MTljM2I0YjEwZjgyYzdkIiwiaXAiOiIxMTEuMTguOTIuMTAwIiwiX3RpbWVzdGFtcCI6MTczMzAyOTYxOS.4.1733489629; Hm_lvt_f0faad39bcf8471e3ab3ef70125152c3=1733031858,1733406426,1733408275,1733489629; Hm_lpvt_f0faad39bcf8471e3ab3ef70125152c3=1733489629; HMACCOUNT=08581CDBCE7561F7; _gat=1; _ga=GA1.1.682246719.1720544509; _ga_PDVPZYN3CW=GS1.1.1733489629.22.1.1733489665.24.0.0",
    "Origin": "https://leetcode.cn",
    "Referer": "https://leetcode.cn/problems/string-to-integer-atoi/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "authorization;": "",
    "baggage": "sentry-environment=production,sentry-release=8f62ed3b,sentry-transaction=%2Fproblems%2F%5Bslug%5D%2F%5B%5B...tab%5D%5D,sentry-public_key=1595090ae2f831f9e65978be5851f865,sentry-trace_id=beeb12a8419843debf1a69ba0c5ba17e,sentry-sample_rate=0.03",
    "content-type": "application/json",
    "random-uuid": "d3aecd55-2f9d-91f8-493b-c83612e71311",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sentry-trace": "beeb12a8419843debf1a69ba0c5ba17e-9f96529e62e742f2-0",
    "x-csrftoken": "HnfqM4i4h3GONDVaogNxUtA9on2ondHxIQz5cQREGkpP5wg2DDkzV2YwkaQqPoTu"
}

# 原始查询语句：查询题目描述
origin_query_description = '''
    query questionDetail($titleSlug: String!) {
  languageList {
    id
    name
    verboseName
  }
  statusList {
    id
    name: translatedName
  }
  question(titleSlug: $titleSlug) {
    title
    titleSlug
    questionId
    questionFrontendId
    questionTitle
    translatedTitle
    content
    translatedContent
    categoryTitle
    difficulty
    stats
    style
    contributors {
      username
      profileUrl
      avatarUrl
    }
    book {
      id
      bookName
      pressName
      source
      shortDescription
      fullDescription
      bookImgUrl
      pressImgUrl
      productUrl
    }
    companyTagStatsV2
    topicTags {
      name
      slug
      translatedName
    }
    similarQuestions
    mysqlSchemas
    dataSchemas
    frontendPreviews
    likes
    dislikes
    isPaidOnly
    status
    boundTopicId
    enableTestMode
    metaData
    enableRunCode
    enableSubmit
    envInfo
    isLiked
    nextChallengePairs
    libraryUrl
    hints
    codeSnippets {
      code
      lang
      langSlug
    }
    jsonExampleTestcases
    exampleTestcases
    sampleTestCase
    hasFrontendPreview
    editorType
  }
}
'''
# 原始查询语句：查询题目标题
origin_query_title_slug = '''
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    hasMore
    total
    questions {
      acRate
      difficulty
      freqBar
      frontendQuestionId
      isFavor
      paidOnly
      solutionNum
      status
      title
      titleCn
      titleSlug
      topicTags {
        name
        nameTranslated
        id
        slug
      }
      extra {
        hasVideoSolution
        topCompanyTags {
          imgUrl
          slug
          numSubscribed
        }
      }
    }
  }
}
'''


# 根据id查题目标题
def get_question_title_by_id(question_id):
    # 查询语句
    query_title_slug = '''
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        questions {
          titleCn
          titleSlug
        }
      }
    }
    '''
    # 请求参数
    query_description_data = {
        "query": query_title_slug,
        "variables": {
            "categorySlug": "all-code-essentials",
            "skip": question_id - 1,
            "limit": 1,
            "filters": {}
        },
        "operationName": "problemsetQuestionList"
    }
    # 发送POST请求
    response = requests.post(url, headers=headers, json=query_description_data)
    # 处理响应
    if response.status_code == 200:
        # 原始数据
        # print(response.json())
        # 格式化输出
        # print(json.dumps(response.json(), indent=4))
        # print(response.json()['data']['problemsetQuestionList']['questions'][0]['titleSlug'])
        return response.json()['data']['problemsetQuestionList']['questions'][0]['titleSlug']
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return ""


# 根据标题查题目描述
def get_question_desc_by_tite(question_title_slug):
    # 查询语句
    query_description = '''
        query questionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        translatedTitle
        translatedContent
        companyTagStatsV2
        libraryUrl
        hints
        codeSnippets {
          code
          lang
          langSlug
        }
        jsonExampleTestcases
        exampleTestcases
        sampleTestCase
      }
    }
    '''
    # 请求参数
    query_description_data = {
        "query": query_description,
        "variables": {
            "titleSlug": question_title_slug
        },
        "operationName": "questionDetail"
    }
    # 发送POST请求
    response = requests.post(url, headers=headers, json=query_description_data)
    # 处理响应
    if response.status_code == 200:
        # 原始数据
        # print(response.json())
        # 格式化输出
        # print(json.dumps(response.json(), indent=4))
        return response.json()
    else:
        print(f"请求失败，状态码: {response.status_code}")


# 文件开头的时间注释
def create_by():
    return f"//\n// Created by DXT on {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}.\n//\n\n"


# 检查目录是否存在
def check_dir_exists(fp):
    # 获取文件所在的目录
    directory = os.path.dirname(fp)
    # 如果目录不存在，则创建目录
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"\033[92m提示：目录 {directory} 创建成功。\033[0m")
    else:
        print(f"\033[91m告警: 目录 {directory} 已经存在。\033[0m")


# 使用正则表达式去除 <pre> 标签并将其中每一行用 <p> 标签包裹
def remove_replace_tags(content, remove_tag, add_tag_each_line_in=''):
    pattern = re.compile(rf'<{remove_tag}>(.*?)</{remove_tag}>', re.DOTALL)

    def replace_match(match):
        # 获取标签内的内容
        inner_content = match.group(1)
        # 去除前后的空白字符
        inner_content = inner_content.strip()
        # 将每一行用 <p> 标签包裹
        rows = inner_content.split('\n')
        wrapped_lines = [f'<{add_tag_each_line_in}>{row}</{add_tag_each_line_in}>' for row in rows if row.strip()]
        return '\n'.join(wrapped_lines)

    # 替换标签及其内容
    return pattern.sub(replace_match, content)


# 使用正则表达式在“<p><strong>(.*?)示例(.*?)</strong>”前添加空行
def add_empty_paragraph(text):
    pattern = re.compile(r'(<p><strong>(.*?)示例(.*?)</strong></p>)')
    replacement = r'<p>&nbsp;</p>\n\1'
    return re.sub(pattern, replacement, text)


# 将内容写入文件
def write_to_file(fp, content, code_template=''):
    # 检查目录是否存在, 如果不存在则创建目录
    check_dir_exists(fp)
    # 检查文件是否存在
    if os.path.exists(fp):
        print(f"\033[91m告警: 文件 {fp} 已经存在。\033[0m")
        return
    # 打开文件，如果文件不存在则创建文件,并设置编码为utf-8,如果存在则告警
    with open(fp, 'a+') as file:
        # 追加时间注释
        file.write(create_by())
        file.seek(0, 0)
        # 追加其他内容
        file.write(f"/**\n{content}\n */\n\n")
        # 追加代码模板
        file.write(code_template)
        print(f"\033[92m提示：文件 {fp} 保存成功。\033[0m")


# 检测内容是否包含img标签，如果有则下载图片到本地
def check_and_download_img(content, img_p):
    # re 模块提供了正则表达式的相关功能，用于字符串的匹配、搜索、替换等操作。
    import re
    # 匹配img标签
    img_tags = re.findall(r'<img.*?>', content)
    # 遍历img标签，下载图片到本地
    for img_tag in img_tags:
        # 提取图片链接
        img_url = re.search(r'src="(.*?)"', img_tag).group(1)
        # 下载图片到本地
        response = requests.get(img_url)
        if response.status_code == 200:
            # 提取图片名称
            img_name = re.search(r'/([^/]+)$', img_url).group(1)
            # 图片文件路径
            img_path = img_p + "\\" + img_name
            # 检查目录是否存在, 如果不存在则创建目录
            check_dir_exists(img_path)
            # 检查图片文件是否存在
            if not os.path.exists(img_path):
                # 保存图片到本地
                with open(f'{img_path}', 'wb') as f:
                    f.write(response.content)
                    print(f"\033[92m提示：图片 {img_path} 保存成功。\033[0m")
            else:
                print(f"\033[91m告警: 图片 {img_path} 已经存在。\033[0m")
            # 去除img标签
            content = content.replace(img_tag, '')
    return content


if __name__ == '__main__':
    # 根据题目id查题目标题
    # TODO 每次生成题目，ID需要修改（否则题目内容不会改变）
    question_num_id = 10
    titleSlug = get_question_title_by_id(question_num_id)
    # 根据题目标题查题目描述
    json_data = get_question_desc_by_tite(titleSlug)
    # 提取题目描述内容
    translated_content = json_data["data"]["question"]["translatedContent"]
    # 提取不同语言示例代码 0.c++ 1.java 2.python 3.python3 4.c 5.c# 6.JavaScript
    c_code_template = json_data["data"]["question"]["codeSnippets"][4]['code']
    translated_content = remove_replace_tags(translated_content, 'pre', 'p')
    translated_content = add_empty_paragraph(translated_content)
    # 题目以及文件名
    # TODO 每次生成题目，文件名需要修改（否则会覆盖原文件内容） 在此设置根据id 生成文件名
    question_name_id = f"question0{question_num_id}"
    # 写入到指定C文件
    file_dir = f"E:\\Projects\\CProjects\\LeetCode\\questions\\{question_name_id}"
    file_dir_img = file_dir + "\\img"
    # 检测内容是否包含img标签，如果有则下载图片到本地
    translated_content = check_and_download_img(translated_content, file_dir_img)
    # 将内容整理为C语言文档注释格式
    formatted_content = []
    lines = translated_content.splitlines()
    for line in lines:
        formatted_content.append(f" * {line}")
    formatted_content = "\n".join(formatted_content)
    # 将内容写入文件
    c_file_name = file_dir + "\\" + question_name_id + ".c"
    write_to_file(c_file_name, formatted_content, c_code_template)
