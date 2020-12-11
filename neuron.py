import numpy as np
import xlrd, xlwt
from array import *


from xlutils.copy import copy as xlcopy
import numpy as p
def god():
    rb = xlrd.open_workbook('seb.xls')
    sheet = rb.sheet_by_index(0)
    sheet1 = rb.sheet_by_index(2)
    write_book = xlcopy(rb)
    write_sheet = write_book.get_sheet(1)
    d = int(sheet1.row_values(0)[3])

    def sigmoid(x):

        return 1 / (1 + np.exp(-x))

    def deriv_sigmoid(x):

        fx = sigmoid(x)
        return fx * (1 - fx)

    def mse_loss(y_true, y_pred):
        
        return ((y_true - y_pred) ** 2).mean()

    class OurNeuralNetwork:


        def __init__(self):

            self.w1 = np.random.normal()
            self.w2 = np.random.normal()
            self.w3 = np.random.normal()
            self.w4 = np.random.normal()
            self.w5 = np.random.normal()
            self.w6 = np.random.normal()
            self.w7 = np.random.normal()
            self.w8 = np.random.normal()
            self.w9 = np.random.normal()
            self.w10 = np.random.normal()
            self.w11 = np.random.normal()


            self.b1 = np.random.normal()
            self.b2 = np.random.normal()
            self.b3 = np.random.normal()

        def feedforward(self, x):

            h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.w6 * x[2] + self.w9 * x[3] + self.w8 * x[4] + self.b1)
            h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.w7 * x[2] + self.w10 * x[3] + self.w11 * x[4] + self.b2)
            o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
            return o1

        def train(self, data, all_y_trues):
            learn_rate = 0.1
            epochs = 1000

            for epoch in range(epochs):
                for x, y_true in zip(data, all_y_trues):

                    sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.w6 * x[2] + self.w9 * x[3] + self.w8 * x[
                        4] + self.b1
                    h1 = sigmoid(sum_h1)

                    sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.w7 * x[2] + self.w10 * x[3] + self.w11 * x[
                        4] + self.b2
                    h2 = sigmoid(sum_h2)

                    sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                    o1 = sigmoid(sum_o1)
                    y_pred = o1

                    d_L_d_ypred = -2 * (y_true - y_pred)
                    d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
                    d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)
                    d_ypred_d_b3 = deriv_sigmoid(sum_o1)

                    d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)
                    d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)


                    d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                    d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                    d_h1_d_w6 = x[2] * deriv_sigmoid(sum_h1)
                    d_h1_d_w9 = x[3] * deriv_sigmoid(sum_h1)
                    d_h1_d_w8 = x[4] * deriv_sigmoid(sum_h1)
                    d_h1_d_b1 = deriv_sigmoid(sum_h1)


                    d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
                    d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
                    d_h2_d_w7 = x[2] * deriv_sigmoid(sum_h2)
                    d_h2_d_w10 = x[3] * deriv_sigmoid(sum_h2)
                    d_h2_d_w11 = x[4] * deriv_sigmoid(sum_h2)
                    d_h2_d_b2 = deriv_sigmoid(sum_h2)

                    self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                    self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                    self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w6
                    self.w9 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w9
                    self.w8 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w8
                    self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                    self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                    self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                    self.w7 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w7
                    self.w10 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w10
                    self.w11 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w11
                    self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                    self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                    self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                    self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

                if epoch % 10 == 0:
                    y_preds = np.apply_along_axis(self.feedforward, 1, data)
                    #loss = mse_loss(all_y_trues, y_preds)
                    # print("Epoch %d loss: %.3f" % (epoch, loss))


    data = np.array([
        [1, 1, 10, 12, 30],
        [1, 1, 10, 12, -1],
        [1, 1, 10, -11, 30],
        [1, 1, 10, -11, -1],
        [1, 1, -0.35, 12, 30],
        [1, 1, -0.35, 12, -1],
        [1, 1, -0.35, -11, 30],
        [1, 1, -0.35, -11, -1],
        [0, 0, 10, 12, 30],
        [0, 0, 10, 12, -1],
        [0, 0, 10, -11, 30],
        [0, 0, 10, -11, -1],
        [0, 0, -0.35, 12, 30],
        [0, 0, -0.35, 12, -1],
        [0, 0, -0.35, -11, 30],
        [0, 0, -0.35, -11, -1],
        [0, 1, 10, 12, 30],
        [0, 1, 10, 12, -1],
        [0, 1, 10, -11, 30],
        [0, 1, 10, -11, -1],
        [0, 1, -0.35, 12, 30],
        [0, 1, -0.35, 12, -1],
        [0, 1, -0.35, -11, 30],
        [0, 1, -0.35, -11, -1],
        [0, 0, 10, 12, 30],
        [0, 0, 10, 12, -1],
        [0, 0, 10, -11, 30],
        [0, 0, 10, -11, -1],
        [0, 0, -0.35, 12, 30],
        [0, 0, -0.35, 12, -1],
        [0, 0, -0.35, -11, 30],
        [0, 0, -0.35, -11, -1],

    ])

    all_y_trues = np.array([
        1,
        0.96875,
        0.9375,
        0.90625,
        0.875,
        0.84375,
        0.8125,
        0.78125,
        0.75,
        0.71875,
        0.6875,
        0.65625,
        0.625,
        0.59375,
        0.5625,
        0.53125,
        0.5,
        0.46875,
        0.4375,
        0.40625,
        0.375,
        0.34375,
        0.3125,
        0.28125,
        0.25,
        0.21875,
        0.1875,
        0.15625,
        0.125,
        0.09375,
        0.0625,
        0.03125,
        0,

    ])


    network = OurNeuralNetwork()
    network.train(data, all_y_trues)

    m1 = np.zeros((15, 18))
    d1 = np.zeros((4, 18))
    m2 = np.zeros((18, 11))
    d2 = np.zeros((5, 11))
    m3 = np.zeros((4, 31))
    d3 = np.zeros((1, 31))
    m4 = np.zeros((4, 31))
    d4 = np.zeros((1, 31))
    m5 = np.zeros((4, 31))
    d5 = np.zeros((1, 31))
    print(m1[0][1])
    M1 = int(sheet1.row_values(3)[1])
    D1 = int(sheet1.row_values(3)[2])
    M2 = int(sheet1.row_values(5)[1])
    D2 = int(sheet1.row_values(5)[2])
    M3 = int(sheet1.row_values(7)[1])
    D3 = int(sheet1.row_values(7)[2])
    M4 = int(sheet1.row_values(9)[1])
    D4 = int(sheet1.row_values(9)[2])
    M5 = int(sheet1.row_values(11)[1])
    D5 = int(sheet1.row_values(11)[2])
    M=array('i', [0, 0, 0, 0, 0])
    D = array('i', [0, 0, 0, 0, 0])
    if M1>810:
        print("Ошибка неверна введены дланные в для М1")
        exit(0)
    if D1>216:
        print("Ошибка неверна введены дланные в для D1")
        exit(0)
    if M2>594:
        print("Ошибка неверна введены дланные в для М2")
        exit(0)
    if D2>165:
        print("Ошибка неверна введены дланные в для D2")
        exit(0)
    if M3>372:
        print("Ошибка неверна введены дланные в для М3")
        exit(0)
    if D3>93:
        print("Ошибка неверна введены дланные в для D3")
        exit(0)
    if M4>372:
        print("Ошибка неверна введены дланные в для М4")
        exit(0)
    if D4>93:
        print("Ошибка неверна введены дланные в для D4")
        exit(0)
    if M5>372:
        print("Ошибка неверна введены дланные в для М5")
        exit(0)
    if D5>93:
        print("Ошибка неверна введены дланные в для D5")
        exit(0)
    m=3
    for number in range(d):
        if number != 0:
            f1 = str(sheet.row_values(number)[0])
            f2 = int(sheet.row_values(number)[6])
            f3 = int(sheet.row_values(number)[7])
            f4 = int(sheet.row_values(number)[3])
            f5 = int(sheet.row_values(number)[9])
            f6 = str(sheet.row_values(number)[11])
            if (f6 == 'м'):
                f6 = 1
            else:
                f6 = 0
            o1 = np.array([f4, f6, f2, f3, f5])
            o2 = int(sheet.row_values(number)[8])
            write_sheet.write(number, 0, f1)
            print(f1, end="")
            print(": %.3f " % network.feedforward(o1), end="")
            o1 = network.feedforward(o1)
            t = 0
            while t == 0:
                if t > 0:
                    break
                if o1 >= 0.8:
                    if (o2==0&D[0]<D1)|(o2!=0&M[0]<M1):
                        if t > 0:
                            break
                        if o1 >= 0.95:
                            for y in range(18):
                                if o2 == 0:
                                    if d1[3][y] < m:
                                        d1[3][y] = d1[3][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "1 общага")
                                        write_sheet.write(number, 2, " 19 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("1 общага Д, 19 этаж ", y, "комната")
                                        y = y - 1
                                        D[0]=D[0]+1
                                        break
                                        break
                                    else:
                                        o1 = 0.9

                                else:
                                    for x in range(11, 15):

                                        if t > 0:
                                            break
                                        if m1[x][y] <= m:
                                            m1[x][y] = m1[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "1 общага")
                                            x = x + 1
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 1
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("1 общага М,", x, "этаж", y, "комната")
                                            y = y - 1
                                            M[0]=M[0]+1
                                            break
                                            break
                                        else:
                                            o1 = 0.9

                        if t > 0:
                            break
                        if o1 >= 0.9 and o1 < 0.95:
                            for y in range(18):
                                if o2 == 0:
                                    if d1[2][y] < m:
                                        d1[2][y] = d1[2][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "1 общага")
                                        write_sheet.write(number, 2, "18 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("1 общага Д, 18 этаж ", y, "комната")
                                        y = y - 1
                                        D[0]=D[0]+1
                                        break
                                        break
                                    else:
                                        o1 = 0.85
                                else:
                                    for x in range(7, 11):
                                        if t > 0:
                                            break
                                        if m1[x][y] < m:
                                            m1[x][y] = m1[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "1 общага")
                                            x = x + 1
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 1
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("1 общага М,", x, " этаж", y, "комната")
                                            y = y - 1
                                            M[0] = M[0] + 1
                                            break
                                            break
                                        else:
                                            o1 = 0.85

                        if t > 0:
                            break
                        if o1 >= 0.85 and o1 < 0.9:
                            for y in range(18):
                                if o2 == 0:
                                    if d1[1][y] < m:
                                        d1[1][y] = d1[1][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "1 общага")
                                        write_sheet.write(number, 2, "17 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("1 общага Д, 17 этаж ", y, "комната")
                                        y = y - 1
                                        D[0]=D[0]+1
                                        break
                                        break
                                    else:
                                        o1 = 0.8
                                else:
                                    for x in range(3, 7):
                                        if t > 0:
                                            break
                                        if m1[x][y] < m:
                                            m1[x][y] = m1[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "1 общага")
                                            x = x + 1
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 1
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("1 общага М,", x, " этаж", y, "комната")
                                            y = y - 1
                                            M[0] = M[0] + 1
                                            break
                                            break
                                        else:
                                            o1 = 0.8

                        if t > 0:
                            break
                        if o1 >= 0.8 and o1 < 0.85:
                            for y in range(4):
                                if o2 == 0:
                                    if d1[0][y] < m:
                                        d1[0][y] = d1[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "1 общага")
                                        write_sheet.write(number, 2, "16 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("1 общага Д, 16 этаж ", y, "комната")
                                        y = y - 1
                                        D[0]=D[0]+1
                                        break
                                        break
                                    else:
                                        o1 = 0.75
                                else:
                                    for x in range(0, 3):
                                        if t > 0:
                                            break
                                        if m1[x][y] < m:
                                            m1[x][y] = m1[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "1 общага")
                                            x = x + 1
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 1
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("1 общага М,", x, "этаж", y, "комната")
                                            y = y - 1
                                            M[0] = M[0] + 1
                                            break
                                            break
                                        else:
                                            o1 = 0.75

                if t > 0:
                    break
                if o1 >= 0.6 and o1 < 0.8:
                    if t > 0:
                        break
                    if (o2 == 0 & D[1] < D2) | (o2 != 0 & M[1] < M2):
                        if o1 >= 0.75:
                            for y in range(11):
                                for x in range(3, 5):
                                    if t > 0:
                                        break
                                    if o2 == 0:
                                        if d2[x][y] < m:
                                            d2[x][y] = d2[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "2 общага")
                                            x = x + 19
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 19
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("2 общага Д,", x, " этаж ", y, "комната")
                                            y = y - 1
                                            D[1] = D[1] + 1
                                            break
                                            break
                                        else:
                                            o1 = 0.7

                                else:
                                    for x in range(13, 18):

                                        if t > 0:
                                            break
                                        if m2[x][y] < m:
                                            m2[x][y] = m2[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "2 общага")
                                            x = x + 1
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 1
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("2 общага М,", x, " этаж", y, "комната")
                                            y = y - 1
                                            M[1] = M[1] + 1
                                            break
                                            break
                                        else:
                                            o1 = 0.7

                        if t > 0:
                            break
                        if o1 >= 0.7 and o1 < 0.75:
                            for y in range(4):
                                if o2 == 0:
                                    if d2[2][y] < m:
                                        d2[2][y] = d2[2][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "2 общага")
                                        write_sheet.write(number, 2, "21 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("2 общага Д, 21 этаж ", y, "комната")
                                        y = y - 1
                                        D[1] = D[1] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.65
                                else:
                                    for x in range(8, 13):
                                        if t > 0:
                                            break
                                        if m2[x][y] < m:
                                            m2[x][y] = m2[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "2 общага")
                                            x = x + 1
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 1
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("2 общага М,", x, " этаж", y, "комната")
                                            y = y - 1
                                            M[1] = M[1] + 1
                                            break
                                            break
                                        else:
                                            o1 = 0.65

                        if t > 0:
                            break
                        if o1 >= 0.65 and o1 < 0.7:
                            for y in range(4):
                                if o2 == 0:
                                    if d2[1][y] < m:
                                        d2[1][y] = d2[1][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "2 общага")
                                        write_sheet.write(number, 2, "20 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("2 общага Д, 20 этаж ", y, "комната")
                                        y = y - 1
                                        D[1] = D[1] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.6
                                else:
                                    for x in range(4, 8):
                                        if t > 0:
                                            break
                                        if m2[x][y] < m:
                                            m2[x][y] = m2[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "2 общага")
                                            x = x + 1
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 1
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("2 общага М,", x, " этаж", y, "комната")
                                            y = y - 1
                                            M[1] = M[1] + 1
                                            break
                                            break
                                        else:
                                            o1 = 0.6

                        if t > 0:
                            break
                        if o1 >= 0.6 and o1 < 0.65:
                            for y in range(4):
                                if o2 == 0:
                                    if d2[0][y] < m:
                                        d2[0][y] = d2[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "2 общага")
                                        write_sheet.write(number, 2, "19 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("2 общага Д, 19 этаж ", y, "комната")
                                        y = y - 1
                                        D[1] = D[1] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.55
                                else:
                                    for x in range(0, 4):
                                        if t > 0:
                                            break
                                        if m2[x][y] < m:
                                            m2[x][y] = m2[x][y] + 1
                                            t = t + 1
                                            write_sheet.write(number, 1, "2 общага")
                                            x = x + 1
                                            write_sheet.write(number, 2, str(x) + " этаж")
                                            x = x - 1
                                            y = y + 1
                                            write_sheet.write(number, 3, y)
                                            print("2 общага М,", x, " этаж", y, "комната")
                                            y = y - 1
                                            M[1] = M[1] + 1
                                            break
                                            break
                                        else:
                                            o1 = 0.55


                if t > 0:
                    break
                if o1 >= 0.4 and o1 < 0.6:
                    if t > 0:
                        break
                    if (o2 == 0 & D[2] < D3) | (o2 !=0 & M[2] < M3):
                        if o1 >= 0.55:
                            for y in range(4):
                                if o2 == 0:
                                    if d3[0][y] < m:
                                        d3[0][y] = d3[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "3 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("3 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[2] = D[2] + 1

                                        break
                                        break
                                    else:
                                        o1 = 0.5
                                else:
                                    if m3[3][y] < m:
                                        m3[3][y] = m2[3][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "3 общага")
                                        write_sheet.write(number, 2, "4 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("3 общага М, 4 этаж", y, "комната")
                                        y = y - 1
                                        M[2] = M[2] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.5
                        if t > 0:
                            break
                        if o1 >= 0.5 and o1 < 0.55:
                            for y in range(4):
                                if o2 == 0:
                                    if d3[0][y] < m:
                                        d3[0][y] = d3[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "3 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("3 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[2] = D[2] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.45
                                else:
                                    if m3[2][y] < m:
                                        m3[2][y] = m3[2][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "3 общага")
                                        write_sheet.write(number, 2, "3 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("3 общага М, 3 этаж", y, "комната")
                                        y = y - 1
                                        M[2] = M[2] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.45
                        if t > 0:
                            break
                        if o1 >= 0.45 and o1 < 0.5:
                            for y in range(4):
                                if o2 == 0:
                                    if d3[0][y] < m:
                                        d3[0][y] = d3[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "3 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("3 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[2] = D[2] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.4
                                else:
                                    if m3[1][y] < m:
                                        m3[1][y] = m3[1][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "3 общага")
                                        write_sheet.write(number, 2, "2 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("3 общага М, 2 этаж", y, "комната")
                                        y = y - 1
                                        M[2] = M[2] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.4
                        if t > 0:
                            break
                        if o1 >= 0.4 and o1 < 0.45:
                            for y in range(4):
                                if o2 == 0:
                                    if d3[0][y] < m:
                                        d3[0][y] = d3[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "3 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("3 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[2] = D[2] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.35
                                else:
                                    if m3[0][y] < m:
                                        m3[0][y] = m3[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "3 общага")
                                        write_sheet.write(number, 2, "1 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("3 общага М, 1 этаж", y, "комната")
                                        y = y - 1
                                        M[2] = M[2] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.35
                if t > 0:
                    break
                if o1 >= 0.2 and o1 < 0.4:
                    if t > 0:
                        break
                    if (o2 == 0 & D[3] < D4) | (o2 != 0 & M[3] < M4):
                        if o1 >= 0.35:
                            for y in range(4):
                                if o2 == 0:
                                    if d4[0][y] < m:
                                        d4[0][y] = d4[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "4 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("4 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[3] = D[3] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.3
                                else:
                                    if m4[3][y] < m:
                                        m4[3][y] = m4[3][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "4 общага")
                                        write_sheet.write(number, 2, "4 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("4 общага М, 4 этаж", y, "комната")
                                        y = y - 1
                                        M[3] = M[3] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.3
                        if t > 0:
                            break
                        if o1 >= 0.3 and o1 < 0.35:
                            for y in range(4):
                                if o2 == 0:
                                    if d4[0][y] < m:
                                        d4[0][y] = d4[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "4 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("4 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[3] = D[3] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.25
                                else:
                                    if m4[2][y] < m:
                                        m4[2][y] = m4[2][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "4 общага")
                                        write_sheet.write(number, 2, "3 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("4 общага М, 3 этаж", y, "комната")
                                        y = y - 1
                                        M[3] = M[3] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.25
                        if t > 0:
                            break
                        if o1 >= 0.25 and o1 < 0.3:
                            for y in range(4):
                                if o2 == 0:
                                    if d4[0][y] < m:
                                        d4[0][y] = d4[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "4 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("4 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[3] = D[3] + 1

                                        break
                                        break
                                    else:
                                        o1 = 0.2
                                else:
                                    if m4[1][y] < m:
                                        m4[1][y] = m4[1][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "4 общага")
                                        write_sheet.write(number, 2, "2 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("4 общага М, 2 этаж", y, "комната")
                                        y = y - 1
                                        M[3] = M[3] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.2
                        if t > 0:
                            break
                        if o1 >= 0.2 and o1 < 0.25:
                            for y in range(4):
                                if o2 == 0:
                                    if d4[0][y] < m:
                                        d4[0][y] = d4[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "4 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("4 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[3] = D[3] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.15
                                else:
                                    if m4[0][y] < m:
                                        m4[0][y] = m4[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "4 общага")
                                        write_sheet.write(number, 2, "1 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("4 общага М, 1 этаж", y, "комната")
                                        y = y - 1
                                        M[3] = M[3] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.15

                if t > 0:
                    break
                if o1 >= 0 and o1 < 0.2:
                    if t > 0:
                        break
                    if (o2 == 0 & D[4] < D5) | (o2 != 0 & M[4] < M5):
                        if o1 >= 0.15:
                            for y in range(4):
                                if o2 == 0:
                                    if d5[0][y] < m:
                                        d5[0][y] = d5[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("5 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[4] = D[4] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.1
                                else:
                                    if m5[3][y] < m:
                                        m5[3][y] = m5[3][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "4 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("5 общага М, 4 этаж", y, "комната")
                                        y = y - 1
                                        M[4] = M[4] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.1
                        if t > 0:
                            break
                        if o1 >= 0.1 and o1 < 0.15:
                            for y in range(4):
                                if o2 == 0:
                                    if d5[0][y] < 3:
                                        d5[0][y] = d5[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("5 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[4] = D[4] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.05
                                else:
                                    if m5[2][y] < m:
                                        m5[2][y] = m5[2][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "3 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("5 общага М, 3 этаж", y, "комната")
                                        y = y - 1
                                        M[4] = M[4] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.05
                        if t > 0:
                            break
                        if o1 >= 0.05 and o1 < 0.1:
                            for y in range(4):
                                if o2 == 0:
                                    if d5[0][y] < m:
                                        d5[0][y] = d5[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("5 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[4] = D[4] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0
                                else:
                                    if m5[1][y] < m:
                                        m5[1][y] = m3[1][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "2 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("5 общага М, 2 этаж", y, "комната")
                                        y = y - 1
                                        M[4] = M[4] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0
                        if t > 0:
                            break
                        if o1 >= 0 and o1 < 0.05:
                            for y in range(4):
                                if o2 == 0:
                                    if d5[0][y] < m:
                                        d5[0][y] = d5[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "5 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("5 общага Д, 5 этаж ", y, "комната")
                                        y = y - 1
                                        D[4] = D[4] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.95
                                else:
                                    if m5[0][y] < m:
                                        m5[0][y] = m5[0][y] + 1
                                        t = t + 1
                                        write_sheet.write(number, 1, "5 общага")
                                        write_sheet.write(number, 2, "1 этаж")
                                        y = y + 1
                                        write_sheet.write(number, 3, y)
                                        print("5 общага М, 1 этаж", y, "комната")
                                        y = y - 1
                                        M[4] = M[4] + 1
                                        break
                                        break
                                    else:
                                        o1 = 0.95

    write_book.save('seb.xls')
