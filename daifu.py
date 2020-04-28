# -*- coding:utf-8 -*-

daifu = '歪比巴卜'
decode_table = dict((daifu[i], i) for i in range(4))
print(decode_table)
encode_table = dict((val, key) for key, val in decode_table.items())
print(encode_table)


def daifu_encode(plain: bytes, encoding: str = 'utf-8') -> bytes:
    cipher = ''
    # print(list(plain))
    for twohex in plain:
        halfhex = twohex >> 6
        cipher += encode_table[halfhex]
        halfhex = twohex >> 4 & 3
        cipher += encode_table[halfhex]
        halfhex = twohex >> 2 & 3
        cipher += encode_table[halfhex]
        halfhex = twohex & 3
        cipher += encode_table[halfhex]
    return cipher.encode(encoding)


def daifu_decode(cipher: bytes, encoding: str = 'utf-8') -> bytes:
    try:
        cipher_text = cipher.decode(encoding)
    except:
        raise Exception("Wrong cipher!")
    length = len(cipher_text)
    if length % 4:
        raise Exception("Wrong cipher!")
    plain_hex_list = []
    for i in range(length//4):
        temp = 0
        for j in range(4):
            temp <<= 2
            temp += decode_table[cipher_text[i*4+j]]
        plain_hex_list.append(temp)
    # print(plain_hex_list)
    return bytes(plain_hex_list)


if __name__ == "__main__":
    plain = "你好"
    cipher = daifu_encode(plain.encode('utf-8')).decode('utf-8')
    print(cipher)
    print(daifu_decode(cipher.encode('utf-8')).decode('utf-8'))
