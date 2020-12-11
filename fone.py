import wx
import xlrd, xlwt
from xlutils.copy import copy as xlcopy
from delete import delete
from b4 import bp
from c1 import cp
from m2 import mp
from vk import vk
from neuron import god


rb = xlrd.open_workbook('seb.xls')
sheet = rb.sheet_by_index(2)
write_book = xlcopy(rb)
write_sheet = write_book.get_sheet(2)


class LoginDialog(wx.Dialog):
   
    def __init__(self, parent):
        wx.Dialog.__init__(self, None, title="Авторизация")
        self.frame = parent
        self.logged_in = False
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
     

        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label="Логин:")
        user_sizer.Add(user_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.CENTER, 5)

       
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="Пароль:")
        p_sizer.Add(p_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)
        p_sizer.Add(self.password, 0, wx.CENTER, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.CENTER, 5)
        main_sizer.Add(p_sizer, 0, wx.CENTER, 5)

        btn = wx.Button(self, label="Вход")
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    def OnEraseBackground(self, evt):
      
        
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)

        dc.Clear()
        bmp = wx.Bitmap("obhaga.jpg")
        dc.DrawBitmap(bmp, 0, 0)

    def onLogin(self, event):
        
        stupid_password = "1"
        user_password = self.password.GetValue()
        if user_password == stupid_password:
            print("You are now logged in!")
            self.logged_in = True
            self.Close()
        else:
            print("Username or password is incorrect!")


class Many(wx.Dialog):
    def __init__(self, parent):
        
        wx.Dialog.__init__(self, parent=parent,size=(650, 600))

        self.frame = parent
        self.l1 = False
        self.l3 =False
        user_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        user_lbl1 = wx.StaticText(self, label="Меню:")
        user_sizer1.Add(user_lbl1, 0, wx.CENTER)
        btn = wx.Button(self, label="Ввод количества мест")
        btn.Bind(wx.EVT_BUTTON, self.onLogi1)
        btn1 = wx.Button(self, label="Загрузка данных бакалавриата")
        btn1.Bind(wx.EVT_BUTTON, self.onLogi2)
        btn2 = wx.Button(self, label="Загрузка данных специалитета")
        btn2.Bind(wx.EVT_BUTTON, self.onLogi3)
        btn3 = wx.Button(self, label="Загрузка данных магистратура")
        btn3.Bind(wx.EVT_BUTTON, self.onLogi4)
        btn4 = wx.Button(self, label="Загрузка дополнительных данных")
        btn4.Bind(wx.EVT_BUTTON, self.onLogi5)
        btn5 = wx.Button(self, label="Очистка данных")
        btn5.Bind(wx.EVT_BUTTON, self.onLogi6)
        btn6 = wx.Button(self, label="Обработка данных")
        btn6.Bind(wx.EVT_BUTTON, self.onLogi7)
        btn7 = wx.Button(self, label="Выход")
        btn7.Bind(wx.EVT_BUTTON, self.onLogi8)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add((0, 0), 1, wx.EXPAND)
        main_sizer.Add(user_sizer1, 0, wx.CENTER)
        main_sizer.Add(btn, 0, wx.CENTER)
        main_sizer.Add(btn1, 0, wx.CENTER)
        main_sizer.Add(btn2, 0, wx.CENTER)
        main_sizer.Add(btn3, 0, wx.CENTER)
        main_sizer.Add(btn4, 0, wx.CENTER)
        main_sizer.Add(btn6, 0, wx.CENTER)
        main_sizer.Add(btn5, 0, wx.CENTER)
        main_sizer.Add(btn7, 0, wx.CENTER)
        main_sizer.Add((0, 0), 1, wx.EXPAND)
        self.SetSizer(main_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.EnEraseBackground)

    def onLogi1(self, event):
     
        self.l1 = True

        print("done2")
        self.Close()

    def onLogi2(self, event):
       
        bp()
        print("done")
        self.Close()

    def onLogi3(self, event):
       
        cp()
        print("done")
        self.Close()

    def onLogi4(self, event):
       
        mp()
        print("done")
        self.Close()

    def onLogi5(self, event):
       
        vk()
        print("done")
        self.Close()

    def onLogi6(self, event):
       
        delete()
        print("done")
        self.Close()

    def onLogi7(self, event):
        
        god()
        print("done")
        self.Close()

    def onLogi8(self, event):
       
        self.l3=True
        print("done5")
        self.Close()

    def EnEraseBackground(self, evt):
      
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)

        dc.Clear()
        bmp = wx.Bitmap("mifi.jpg")
        dc.DrawBitmap(bmp, 0, 0)


class MyPanel(wx.Dialog):

    def __init__(self, parent):
        
        wx.Dialog.__init__(self,None,size=(650, 600) )
        self.frame = parent
        self.l2 = False
        user_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        user_lbl1 = wx.StaticText(self, label="Введите количество мест:")
        user_sizer1.Add(user_lbl1, 0, wx.CENTER)

        user_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        user_lbl2 = wx.StaticText(self, label="Мальчики:        ")
        user_lbl3 = wx.StaticText(self, label="        Девочки:")
        user_sizer2.Add(user_lbl2, 0, wx.CENTER, 5)
        user_sizer2.Add(user_lbl3, 0, wx.CENTER, 5)

        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label="1 общага:")
        user_sizer.Add(user_lbl, 0, wx.CENTER)
        self.user = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.user.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.user1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.user1.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        user_sizer.Add(self.user, 0, wx.CENTER)
        user_sizer.Add(self.user1, 0, wx.CENTER)

        
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="2 общага:")
        p_sizer.Add(p_lbl, 0, wx.CENTER)
        self.password = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.passwor = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.passwor.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        p_sizer.Add(self.password, 0, wx.CENTER)
        p_sizer.Add(self.passwor, 0, wx.CENTER)

        p_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        p_lbl1 = wx.StaticText(self, label="3 общага:")
        p_sizer1.Add(p_lbl1, 0, wx.CENTER)
        self.password1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.password1.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.passwor1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.passwor1.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        p_sizer1.Add(self.password1, 0, wx.CENTER)
        p_sizer1.Add(self.passwor1, 0, wx.CENTER)

        p_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        p_lbl2 = wx.StaticText(self, label="4 общага:")
        p_sizer2.Add(p_lbl2, 0, wx.CENTER)
        self.password2 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.password2.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.passwor2 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.passwor2.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        p_sizer2.Add(self.password2, 0, wx.CENTER)
        p_sizer2.Add(self.passwor2, 0, wx.CENTER)

        p_sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        p_lbl3 = wx.StaticText(self, label="5 общага:")
        p_sizer3.Add(p_lbl3, 0, wx.CENTER)
        self.password3 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.password3.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.passwor3 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.passwor3.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        p_sizer3.Add(self.password3, 0, wx.CENTER)
        p_sizer3.Add(self.passwor3, 0, wx.CENTER)

        btn = wx.Button(self, label="Ввод")
        btn.Bind(wx.EVT_BUTTON, self.onLogi1)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add((0, 0), 1, wx.EXPAND)
        main_sizer.Add(user_sizer1, 0, wx.CENTER)
        main_sizer.Add(user_sizer2, 0, wx.CENTER)
        main_sizer.Add(user_sizer, 0, wx.CENTER)
        main_sizer.Add(p_sizer, 0, wx.CENTER)
        main_sizer.Add(p_sizer1, 0, wx.CENTER)
        main_sizer.Add(p_sizer2, 0, wx.CENTER)
        main_sizer.Add(p_sizer3, 0, wx.CENTER)
        main_sizer.Add(btn, 0, wx.CENTER)
        main_sizer.Add((0, 0), 1, wx.EXPAND)

        self.SetSizer(main_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.EnEraseBackground)

    def onLogi1(self, event):
        
        self.l2 = True
        user = self.user.GetValue()
        user1 = self.user1.GetValue()
        password = self.password.GetValue()
        passwor = self.passwor.GetValue()
        password1 = self.password1.GetValue()
        passwor1 = self.passwor1.GetValue()
        password2 = self.password2.GetValue()
        passwor2 = self.passwor2.GetValue()
        password3 = self.password3.GetValue()
        passwor3 = self.passwor3.GetValue()

        print(user)
        write_sheet.write(3, 1, int(user))
        write_sheet.write(5, 1, int(password))
        write_sheet.write(7, 1, int(password1))
        write_sheet.write(9, 1, int(password2))
        write_sheet.write(11, 1, int(password3))
        write_sheet.write(3, 2, int(user1))
        write_sheet.write(5, 2, int(passwor))
        write_sheet.write(7, 2, int(passwor1))
        write_sheet.write(9, 2, int(passwor2))
        write_sheet.write(11, 2, int(passwor3))
        write_book.save('seb.xls')

        self.Close()

    def EnEraseBackground(self, evt):
        
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)

        dc.Clear()
        bmp = wx.Bitmap("mifi.jpg")
        dc.DrawBitmap(bmp, 0, 0)


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, size=(650, 600), title="Успешный вход")

        self.Center()
        dlg = LoginDialog(None)
        dlg.ShowModal()
        authenticated = dlg.logged_in
        dlg.Destroy()
        dlm = Many(None)
        authenticated3 = dlm.l3
        if not authenticated:
            self.Close()
        while not authenticated3:
            dlm = Many(None)
            dlm.ShowModal()
            authenticated1 = dlm.l1
            authenticated3 = dlm.l3
            if authenticated3:
                break

            if authenticated1:
                dlm.Hide()
                dlt = MyPanel(None)
                dlt.ShowModal()
                authenticated2 = dlt.l2
                if authenticated2:
                 dlt.Hide()

        exit(0)
        self.Center()


class Main(wx.App):

    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()


if __name__ == "__main__":
    app = Main()
    app.MainLoop()

