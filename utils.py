import requests
# re 模块提供了正则表达式的相关功能，用于字符串的匹配、搜索、替换等操作。
import re
# time 模块提供了与时间相关的函数，用于获取当前时间、等待一段时间等。
import time
# os 模块提供了与操作系统交互的功能，如文件、目录等。
import os


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
def write_to_cfile(fp, content, code_template=''):
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


# 将注释转换py注释格式
def translate_to_py_comment(content):
    # 处理单行注释
    content = re.sub(r'//\s*(.*)', r'# \1', content)
    # 处理多行注释
    content = re.sub(r'/\*\s*(.*?)\s*\*/', lambda match: '"""' + match.group(1).replace('\n', '\n') + '"""', c_code,
                    flags=re.DOTALL)
    return content