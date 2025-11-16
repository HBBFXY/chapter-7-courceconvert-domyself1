# 在这个文件中编写代码实现题目要求的功能 
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成

def transform_code(code: str) -> str:
    result = []
    word = ""       # 当前累积的单词（变量名/关键字等）

    def process_word(w):
        """处理一个单词：如果是保留字则保持原样，否则小写字母转大写"""
        if w in reserved_words:
            return w
        else:
            return "".join(ch.upper() if ch.islower() else ch for ch in w)

    for ch in code:
        if ch.isalpha() or ch == "_":   # 属于标识符的一部分
            word += ch
        else:
            # 遇到分隔符，需要处理之前的单词
            if word:
                result.append(process_word(word))
                word = ""
            result.append(ch)   # 非字母字符直接加入结果

    # 结束后可能还剩一个单词
    if word:
        result.append(process_word(word))

    return "".join(result)


# 读取 random_int.py
with open("random_int.py", "r", encoding="utf-8") as f:
    original_code = f.read()

# 转换
converted_code = transform_code(original_code)

# 保存到新文件
with open("converted_random_int.py", "w", encoding="utf-8") as f:
    f.write(converted_code)

print("转换完成！结果保存在 converted_random_int.py")
