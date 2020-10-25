import wx
import xlrd, xlwt
from xlutils.copy import copy as xlcopy
rb = xlrd.open_workbook('seb.xls')
sheet = rb.sheet_by_index(0)
write_book = xlcopy(rb)
write_sheet = write_book.get_sheet(0)

class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """

    def __init__(self,parent):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Авторизация")
        self.frame = parent
        self.logged_in = False
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # user info

        user_sizer = wx.BoxSizer(wx.HORIZONTAL)


        user_lbl = wx.StaticText(self, label="Логин:")
        user_sizer.Add(user_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.CENTER, 5)

        # pass info
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
        """
        Добавляем фоновое изображение.
        """
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)

        dc.Clear()
        bmp = wx.Bitmap("obhaga.jpg")
        dc.DrawBitmap(bmp, 0, 0)

    def onLogin(self, event):
        """
        Check credentials and login
        """
        stupid_password = "1"
        user_password = self.password.GetValue()
        if user_password == stupid_password:
            print("You are now logged in!")
            self.logged_in = True
            self.Close()
        else:
            print("Username or password is incorrect!")


class MyPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent


        user_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        user_lbl1 = wx.StaticText(self, label="Введите количество мест:")
        user_sizer1.Add(user_lbl1, 0, wx.CENTER)

        user_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        user_lbl2 = wx.StaticText(self, label="Мальчики:        ")
        user_lbl3 = wx.StaticText(self, label="        Девочки:")
        user_sizer2.Add(user_lbl2, 0, wx.CENTER,5)
        user_sizer2.Add(user_lbl3, 0, wx.CENTER,5)

        user_sizer = wx.BoxSizer(wx.HORIZONTAL)


        user_lbl = wx.StaticText(self, label="1 общага:")
        user_sizer.Add(user_lbl,  0, wx.CENTER)
        self.user = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
        self.user.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.user1 = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
        self.user1.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        user_sizer.Add(self.user,  0, wx.CENTER)
        user_sizer.Add(self.user1, 0, wx.CENTER)

        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="2 общага:")
        p_sizer.Add(p_lbl,  0, wx.CENTER)
        self.password = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.passwor = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
        self.passwor.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        p_sizer.Add(self.password, 0, wx.CENTER)
        p_sizer.Add(self.passwor, 0, wx.CENTER)

        p_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        p_lbl1 = wx.StaticText(self, label="3 общага:")
        p_sizer1.Add(p_lbl1, 0, wx.CENTER)
        self.password1 = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
        self.password1.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.passwor1 = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
        self.passwor1.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        p_sizer1.Add(self.password1,  0, wx.CENTER)
        p_sizer1.Add(self.passwor1, 0, wx.CENTER)

        p_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        p_lbl2 = wx.StaticText(self, label="4 общага:")
        p_sizer2.Add(p_lbl2, 0, wx.CENTER)
        self.password2 = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
        self.password2.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.passwor2 = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
        self.passwor2.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        p_sizer2.Add(self.password2, 0, wx.CENTER)
        p_sizer2.Add(self.passwor2, 0, wx.CENTER)

        p_sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        p_lbl3 = wx.StaticText(self, label="5 общага:")
        p_sizer3.Add(p_lbl3, 0, wx.CENTER)
        self.password3 = wx.TextCtrl(self,style=wx.TE_PROCESS_ENTER)
        self.password3.Bind(wx.EVT_TEXT_ENTER, self.onLogi1)
        self.passwor3 = wx.TextCtrl(self,style= wx.TE_PROCESS_ENTER)
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
        """
        Check credentials and login
        """
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
        write_sheet.write(3, 12, int(user))
        write_sheet.write(5, 12, int(password))
        write_sheet.write(7, 12, int(password1))
        write_sheet.write(9, 12, int(password2))
        write_sheet.write(11, 12, int(password3))
        write_sheet.write(3, 13, int(user1))
        write_sheet.write(5, 13, int(passwor))
        write_sheet.write(7, 13, int(passwor1))
        write_sheet.write(9, 13, int(passwor2))
        write_sheet.write(11, 13, int(passwor3))
        write_book.save('seb.xls')

        self.Close()


    def EnEraseBackground(self, evt):
        """
        Добавляем фоновое изображение.
        """
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
        wx.Frame.__init__(self, None, size=(650, 600),title="Успешный вход")
        panel = MyPanel(self)
        self.Center()
        dlg = LoginDialog(None)
        dlg.ShowModal()
        authenticated = dlg.logged_in
        dlg.Destroy()

        if not authenticated:
            self.Close()



        self.Center()


class Main(wx.App):

    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()


if __name__ == "__main__":
    app = Main()
    app.MainLoop()
