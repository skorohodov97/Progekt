import wx


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
        bmp = wx.Bitmap("C:\универ\Проэкт\obhaga.jpg")
        dc.DrawBitmap(bmp, 0, 0)

    def onLogin(self, event):
        """
        Check credentials and login
        """
        stupid_password = "password"
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
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)


        btn = wx.Button(self, label="Добро пожаловать")
        sizer.Add(btn, 0, wx.ALL, 260)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP,0 )
        hSizer.Add((1, 1), 0, wx.ALL, 0)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.EnEraseBackground)

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
        bmp = wx.Bitmap("C:\универ\Проэкт\mifi.jpg")
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