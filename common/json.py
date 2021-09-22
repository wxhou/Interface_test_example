"""
序列化和反序列化类
"""
import json


def loads(content: str):
    """
    反序列化
        json对象 -> python数据类型
    """
    return json.loads(content)


def dumps(content, ensure_ascii=True):
    """
    序列化
        python数据类型 -> json对象
    """
    return json.dumps(content, ensure_ascii=ensure_ascii)


def is_json_str(string: str):
    """验证是否为json字符串"""
    try:
        json.loads(string)
        return True
    except:
        return False
