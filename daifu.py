# -*- coding:utf-8 -*-

daifu = '歪比巴卜'
decode_table = dict((daifu[i], 2**(3-i)) for i in range(4))
encode_table = dict((val, key) for key, val in decode_table.items())


def hextodaifu(hexcode: int):
    temp = ''
    for val in encode_table:
        if hexcode & val:
            temp += encode_table[val]
            hexcode ^= val
    return temp


def daifu_encode(plain: str):
    plain_bytes = plain.encode('utf-8')
    code_list = ['歪比歪比']
    for twohex in plain_bytes:
        onehex1 = twohex//16
        onehex2 = twohex % 16
        code_list.append(hextodaifu(onehex1))
        code_list.append(hextodaifu(onehex2))
    code_list.append('歪比巴卜')
    return ' '.join(code_list)


def daifu_decode(code: str):
    code_list = code.split(' ')
    if not (len(code_list) >= 2 and code_list.pop(0) == '歪比歪比' and code_list.pop() == '歪比巴卜'):
        return ''
    hex_text = ''
    for code in code_list:
        temp = 0
        for i in code:
            temp += decode_table[i]
        hex_text += hex(temp)[-1]
    return bytes.fromhex(hex_text).decode('utf-8')


if __name__ == "__main__":
    daifu_text = daifu_encode("你好")
    print(daifu_text)
    print(daifu_decode(daifu_text))
