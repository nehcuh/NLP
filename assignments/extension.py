"""
模式匹配回答
"""

def is_variable(pat: str):
    """
    判断 pat 是否是需要匹配词，如果类似 ?X 这样的，符合条件
    """
    if pat[0] == "?" and all(a.isalpha() for a in pat[1:]):
        return True
    return False

def pat_match(pattern: list, saying: list):
    """
    匹配模式语句与输入语句，进行模式提取
    可进行多条件词匹配
    """
    if not pattern or not saying: return []
    if is_variable(pattern[0]):
        return [(pattern[0], saying[0])] + pat_match(pattern[1:], saying[1:])
    if pattern[0] != saying[0]:
        return []
    return pat_match(pattern[1:], saying[1:])

def pat_to_dict(patterns: list):
    """
    将所有匹配的单词对转换为 dict, 方便之后对语法进行替换
    """
    if not patterns: return None
    return {k: "".join(v) if isinstance(v, list) else v for k, v in patterns}

def sustitute(rules: list, parsed_rule: dict):
    """
    根据 parsed_rule 定义，对 rules 进行匹配替换
    :param rules: 需进行替换的语句
    :param parsed_rule: 替换对照表
    """
    if not rules or not parsed_rule: return None
    return [parsed_rule.get(rules[0], rules[0]) + sustitute(rules[1:], parsed_rule)]

def is_segment(seg: str):
    """
    判断是否段落匹配
    """
    if seg.startswith("?*") and all(a.isalpha() for a in seg[2:]):
        return True
    return False

def pat_match_with_seg(pattern: list, saying: list):
    """
    比对 pattern 与 saying，返回提取到的 segment
    """
    if not pattern or not saying: return []

    if is_variable(pattern[0]):
        return [(pattern[0], saying[0])] + pat_match_with_seg(pattern[1:], saying[1:])
    if is_segment(pattern[0]):
        match, index = segment_match(pattern, saying)

def segment_match(pattern: list, saying: list):
    """

    """
    pass
