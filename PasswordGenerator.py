# coding:utf8
import random
import string

charset = {
    'capital':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'lowercase':'abcdefghijklmnopqrstuvwxyz',
    'digit':'0123456789',
    'specific_symbol':'\!@#$%^&*?/.',
}

def get_chars(charset_name, num):
    charset_name_chars = charset[charset_name]
    temp_chars = []
    while num > len(charset_name_chars):
        temp_chars += random.sample(charset_name_chars, len(charset_name_chars))
        num -= len(charset_name_chars)
    temp_chars += random.sample(charset_name_chars, num % len(charset_name_chars))
    return temp_chars


def get_password(length=16, specific_symbol=1, capital=1, lowercase=1, digit=1):
    if length < 6:
        print u"密码长度最小为 6"
        return ''

    charset_flag = {
        'capital':capital,
        'lowercase':lowercase,
        'digit':digit,
        'specific_symbol':specific_symbol,
    }
    password = ''

    t = specific_symbol + capital + lowercase + digit

    specific_symbol_num = length / t * specific_symbol
    capital_num = length / t * capital
    lowercase_num = length / t * lowercase
    digit_num = length / t * digit

    specific_symbol_chars = get_chars('specific_symbol', specific_symbol_num)
    capital_chars = get_chars('capital', capital_num)
    lowercase_chars = get_chars('lowercase', lowercase_num)
    digit_chars = get_chars('digit', digit_num)

    other_num = length % t
    other_key = random.sample([x for x in charset_flag.keys() if x], 1)[0]
    other_chars = get_chars(other_key, other_num)

    all_chars = specific_symbol_chars + capital_chars + lowercase_chars + digit_chars + other_chars

    random.shuffle(all_chars)
    return ''.join(all_chars)

def get_many_password(num=10):
    for i in range(num):
        print get_password(10)
    return

if __name__ == '__main__':
    print get_password(16)
    #
    #get_many_password()
