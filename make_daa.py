import random


def gen_ask_no_product():
    sanpham = ['Tivi', 'Tủ lạnh', 'máy giặt', 'Điều hòa', 'bóng đèn', 'xà bông', 'bếp', 'xe máy', 'xe đạp',
               'lò vi sóng', 'quạt', 'giày', 'dép', 'quần áo', 'điện thoại', 'máy ảnh', 'máy in'
               'Bếp ga', 'Bếp điện', 'xe đạp', 'điện thoại', 'xoong', 'nồi', 'chảo', 'bảng đen', 'máy lọc nước']
    strings = ['- Shop có kinh doanh [{}](product) không\n', '- Mình muốn mua [{}](product)\n', '- Shop có bán [{}](product)\n',
              '- Shop có [{}](product) không\n']
    res = ''
    for y in sanpham:
        string = random.choice(strings)
        a = string.format(y)
        res += a
    print(res)
    return res


def gen_ask_payment():
    string = "- {} {} như nào\n"
    text = ["Em", "Mình", "Tôi", "Anh", "Chị", "Hình thức"]
    verb = ["Thanh toán", "Giao dịch", "Trả tiền"]
    res = ''
    for x in text:
        for y in verb:
            a = string.format(x, y)
            res += a
    return res

def gen_ask_product():
    strings = ["- Giới thiệu mình sản phẩm [{}](product)\n", "-Bên shop có những [{}](product) nào\n", "- Mình cần thông tin về [{}](product)\n",
               "- Mình muốn mua [{}](product)\n", "- Bạn tư vấn cho mình một vài mẫu [{}](product)\n", "- Có {} không shop\n", "- Có [{}](product) không bạn\n",
               "- Mình đang phân vân không biết mua [{}](product) nào\n"]
    product = ['Bàn phím', 'Chuột', "Laptop", "Máy tính xách tay", "PC", "Màn Hình"]
    res = ''
    for string in strings:
        for p in product:
            temp = string.format(p)
            res += temp
    print(res)
    return res

def gen_ask_product_with_brand():
    strings = ["- Giới thiệu mình sản phẩm [{}](product) [{}](brand)\n", "-Bên shop có những [{}](product) [{}](brand) nào\n", "- Mình cần thông tin về [{}](product) [{}](brand)\n",
               "- Mình muốn mua [{}](product) [{}](brand)\n", "- Bạn tư vấn cho mình một vài mẫu [{}](product) [{}](brand)\n", "- Có [{}](product) [{}](brand) không shop\n", "- Có [{}](product) [{}](brand) không bạn\n",
               "- Mình đang phân vân không biết mua [{}](product) [{}](brand) nào\n"]
    product = ['Bàn phím', 'Chuột', "Laptop", "Máy tính xách tay", "PC", "Màn Hình"]
    brands = ['LG', 'Lenovo', 'Logitech', 'Gigabit', 'Acer', 'Asus']
    res = ''
    for string in strings:
        for p in product:
            for b in brands:
                temp = string.format(p, b)
                res += temp
    print(res)
    return res
def gen_complain():
    product = ['Bàn phím', 'Chuột', "Laptop", "Máy tính xách tay", "PC", "Màn Hình", "Sản Phẩm"]
    strings = ["- [{}](product) quá {}\n", '- [{}](product) dùng quá {}\n', "- Mới mua nhưng nhận thấy [{}](product) này chả thích\n",]
    types = ['chán', 'tệ', 'không tốt', 'không ra gì']
    res = ""
    for string in strings:
        for p in product:
            for t in types:
                temp = string.format(p, t)
                res += temp
    print(res)
    return res

def gen_stories(number):
    res = ""
    intents = get_intent()
    for i in range(number):
        res_ = "- story: sample{}\n".format(i) + "  steps:\n"
        num_con = random.randint(2, 8)
        for j in range(num_con):
            intent = random.choice(intents)
            action = "utter_"+intent
            if (j == 0 and intent == 'bye') or (j == 0 and intent == 'thank'):
                continue
            intent_template = "  - intent: {}\n".format(intent)
            action_template = "  - action: {}\n".format(action)
            res_ += intent_template
            res_ += action_template
            if intent == "complain" or intent == "bye":
                break
        res += '\n' + res_
    print(res)
    return res

def get_intent():
    res = []
    with open(r"D:\pycharm\ChatBot\data\nlu.yml", encoding='utf-8') as f:
        data = f.readlines()
    for ele in data:
        if '- intent' in ele:
            tempt = ele.split(' ')[-1].strip()
            res.append(tempt)
    return res

def get_utter():
    res = []
    with open(r"D:\pycharm\ChatBot\domain.yml", encoding='utf-8') as f:
        data = f.readlines()
    for ele in data:
        if 'utter' in ele:
            temp = ele.strip().replace(':', '')
            res.append(temp)
    return res


if __name__ == "__main__":
    gen_ask_no_product()
