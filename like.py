import difflib

def similarity(str1, str2):
    """
    This function returns the similarity ratio between two strings.
    """
    seq = difflib.SequenceMatcher(None, str1, str2)
    percent = '{:.2%}'.format(seq.ratio())
    print(f"相似度：{percent}")
    print(type(percent))
    print(float(percent))
    return percent

similarity("你很好", "你很不好")