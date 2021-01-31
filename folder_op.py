#Các thư viện cần thiết
import os
import codecs
import requests

#Các hàm

#Hàm này tạo tên file tự động bắt đầu bằng cụm filename tiếp theo là số các file kết thúc là .html
def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)



def luu_tat_ca_file(history, so_luong_trang):
    for (stt, url_con) in enumerate(history):
        if stt >= so_luong_trang:
            break
        file = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
        file.write(requests.get(url_con).text)
        file.close()
        print(f'{stt} {url_con}')
