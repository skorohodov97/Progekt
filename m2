from selenium import webdriver
import  time
import xlrd, xlwt
from xlutils.copy import copy as xlcopy
def mp():
    rb = xlrd.open_workbook('seb.xls')
    sheet = rb.sheet_by_index(0)
    sheet1 = rb.sheet_by_index(2)
    write_book = xlcopy(rb)
    write_sheet = write_book.get_sheet(0)
    write_sheet1 = write_book.get_sheet(2)
    restart = 0
    a = 43
    b = 0
    while restart < 1 and b < 5:
        try:
            driver = webdriver.Chrome('C:/Users/skoro/Downloads/chromedriver_win32 (1)/chromedriver.exe')
            driver.maximize_window()
            driver.get("https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome")
            s_username = driver.find_element_by_id("username")
            s_username.clear()
            s_username.send_keys("sda052")
            s_password = driver.find_element_by_id('password')
            s_password.clear()
            s_password.send_keys("vfvf2014")
            s_continue = driver.find_element_by_css_selector('#login-form > div.form-actions > button')
            s_continue.click()
            time.sleep(1)
            s_c = driver.find_element_by_css_selector('#sidebar-wrapper > ul > li:nth-child(9) > a')
            s_c.click()
            time.sleep(1)
            xa = int(sheet1.row_values(0)[3])
            if xa == 0:
                xa = xa + 1
            aj = a
            for j in range(aj, 85):
                a = j
                try:
                    s_co = driver.find_element_by_css_selector(
                        '#page-content-wrapper > div > div > ul.nav.nav-tabs.btn-toolbar > li:nth-child(4) > a')
                    s_co.click()
                    time.sleep(1)
                except:
                    s_c = driver.find_element_by_css_selector('#sidebar-wrapper > ul > li:nth-child(9) > a')
                    s_c.click()
                    time.sleep(1)
                    s_co = driver.find_element_by_css_selector(
                        '#page-content-wrapper > div > div > ul.nav.nav-tabs.btn-toolbar > li:nth-child(4) > a')
                    s_co.click()
                    time.sleep(1)
                # page-content-wrapper > div > div > ul.nav.nav-tabs.btn-toolbar > li:nth-child(3) > a
                s_cor = driver.find_element_by_css_selector(
                    '#page-content-wrapper > div > div > div.row > div:nth-child(1) > div > a:nth-child(' + str(
                        j) + ')')
                s_cor.click()
                time.sleep(10)
                s_cort = driver.find_element_by_css_selector(
                    '#page-content-wrapper > div > div:nth-child(5) > a:nth-child(2)')
                s_cort.click()
                time.sleep(10)
                wa = driver.find_element_by_css_selector('#page-content-wrapper > div > h1')
                na = xa
                print(wa.text)
                la = driver.find_elements_by_class_name('list-group-item')
                ta = int(len(la))
                print(ta)
                for num in range(1, ta + 1):
                    try:
                        s = "#page-content-wrapper > div > div.list-group > div:nth-child(" + str(num) + ") > a"
                        row = driver.find_element_by_css_selector(s)
                        sa = row.text
                    except:
                        s = "#page-content-wrapper > div > div.list-group > div:nth-child(" + str(num) + ")"
                        row = driver.find_element_by_css_selector(s)
                        sa = row.text
                        temp = sa.find(' ')
                        index = temp
                        sa = sa[index:]
                        sa = sa[1:]
                    print(sa)
                    write_sheet.write(na, 2, wa.text)
                    na = na + 1

                for num in range(1, ta + 1):
                    try:
                        s_cort = driver.find_element_by_css_selector(
                            '#page-content-wrapper > div > div:nth-child(5) > a:nth-child(2)')
                        s_cort.click()
                        time.sleep(10)
                    except:
                        time.sleep(1)
                    try:
                        s = "#page-content-wrapper > div > div.list-group > div:nth-child(" + str(num) + ") > a"
                        row = driver.find_element_by_css_selector(s)
                        sa = row.text
                    except:
                        s = "#page-content-wrapper > div > div.list-group > div:nth-child(" + str(num) + ")"
                        row = driver.find_element_by_css_selector(s)
                        sa = row.text
                        temp = sa.find(' ')
                        index = temp
                        sa = sa[index:]
                        sa = sa[1:]
                    print(sa)
                    write_sheet.write(xa, 0, sa)
                    write_sheet.write(xa, 11, 'м')
                    t = "#page-content-wrapper > div > div.list-group > div:nth-child(" + str(num) + ") > a"
                    try:
                        s_corte = driver.find_element_by_css_selector(t)
                        s_corte.click()
                        time.sleep(3)
                        try:
                            roww = driver.find_element_by_css_selector(
                                "#page-content-wrapper > div > div > div.col-md-4 > div > div:nth-child(4) > ul > li > a")
                            r = roww.get_attribute("href")
                            new_str = r.replace("https://vk.com/", "")
                        except:
                            new_str = ''
                        write_sheet.write(xa, 10, new_str)
                        driver.back()
                    except:
                        time.sleep(1)
                    xa = xa + 1
                    time.sleep(10)

                driver.back()
                time.sleep(3)
                write_sheet1.write(0, 3, xa)
                write_book.save('seb.xls')
                driver.back()
                b = 0
                time.sleep(10)
            write_sheet1.write(0, 3, xa)
            write_book.save('seb.xls')
            driver.close()
            restart = 5
        except:
            b = b + 1
            print(b)
            driver.close()
    if b >= 5:
        print("Циклическая ошибка")
