import numpy as np
import xlrd, xlwt
from xlutils.copy import copy as xlcopy
rb = xlrd.open_workbook('seb.xls')
sheet = rb.sheet_by_index(0)
write_book = xlcopy(rb)
write_sheet = write_book.get_sheet(1)
def sigmoid(x):
    # Функция активации sigmoid:: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    # Производная от sigmoid: f'(x) = f(x) * (1 - f(x))
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(y_true, y_pred):
    # y_true и y_pred являются массивами numpy с одинаковой длиной
    return ((y_true - y_pred) ** 2).mean()


class OurNeuralNetwork:
    """
    Нейронная сеть, у которой:
        - 2 входа
        - скрытый слой с двумя нейронами (h1, h2)
        - слой вывода с одним нейроном (o1)

    *** ВАЖНО ***:
    Код ниже написан как простой, образовательный. НЕ оптимальный.
    Настоящий код нейронной сети выглядит не так. НЕ ИСПОЛЬЗУЙТЕ этот код.
    Вместо этого, прочитайте/запустите его, чтобы понять, как работает эта сеть.
    """

    def __init__(self):
        # Вес
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
        self.w7 = np.random.normal()

        self.w9 = np.random.normal()
        self.w10 = np.random.normal()

        # Смещения
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def feedforward(self, x):
        # x является массивом numpy с двумя элементами
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.w6 * x[2] + self.w9 * x[3]+ self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.w7 * x[2]+ self.w10 * x[3] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, all_y_trues):
        """
        - data is a (n x 2) numpy array, n = # of samples in the dataset.
        - all_y_trues is a numpy array with n elements.
            Elements in all_y_trues correspond to those in data.
        """
        learn_rate = 0.1
        epochs = 1000  # количество циклов во всём наборе данных

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # --- Выполняем обратную связь (нам понадобятся эти значения в дальнейшем)
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.w6 * x[2] +self.w9 * x[3]+ self.b1
                h1 = sigmoid(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.w7 * x[2] +self.w10 * x[3]+ self.b2
                h2 = sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1

                # --- Подсчет частных производных
                # --- Наименование: d_L_d_w1 представляет "частично L / частично w1"
                d_L_d_ypred = -2 * (y_true - y_pred)

                # Нейрон o1
                d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = deriv_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)

                # Нейрон h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                d_h1_d_w6 = x[2] * deriv_sigmoid(sum_h1)
                d_h1_d_w9 = x[3] * deriv_sigmoid(sum_h1)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)

                # Нейрон h2
                d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
                d_h2_d_w7 = x[2] * deriv_sigmoid(sum_h2)
                d_h2_d_w10 = x[3] * deriv_sigmoid(sum_h2)
                d_h2_d_b2 = deriv_sigmoid(sum_h2)

                # --- Обновляем вес и смещения
                # Нейрон h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w6
                self.w9 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w9
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                # Нейрон h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.w7 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w7
                self.w10 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h2_d_w10
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                # Нейрон o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

            # --- Подсчитываем общую потерю в конце каждой фазы
            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse_loss(all_y_trues, y_preds)
                #print("Epoch %d loss: %.3f" % (epoch, loss))


# Определение набора данных
data = np.array([
    [3.6, 4, 0, 5],
    [3.6, 4, 1, -7],
    [-0.05, -8, 0,-3],
    [-0.05, -8, 1, 0],
    [1.5, 3, 0, 7],
    [1.5, 3, 1, 6],
    [-9, -9, 0, 2],
    [-9, -9, 1, -1],
])

all_y_trues = np.array([
    0.8,
    0,
    0.6,
    0,
    1,
    0,
    0.6,
    0,
])

# Тренируем нашу нейронную сеть!
network = OurNeuralNetwork()
network.train(data, all_y_trues)
# Делаем предсказания
m1=0
d1=0
m2=0
d2=0
m3=0
d3=0
m4=0
d4=0
m5=0
d5=0

for number in range(48):
    if number!=0:
        f1=sheet.row_values(number)[0]
        f2=int(sheet.row_values(number)[6])
        f3=int(sheet.row_values(number)[7])
        f4=int(sheet.row_values(number)[3])
        f5=int(sheet.row_values(number)[9])
        o1 = np.array([f2, f3, f4, f5])
        o2=int(sheet.row_values(number)[8])
        write_sheet.write(number, 0, f1)
        print(f1, end="")
        print(": %.3f " % network.feedforward(o1), end="")
        o1=network.feedforward(o1)
        t=0
        while t==0:
            if o1>0.8:
                if o2==0:
                    if d1<int(sheet.row_values(3)[13]):
                        d1=d1+1
                        t=t+1
                        write_sheet.write(number, 1, "1 общага")
                        print("1 общага Д")
                    else:
                        o1=0.7
                else:
                    if m1 < int(sheet.row_values(3)[12]):
                        m1 = m1 + 1
                        t = t + 1
                        write_sheet.write(number, 1, "1 общага")
                        print("1 общага М")
                    else:
                        o1 = 0.7
            if o1>0.6 and o1<0.8:
                if o2==0:
                    if d2<int(sheet.row_values(5)[13]):
                        d2=d2+1
                        t = t + 1
                        write_sheet.write(number, 1, "2 общага")
                        print("2 общага Д")
                    else:
                        o1=0.5
                else:
                    if m2 < int(sheet.row_values(5)[12]):
                        m2 = m2 + 1
                        t = t + 1
                        write_sheet.write(number, 1, "2 общага")
                        print("2 общага М")
                    else:
                        o1 = 0.5
            if o1 > 0.4 and o1<0.6:
                if o2 == 0:
                    if d3 < int(sheet.row_values(7)[13]):
                        d3 = d3 + 1
                        t = t + 1
                        write_sheet.write(number, 1, "3 общага")
                        print("3 общага Д")
                    else:
                        o1 = 0.3
                else:
                    if m3 < int(sheet.row_values(7)[12]):
                        m3 = m3 + 1
                        t = t + 1
                        write_sheet.write(number, 1, "3 общага")
                        print("3 общага М")
                    else:
                        o1 = 0.3
            if o1 > 0.2 and o1<0.4:
                if o2 == 0:
                    if d4 < int(sheet.row_values(9)[13]):
                        d4 = d4 + 1
                        t = t + 1
                        write_sheet.write(number, 1, "4 общага")
                        print("4 общага Д")
                    else:
                        o1 = 0.1
                else:
                    if m4 < int(sheet.row_values(9)[12]):
                        m4 = m4 + 1
                        t = t + 1
                        write_sheet.write(number, 1, "4 общага")
                        print("4 общага М")
                    else:
                        o1 = 0.1
            if o1 >= 0 and o1<0.2:
                if o2 == 0:
                    if d5 < int(sheet.row_values(11)[13]):
                        d5 = d5 + 1
                        t = t + 1
                        write_sheet.write(number, 1, "5 общага")
                        print("5 общага Д")
                    else:
                        o1 = 0.9
                else:
                    if m5 < int(sheet.row_values(11)[12]):
                        m5 = m5 + 1
                        t = t + 1
                        write_sheet.write(number, 1, "5 общага")
                        print("5 общага М")
                    else:
                        o1 = 0.9
write_book.save('seb.xls')



