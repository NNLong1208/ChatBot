def gen_ask_no_product():
    dtnx = ['Shop', 'Bạn', 'Cửa hàng', '']
    sanpham = ['Tivi', 'Tủ lạnh', 'máy giặt', 'Điều hòa', 'bóng đèn', 'xà bông', 'bếp', 'xe máy', 'xe đạp', 'lò vi sóng',
               'Bếp ga', 'Bếp điện', 'xe đạp', 'điện thoại', 'xoong', 'nồi', 'chảo', 'bảng đen', 'máy lọc nước']
    string = '- {} có kinh doanh {} không\n'
    res = ''
    for x in dtnx:
        for y in sanpham:
            a = string.format(x, y)
            res +=a
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
if __name__ == "__main__":
    result = gen_ask_payment()
    print(result)