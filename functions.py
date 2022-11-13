def split_text(text, split_len):
    result = []
    start = 0
    txt: str = text[start:start + split_len]
    while len(txt):
        end = txt.rfind('.', start, start + split_len) + 1
        end = start + split_len + 1 if end == 0 else end
        txt = txt[:end]
        result.append(txt)
        text = text[end:]
        txt: str = text[start:start + split_len]
    return result



