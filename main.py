import web_op
import folder_op


def main():
    url_xuat_phat = 'https://vietnamnet.vn'
    so_luong_trang = 100
    waiting_line = web_op.tim_url_lien_quan(url_xuat_phat, url_xuat_phat)
    history = web_op.them_va_duyet_hang_cho(waiting_line, url_xuat_phat, so_luong_trang)

    folder_op.tao_thu_muc('bt_crawl_python_3')
    folder_op.luu_tat_ca_file(history, so_luong_trang)

if __name__ == '__main__':
    main()