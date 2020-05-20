import wx
import json
import time
import wx.adv

format = "%A, %d/%m/%y, %H:%M"       # format for date and time to display
format_onlydate = "%A, %d/%m/%y, "   # format for only date to get date
realtime = time.strftime(format, time.localtime())       # display realtime with standard format

# Make hour choices in Calendar panel to choose
choice_hour = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

# Make minute choices in Calendar panel to choose
choice_minute = []
for i in range(60):
    if i%5 == 0:     # display minute in 5, 10, 15, 20, ...
        if len(str(i))==1:
            choice_minute.append("0"+str(i))
        else:
            choice_minute.append(str(i))


def IsClosingHour(hour, minute, oper_hour_1, oper_hour_2):
    """
    Author: Ta Quynh Nga
    This function is to check if the current/chosen time is within the operating time

    hour, minute: current/chosen time
    oper_hour_1: opening time    (4-character string)
    oper_hour_2: closing time    (4-character string)
    """
    if (int(hour) < int(oper_hour_1[:2])) \
            or (int(hour) == int(oper_hour_1[:2]) and int(minute) < int(oper_hour_1[2:])) \
            or (int(hour) == int(oper_hour_2[:2]) and int(minute) > int(oper_hour_2[2:])) \
            or (int(hour) > int(oper_hour_2[:2])):
        return True
    else:
        return False


def operating_time_msg(stall_name):
    """
    Author: Ta Quynh Nga
    Retrieve the operating hour and show the message to show that the store is not open now.
    """
    with open("Menu/stall_info.txt", 'r') as info_str:
        info_dict = json.loads(info_str.read())          # convert string into dictionary

        # opening time, closing time
        oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]

        # change the data of operating hour from 4-character string (XXXX) to time in format 'XX:XX - XX:XX'
        text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]

    # display the message with information of operating hour the store
    message = stall_name + " is closing now. " + stall_name + " is just open at " + text + \
        ", close on weekend and public holiday."
    message_dlg = wx.MessageDialog(parent=None, message=message, caption="Oops...")
    if message_dlg.ShowModal() == wx.ID_OK:
        message_dlg.Destroy()


# ---------------------------------------- FRAME ----------------------------------
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(800, 650))
        self.date = "null date"
        self.hour = "null hour"
        self.minute = "null minute"

        # Create panels                           # _a is for another day, _t is for today
        self.panel = MyPanel(self)
        self.today_panel = Today(self)
        self.anotherday_panel = AnotherDay(self)
        self.anotherday_panel_stores = AnotherDay_Stores(self)
        self.miniwok_a = MiniWok_A(self)          # _a is another day
        self.miniwok_t = MiniWok_T(self)          # _t is today
        self.chickenrice_a = ChickenRice_A(self)
        self.chickenrice_t = ChickenRice_T(self)
        self.handmadenoodles_a = HandmadeNoodles_A(self)
        self.handmadenoodles_t = HandmadeNoodles_T(self)
        self.malaybbq_a = MalayBBQ_A(self)
        self.malaybbq_t = MalayBBQ_T(self)
        self.vegetarianfood_a = VegetarianFood_A(self)
        self.vegetarianfood_t = VegetarianFood_T(self)
        self.xiancuisine_a = XianCuisine_A(self)
        self.xiancuisine_t = XianCuisine_T(self)
        self.japanesekoreandelight_a = JapaneseKoreanDelight_A(self)
        self.japanesekoreandelight_t = JapaneseKoreanDelight_T(self)
        self.bbqdelight_a = BBQDelight_A(self)
        self.bbqdelight_t = BBQDelight_T(self)
        self.vietnamesecuisine_a = VietnameseCuisine_A(self)
        self.vietnamesecuisine_t = VietnameseCuisine_T(self)
        self.italianpasta_a = ItalianPasta_A(self)
        self.italianpasta_t = ItalianPasta_T(self)

        # Hide all panel except MyPanel (is the Home Panel)
        self.today_panel.Hide()
        self.anotherday_panel.Hide()
        self.anotherday_panel_stores.Hide()
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()
        self.chickenrice_a.Hide()
        self.chickenrice_t.Hide()
        self.handmadenoodles_a.Hide()
        self.handmadenoodles_t.Hide()
        self.malaybbq_a.Hide()
        self.malaybbq_t.Hide()
        self.vegetarianfood_a.Hide()
        self.vegetarianfood_t.Hide()
        self.xiancuisine_a.Hide()
        self.xiancuisine_t.Hide()
        self.japanesekoreandelight_a.Hide()
        self.japanesekoreandelight_t.Hide()
        self.bbqdelight_a.Hide()
        self.bbqdelight_t.Hide()
        self.vietnamesecuisine_a.Hide()
        self.vietnamesecuisine_t.Hide()
        self.italianpasta_a.Hide()
        self.italianpasta_t.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.sizer.Add(self.today_panel, 1, wx.EXPAND)
        self.sizer.Add(self.anotherday_panel, 1, wx.EXPAND)
        self.sizer.Add(self.anotherday_panel_stores, 1, wx.EXPAND)
        self.sizer.Add(self.miniwok_a, 1, wx.EXPAND)
        self.sizer.Add(self.miniwok_t, 1, wx.EXPAND)
        self.sizer.Add(self.chickenrice_a, 1, wx.EXPAND)
        self.sizer.Add(self.chickenrice_t, 1, wx.EXPAND)
        self.sizer.Add(self.handmadenoodles_a, 1, wx.EXPAND)
        self.sizer.Add(self.handmadenoodles_t, 1, wx.EXPAND)
        self.sizer.Add(self.malaybbq_a, 1, wx.EXPAND)
        self.sizer.Add(self.malaybbq_t, 1, wx.EXPAND)
        self.sizer.Add(self.vegetarianfood_a, 1, wx.EXPAND)
        self.sizer.Add(self.vegetarianfood_t, 1, wx.EXPAND)
        self.sizer.Add(self.xiancuisine_a, 1, wx.EXPAND)
        self.sizer.Add(self.xiancuisine_t, 1, wx.EXPAND)
        self.sizer.Add(self.japanesekoreandelight_a, 1, wx.EXPAND)
        self.sizer.Add(self.japanesekoreandelight_t, 1, wx.EXPAND)
        self.sizer.Add(self.bbqdelight_a, 1, wx.EXPAND)
        self.sizer.Add(self.bbqdelight_t, 1, wx.EXPAND)
        self.sizer.Add(self.vietnamesecuisine_a, 1, wx.EXPAND)
        self.sizer.Add(self.vietnamesecuisine_t, 1, wx.EXPAND)
        self.sizer.Add(self.italianpasta_a, 1, wx.EXPAND)
        self.sizer.Add(self.italianpasta_t, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        # Create the icon for the app
        self.SetIcon(wx.Icon("images/icon.png", wx.BITMAP_TYPE_PNG))

    def OnClickToday(self, event):
        """ Go to Today panel after click on "View Today's Stores"."""
        self.panel.Hide()
        self.today_panel.Show()        #####
        self.anotherday_panel.Hide()
        self.anotherday_panel_stores.Hide()
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()
        self.chickenrice_a.Hide()
        self.chickenrice_t.Hide()
        self.handmadenoodles_a.Hide()
        self.handmadenoodles_t.Hide()
        self.malaybbq_a.Hide()
        self.malaybbq_t.Hide()
        self.vegetarianfood_a.Hide()
        self.vegetarianfood_t.Hide()
        self.xiancuisine_a.Hide()
        self.xiancuisine_t.Hide()
        self.japanesekoreandelight_a.Hide()
        self.japanesekoreandelight_t.Hide()
        self.bbqdelight_a.Hide()
        self.bbqdelight_t.Hide()
        self.vietnamesecuisine_a.Hide()
        self.vietnamesecuisine_t.Hide()
        self.italianpasta_a.Hide()
        self.italianpasta_t.Hide()
        self.Layout()

    def OnClickAnother(self, event):
        """Go to Another panel after click on 'View stores by other dates'. """
        self.panel.Hide()
        self.today_panel.Hide()
        self.anotherday_panel.Show()   #####
        self.anotherday_panel_stores.Hide()
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()
        self.chickenrice_a.Hide()
        self.chickenrice_t.Hide()
        self.handmadenoodles_a.Hide()
        self.handmadenoodles_t.Hide()
        self.malaybbq_a.Hide()
        self.malaybbq_t.Hide()
        self.vegetarianfood_a.Hide()
        self.vegetarianfood_t.Hide()
        self.xiancuisine_a.Hide()
        self.xiancuisine_t.Hide()
        self.japanesekoreandelight_a.Hide()
        self.japanesekoreandelight_t.Hide()
        self.bbqdelight_a.Hide()
        self.bbqdelight_t.Hide()
        self.vietnamesecuisine_a.Hide()
        self.vietnamesecuisine_t.Hide()
        self.italianpasta_a.Hide()
        self.italianpasta_t.Hide()
        self.Layout()

    def OnClickBack_Panel(self, event):
        """Go back to Today panel."""
        self.panel.Show()           #####
        self.today_panel.Hide()
        self.anotherday_panel.Hide()
        self.anotherday_panel_stores.Hide()
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()
        self.chickenrice_a.Hide()
        self.chickenrice_t.Hide()
        self.handmadenoodles_a.Hide()
        self.handmadenoodles_t.Hide()
        self.malaybbq_a.Hide()
        self.malaybbq_t.Hide()
        self.vegetarianfood_a.Hide()
        self.vegetarianfood_t.Hide()
        self.xiancuisine_a.Hide()
        self.xiancuisine_t.Hide()
        self.japanesekoreandelight_a.Hide()
        self.japanesekoreandelight_t.Hide()
        self.bbqdelight_a.Hide()
        self.bbqdelight_t.Hide()
        self.vietnamesecuisine_a.Hide()
        self.vietnamesecuisine_t.Hide()
        self.italianpasta_a.Hide()
        self.italianpasta_t.Hide()
        self.Layout()

    def OnClick_Next_A(self, event):
        """Open stores according to chosen date."""
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # re-create the panel
        self.anotherday_panel_stores = AnotherDay_Stores(self)
        self.sizer.Add(self.anotherday_panel_stores, 1, wx.EXPAND)
        # SHOW - HIDE
        self.panel.Hide()
        self.today_panel.Hide()
        self.anotherday_panel.Hide()
        self.anotherday_panel_stores.Show()    #####
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()
        self.chickenrice_a.Hide()
        self.chickenrice_t.Hide()
        self.handmadenoodles_a.Hide()
        self.handmadenoodles_t.Hide()
        self.malaybbq_a.Hide()
        self.malaybbq_t.Hide()
        self.vegetarianfood_a.Hide()
        self.vegetarianfood_t.Hide()
        self.xiancuisine_a.Hide()
        self.xiancuisine_t.Hide()
        self.japanesekoreandelight_a.Hide()
        self.japanesekoreandelight_t.Hide()
        self.bbqdelight_a.Hide()
        self.bbqdelight_t.Hide()
        self.vietnamesecuisine_a.Hide()
        self.vietnamesecuisine_t.Hide()
        self.italianpasta_a.Hide()
        self.italianpasta_t.Hide()
        self.Layout()

    def OnClick_MiniWok_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Mini Wok menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Mini Wok"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))     # Get the current day
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")          # Get the current hour
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")        # Get the current minute
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":     # Canteen is not open on weekend
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.miniwok_a.Hide()
            self.miniwok_t.Show()     #####
            self.Layout()

    def OnClick_MiniWok_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Mini Wok menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Mini Wok"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))    # Get the chosen date
        self.hour = self.anotherday_panel.hour_input.GetValue()                              # Get the chosen hour
        self.minute = self.anotherday_panel.minute_input.GetValue()                          # Get the chosen minute
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")                      # Get the chosen day
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.miniwok_a = MiniWok_A(self)
            self.sizer.Add(self.miniwok_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.miniwok_a.Show()      #####
            self.miniwok_t.Hide()
            self.Layout()

    def OnClick_ChickenRice_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Chicken Rice menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Chicken Rice"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.chickenrice_a.Hide()
            self.chickenrice_t.Show()     #####
            self.Layout()

    def OnClick_ChickenRice_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Chicken Rice menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Chicken Rice"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.chickenrice_a = ChickenRice_A(self)
            self.sizer.Add(self.chickenrice_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.chickenrice_a.Show()      #####
            self.chickenrice_t.Hide()
            self.Layout()

    def OnClick_HandmadeNoodles_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Handmade Noodles menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Hand-made Noodles"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.handmadenoodles_a.Hide()
            self.handmadenoodles_t.Show()     #####
            self.Layout()

    def OnClick_HandmadeNoodles_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Handmade Noodles menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Hand-made Noodles"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.handmadenoodles_a = HandmadeNoodles_A(self)
            self.sizer.Add(self.handmadenoodles_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.handmadenoodles_a.Show()      #####
            self.handmadenoodles_t.Hide()
            self.Layout()

    def OnClick_MalayBBQ_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Malay BBQ menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Malay BBQ"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.malaybbq_a.Hide()
            self.malaybbq_t.Show()     #####
            self.Layout()

    def OnClick_MalayBBQ_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Malay BBQ menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Malay BBQ"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.malaybbq_a = MalayBBQ_A(self)
            self.sizer.Add(self.malaybbq_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.malaybbq_a.Show()      #####
            self.malaybbq_t.Hide()
            self.Layout()

    def OnClick_VegetarianFood_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Vegetarian Food menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Vegetarian Food"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.vegetarianfood_a.Hide()
            self.vegetarianfood_t.Show()     #####
            self.Layout()

    def OnClick_VegetarianFood_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Vegetarian Food menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Vegetarian Food"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.vegetarianfood_a = VegetarianFood_A(self)
            self.sizer.Add(self.vegetarianfood_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.vegetarianfood_a.Show()      #####
            self.vegetarianfood_t.Hide()
            self.Layout()

    def OnClick_XianCuisine_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Xian Cuisine menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Xian Cuisine"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.xiancuisine_a.Hide()
            self.xiancuisine_t.Show()     #####
            self.Layout()

    def OnClick_XianCuisine_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Xian Cuisine menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Xian Cuisine"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.xiancuisine_a = XianCuisine_A(self)
            self.sizer.Add(self.xiancuisine_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.xiancuisine_a.Show()      #####
            self.xiancuisine_t.Hide()
            self.Layout()

    def OnClick_JapaneseKoreanDelight_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Japanese Korean Delight menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Japanese Korean Delight"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.japanesekoreandelight_a.Hide()
            self.japanesekoreandelight_t.Show()     #####
            self.Layout()

    def OnClick_JapaneseKoreanDelight_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Japanese Korean Delight menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Japanese Korean Delight"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.japanesekoreandelight_a = JapaneseKoreanDelight_A(self)
            self.sizer.Add(self.japanesekoreandelight_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.japanesekoreandelight_a.Show()      #####
            self.japanesekoreandelight_t.Hide()
            self.Layout()

    def OnClick_BBQDelight_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's BBQ Delight menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "BBQ Delight"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.bbqdelight_a.Hide()
            self.bbqdelight_t.Show()     #####
            self.Layout()

    def OnClick_BBQDelight_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's BBQ Delight menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "BBQ Delight"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.bbqdelight_a = BBQDelight_A(self)
            self.sizer.Add(self.bbqdelight_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.bbqdelight_a.Show()      #####
            self.bbqdelight_t.Hide()
            self.Layout()

    def OnClick_VietnameseCuisine_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Vietnamese Cuisine menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Vietnamese Cuisine"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.vietnamesecuisine_a.Hide()
            self.vietnamesecuisine_t.Show()     #####
            self.Layout()

    def OnClick_VietnameseCuisine_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Vietnamese Cuisine menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Vietnamese Cuisine"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.vietnamesecuisine_a = VietnameseCuisine_A(self)
            self.sizer.Add(self.vietnamesecuisine_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.vietnamesecuisine_a.Show()      #####
            self.vietnamesecuisine_t.Hide()
            self.Layout()

    def OnClick_ItalianPasta_T(self, event):
        """
        Author: Ta Quynh Nga
        Go to today's Italian Pasta menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Italian Pasta"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        hour_now = wx.DateTime.Format(wx.DateTime.UNow(),"%H")
        minute_now = wx.DateTime.Format(wx.DateTime.UNow(),"%M")
        # IS CLOSING?
        if day_now == "Saturday" or day_now == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(hour_now, minute_now, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # --------- SHOW HIDE -------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.italianpasta_a.Hide()
            self.italianpasta_t.Show()     #####
            self.Layout()

    def OnClick_ItalianPasta_A(self, event):
        """
        Author: Ta Quynh Nga
        Go to another day's Italian Pasta menu.
        """

        # ---- CHANGE THE NAME HERE ----
        stall_name = "Italian Pasta"

        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
        self.date = str(self.anotherday_panel.calendar.GetDate().Format(format_onlydate))
        self.hour = self.anotherday_panel.hour_input.GetValue()
        self.minute = self.anotherday_panel.minute_input.GetValue()
        # IS CLOSING?
        weekday = self.anotherday_panel.calendar.GetDate().Format("%A")
        if weekday == "Saturday" or weekday == "Sunday":
            operating_time_msg(stall_name)
        elif IsClosingHour(self.hour, self.minute, oper_hour_1, oper_hour_2):
            operating_time_msg(stall_name)
        else:
            # ------------ REOPEN PANEL -------------
            self.italianpasta_a = ItalianPasta_A(self)
            self.sizer.Add(self.italianpasta_a, 1, wx.EXPAND)
            # ------------ SHOW - HIDE --------------
            self.panel.Hide()
            self.today_panel.Hide()
            self.anotherday_panel.Hide()
            self.anotherday_panel_stores.Hide()
            self.italianpasta_a.Show()      #####
            self.italianpasta_t.Hide()
            self.Layout()


# ------------------------------- HOME PANEL -------------------------------------
class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        self.SetBackgroundColour("white")

        # Welcome text
        self.welcome1 = wx.StaticText(self, label="NANYANG TECHNOLOGICAL UNIVERSITY", pos=(100, 45))
        self.welcome2 = wx.StaticText(self, label="WELCOME TO NTU NORTH SPINE CANTEEN SYSTEM", pos=(30, 85))
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.welcome1.SetFont(font)
        self.welcome2.SetFont(font)

        # View today's store button
        self.today_button = wx.Button(self, label="View Today's stores", pos=(245, 150), size=(300,50))
        font13 = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.today_button.SetFont(font13)
        self.today_button.SetBackgroundColour("violet")
        self.today_button.SetForegroundColour("white")
        self.today_button.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # View stores by another date
        self.anotherday_button = wx.Button(self, label="View stores by other dates", pos=(245, 205), size=(300, 50))
        self.anotherday_button.SetFont(font13)
        self.anotherday_button.SetBackgroundColour("violet")
        self.anotherday_button.SetForegroundColour("white")
        self.anotherday_button.Bind(wx.EVT_BUTTON, parent.OnClickAnother)

        # add an image
        self.background = wx.StaticBitmap(self, size=(500,500), pos=(210,260))
        self.background.SetBitmap(wx.Bitmap("images/welcome_pic.jpg"))


# ------------------------- PANEL ---------------------------
class Today(wx.Panel):
    """
    Author: Shannon
    """
    def __init__(self, parent):
        super(Today, self).__init__(parent)

        # DISPLAY REAL-TIME
        realtime_text = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        realtime_text.SetFont(font20)

        # STORE BUTTONS
        # --- line 1
        self.MiniWok_btn = wx.Button(self, label="Mini Wok", pos=(50, 100), size=(120, 50))
        self.ChickenRice_btn = wx.Button(self, label="Chicken Rice", pos=(195, 100),
                                         size=(120, 50))
        self.HandmadeNoodles_btn = wx.Button(self, label="Hand-made \nNoodles", pos=(335, 100),
                                             size=(120, 50))
        self.MalayBBQ_btn = wx.Button(self, label="Malay BBQ", pos=(475, 100), size=(120, 50))
        self.VegetarianFood_btn = wx.Button(self, label="Vegetarian Food", pos=(615, 100),
                                            size=(120, 50))
        # --- line 2
        self.XianCuisine_btn = wx.Button(self, label="Xian Cuisine", pos=(50, 170), size=(120, 50))
        self.JapaneseKoreanDelight_btn = wx.Button(self, label="Japanese\nKorean Delight",
                                                   pos=(195, 170), size=(120, 50))
        self.BBQDelight_btn = wx.Button(self, label="BBQ Delight", pos=(335, 170), size=(120, 50))
        self.VietnameseCuisine_btn = wx.Button(self, label="Vietnamese \nCuisine", pos=(475, 170),
                                               size=(120, 50))
        self.ItalianPasta_btn = wx.Button(self, label="Italian Pasta", pos=(615, 170), size=(120, 50))
        # ------ set font -----
        font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
        self.MiniWok_btn.SetFont(font11)
        self.ChickenRice_btn.SetFont(font11)
        self.HandmadeNoodles_btn.SetFont(font11)
        self.MalayBBQ_btn.SetFont(font11)
        self.VegetarianFood_btn.SetFont(font11)
        self.XianCuisine_btn.SetFont(font11)
        self.JapaneseKoreanDelight_btn.SetFont(font11)
        self.BBQDelight_btn.SetFont(font11)
        self.VietnameseCuisine_btn.SetFont(font11)
        self.ItalianPasta_btn.SetFont(font11)
        # ------ set color background -----
        self.MiniWok_btn.SetBackgroundColour("coral")
        self.ChickenRice_btn.SetBackgroundColour("coral")
        self.HandmadeNoodles_btn.SetBackgroundColour("coral")
        self.MalayBBQ_btn.SetBackgroundColour("coral")
        self.VegetarianFood_btn.SetBackgroundColour("coral")
        self.XianCuisine_btn.SetBackgroundColour("coral")
        self.JapaneseKoreanDelight_btn.SetBackgroundColour("coral")
        self.BBQDelight_btn.SetBackgroundColour("coral")
        self.VietnameseCuisine_btn.SetBackgroundColour("coral")
        self.ItalianPasta_btn.SetBackgroundColour("coral")
        # ----- Bind function to change panels -----
        self.MiniWok_btn.Bind(wx.EVT_BUTTON, parent.OnClick_MiniWok_T)
        self.ChickenRice_btn.Bind(wx.EVT_BUTTON, parent.OnClick_ChickenRice_T)
        self.HandmadeNoodles_btn.Bind(wx.EVT_BUTTON, parent.OnClick_HandmadeNoodles_T)
        self.MalayBBQ_btn.Bind(wx.EVT_BUTTON, parent.OnClick_MalayBBQ_T)
        self.VegetarianFood_btn.Bind(wx.EVT_BUTTON, parent.OnClick_VegetarianFood_T)
        self.XianCuisine_btn.Bind(wx.EVT_BUTTON, parent.OnClick_XianCuisine_T)
        self.JapaneseKoreanDelight_btn.Bind(wx.EVT_BUTTON, parent.OnClick_JapaneseKoreanDelight_T)
        self.BBQDelight_btn.Bind(wx.EVT_BUTTON, parent.OnClick_BBQDelight_T)
        self.VietnameseCuisine_btn.Bind(wx.EVT_BUTTON, parent.OnClick_VietnameseCuisine_T)
        self.ItalianPasta_btn.Bind(wx.EVT_BUTTON, parent.OnClick_ItalianPasta_T)

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickBack_Panel)

        # ADD AN IMAGE
        self.background = wx.StaticBitmap(self, size=(500, 500), pos=(135, 240))
        self.background.SetBitmap(wx.Bitmap("images/food_sketch.png"))

        # SET WHITE BACKGROUND
        self.SetBackgroundColour('white')


class AnotherDay(wx.Panel):
    """
    Author: Ta Quynh Nga
    This class display a calendar and time for user to choose.
    """
    def __init__(self, parent):
        super(AnotherDay, self).__init__(parent)

        # BACK BUTTON
        self.Back_btn = wx.Button(self, label="Back", pos=(100, 540), size=(300, 50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.Back_btn.SetFont(font12)
        self.Back_btn.SetBackgroundColour("orange")
        self.Back_btn.SetForegroundColour("white")
        self.Back_btn.Bind(wx.EVT_BUTTON, parent.OnClickBack_Panel)
        # NEXT BUTTON
        self.Next_btn = wx.Button(self, label="Next", pos=(400, 540), size=(300, 50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.Next_btn.SetFont(font12)
        self.Next_btn.SetBackgroundColour("SEA GREEN")
        self.Next_btn.SetForegroundColour("white")
        self.Next_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # CREATE CALENDAR TO PICK A DATE
        self.calendar = wx.adv.CalendarCtrl(self, pos=(230, 100), size=(300,200),
                                            style=wx.adv.CAL_SHOW_HOLIDAYS)

        # DISPLAY CURRENT DATE AND TIME
        self.date_str = str(wx.DateTime.Format(wx.DateTime.UNow(),format))
        self.date = wx.StaticText(self, label=self.date_str, pos=(230,35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)

        # ENTER HOUR AND MINUTE
        self.time_text = wx.StaticText(self, label="Time: ", pos=(230, 350))
        self.time_text.SetFont(font20)
        self.hour_input = wx.ComboBox(self, value='00', pos=(330,350), size=(45,50),
                                      choices=choice_hour, style=wx.CB_READONLY)
        self.colon = wx.StaticText(self, label=":", pos=(380,350))
        self.minute_input = wx.ComboBox(self, value='00', pos=(400,350), size=(45,50),
                                        choices=choice_minute, style=wx.CB_READONLY)
        font11_normal = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
        self.hour_input.SetFont(font11_normal)
        self.minute_input.SetFont(font11_normal)
        self.colon.SetFont(font20)
        # set default value
        self.hour_input.SetValue('11')
        self.minute_input.SetValue('00')


# ------------------- DISPLAY STORES AFTER CHOSING A DATE ---------------------
class AnotherDay_Stores(wx.Panel):
    """Author: Shannon"""
    def __init__(self, parent):
        super(AnotherDay_Stores, self).__init__(parent)

        # DISPLAY CHOSEN DATE
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date + chosen_hour + ":" + chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)

        # STORE BUTTONS
        # --- row 1
        self.MiniWok_btn = wx.Button(self, label="Mini Wok", pos=(50, 100), size=(120, 50))
        self.ChickenRice_btn = wx.Button(self, label="Chicken Rice", pos=(195, 100), size=(120, 50))
        self.HandmadeNoodles_btn = wx.Button(self, label="Hand-made \nNoodles", pos=(335, 100), size=(120, 50))
        self.MalayBBQ_btn = wx.Button(self, label="Malay BBQ", pos=(475, 100), size=(120, 50))
        self.VegetarianFood_btn = wx.Button(self, label="Vegetarian Food", pos=(615, 100), size=(120, 50))
        # --- row 2
        self.XianCuisine_btn = wx.Button(self, label="Xian Cuisine", pos=(50, 170), size=(120, 50))
        self.JapaneseKoreanDelight_btn = wx.Button(self, label="Japanese\nKorean Delight", pos=(195, 170), size=(120, 50))
        self.BBQDelight_btn = wx.Button(self, label="BBQ Delight", pos=(335, 170), size=(120, 50))
        self.VietnameseCuisine_btn = wx.Button(self, label="Vietnamese \nCuisine", pos=(475, 170), size=(120, 50))
        self.ItalianPasta_btn = wx.Button(self, label="Italian Pasta", pos=(615, 170), size=(120, 50))
        # ------ set font -----
        font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
        self.MiniWok_btn.SetFont(font11)
        self.ChickenRice_btn.SetFont(font11)
        self.HandmadeNoodles_btn.SetFont(font11)
        self.MalayBBQ_btn.SetFont(font11)
        self.VegetarianFood_btn.SetFont(font11)
        self.XianCuisine_btn.SetFont(font11)
        self.JapaneseKoreanDelight_btn.SetFont(font11)
        self.BBQDelight_btn.SetFont(font11)
        self.VietnameseCuisine_btn.SetFont(font11)
        self.ItalianPasta_btn.SetFont(font11)
        # ------ set color background -----
        self.MiniWok_btn.SetBackgroundColour("coral")
        self.ChickenRice_btn.SetBackgroundColour("coral")
        self.HandmadeNoodles_btn.SetBackgroundColour("coral")
        self.MalayBBQ_btn.SetBackgroundColour("coral")
        self.VegetarianFood_btn.SetBackgroundColour("coral")
        self.XianCuisine_btn.SetBackgroundColour("coral")
        self.JapaneseKoreanDelight_btn.SetBackgroundColour("coral")
        self.BBQDelight_btn.SetBackgroundColour("coral")
        self.VietnameseCuisine_btn.SetBackgroundColour("coral")
        self.ItalianPasta_btn.SetBackgroundColour("coral")
        # ----- Bind function to change panels -----
        self.MiniWok_btn.Bind(wx.EVT_BUTTON, parent.OnClick_MiniWok_A)
        self.ChickenRice_btn.Bind(wx.EVT_BUTTON, parent.OnClick_ChickenRice_A)
        self.HandmadeNoodles_btn.Bind(wx.EVT_BUTTON, parent.OnClick_HandmadeNoodles_A)
        self.MalayBBQ_btn.Bind(wx.EVT_BUTTON, parent.OnClick_MalayBBQ_A)
        self.VegetarianFood_btn.Bind(wx.EVT_BUTTON, parent.OnClick_VegetarianFood_A)
        self.XianCuisine_btn.Bind(wx.EVT_BUTTON, parent.OnClick_XianCuisine_A)
        self.JapaneseKoreanDelight_btn.Bind(wx.EVT_BUTTON, parent.OnClick_JapaneseKoreanDelight_A)
        self.BBQDelight_btn.Bind(wx.EVT_BUTTON, parent.OnClick_BBQDelight_A)
        self.VietnameseCuisine_btn.Bind(wx.EVT_BUTTON, parent.OnClick_VietnameseCuisine_A)
        self.ItalianPasta_btn.Bind(wx.EVT_BUTTON, parent.OnClick_ItalianPasta_A)

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickAnother)

        # ADD AN IMAGE
        self.background = wx.StaticBitmap(self, size=(500, 500), pos=(135, 240))
        self.background.SetBitmap(wx.Bitmap("images/food_sketch.png"))

        # SET WHITE BACKGROUND
        self.SetBackgroundColour('white')


# ############################## STORE PANELS #################################
# #############################################################################

# ------------------------------- MINI WOK ------------------------------------
class MiniWok(wx.Panel):
    """Author: Ta Quynh Nga and William"""
    def __init__(self, parent):
        super(MiniWok, self).__init__(parent)

        self.stall_name = "Mini Wok"
        image_path = "images/miniwok.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=self.stall_name, pos=(50, 100), size=(330,400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[self.stall_name][1], info_dict[self.stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " +text, pos=(60, 130))
            self.font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(self.font11)
            self.waiting_time_value = info_dict[self.stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 393))
        self.enter_text.SetFont(self.font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 390), size=(50, 25))
        self.enter_space.SetFont(self.font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 430))
        self.waiting_time_text.SetFont(self.font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 427), size=(50, 25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(self.font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 387), size=(100, 30))
        self.font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(self.font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244, 430))
        minute.SetFont(self.font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            # check if it is a string
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            # check if it is negative or a float number
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))



class MiniWok_T(MiniWok):
    """Author: Ta Quynh Nga and William"""
    def __init__(self, parent):
        super(MiniWok_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT TIME
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)

        # DISPLAY MENU BY DAY IN A WEEK
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        # Monday Wednesday Friday
        if day_now == 'Monday' or day_now == "Wednesday" or day_now == "Friday":
            with open("Menu/" + self.stall_name + ".txt", 'r') as stall:
                count = 0
                even = 0
                for line in stall.readlines()[1:]:
                    if even%2 == 0:
                        food = line.strip().split('\t')  # 'food' is a list [no., food, price]
                        position1 = (410, 130 + count * 18)
                        position2 = (670, 130 + count * 18)
                        position_heading = (430, 130 + count * 18)
                        if len(food) != 1:
                            self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                            self.price = wx.StaticText(self, label=food[2], pos=position2)
                            self.food_name.SetFont(self.font11)
                            self.price.SetFont(self.font11)
                            if count % 2 != 0:
                                self.food_name.SetForegroundColour("sea green")
                                self.price.SetForegroundColour("sea green")
                        else:
                            self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                            self.heading.SetFont(self.font11bold)
                        count -= 1
                    even += 1
                    count += 1
        # Tuesday Thursday
        if day_now == 'Tuesday' or day_now == "Thursday":
            with open("Menu/" + self.stall_name + ".txt", 'r') as stall:
                count = 0
                even = 0
                for line in stall.readlines()[1:]:
                    if even%2 != 0:
                        food = line.strip().split('\t')  # 'food' is a list [no., food, price]
                        position1 = (410, 130 + count * 18)
                        position2 = (670, 130 + count * 18)
                        position_heading = (430, 130 + count * 18)
                        if len(food) != 1:
                            self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                            self.price = wx.StaticText(self, label=food[2], pos=position2)
                            self.food_name.SetFont(self.font11)
                            self.price.SetFont(self.font11)
                            if count % 2 != 0:
                                self.food_name.SetForegroundColour("sea green")
                                self.price.SetForegroundColour("sea green")
                        else:
                            self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                            self.heading.SetFont(self.font11bold)
                        count -= 1
                    even += 1
                    count += 1


class MiniWok_A(MiniWok):
    """Author: Ta Quynh Nga and William"""
    def __init__(self, parent):
        super(MiniWok_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date+chosen_hour+":"+chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)

        # DISPLAY MENU BY DAY IN A WEEK
        weekday = parent.anotherday_panel.calendar.GetDate().Format("%A")
        # Monday Wednesday Friday
        if weekday == 'Monday' or weekday == "Wednesday" or weekday == "Friday":
            with open("Menu/" + self.stall_name + ".txt", 'r') as stall:
                count = 0
                even = 0
                for line in stall.readlines()[1:]:
                    food = line.strip().split('\t')         # 'food' is a list [no., food, price]
                    position1 = (410, 130 + count * 18)     # position of food
                    position2 = (670, 130 + count * 18)     # position of price
                    position_heading = (430, 130 + count * 18)
                    if len(food) == 1:                      # This line is a heading
                        self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                        self.heading.SetFont(self.font11bold)
                        even = 0
                    elif even % 2 == 0:                     # This line has food and price info
                        self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                        self.price = wx.StaticText(self, label=food[2], pos=position2)
                        self.food_name.SetFont(self.font11)
                        self.price.SetFont(self.font11)
                        if count % 2 != 0:
                            self.food_name.SetForegroundColour("sea green")
                            self.price.SetForegroundColour("sea green")
                    else:
                        count -= 1
                    count += 1
                    even += 1

        # Tuesday Thursday
        if weekday == 'Tuesday' or weekday == "Thursday":
            with open("Menu/" + self.stall_name + ".txt", 'r') as stall:
                count = 0
                even = 0
                for line in stall.readlines()[1:]:
                    food = line.strip().split('\t')  # 'food' is a list [no., food, price]
                    position1 = (410, 130 + count * 18)
                    position2 = (670, 130 + count * 18)
                    position_heading = (430, 130 + count * 18)
                    if len(food) == 1:
                        self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                        self.heading.SetFont(self.font11bold)
                        even = 0
                    elif even % 2 != 0:
                        self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                        self.price = wx.StaticText(self, label=food[2], pos=position2)
                        self.food_name.SetFont(self.font11)
                        self.price.SetFont(self.font11)
                        if count % 2 != 0:
                            self.food_name.SetForegroundColour("sea green")
                            self.price.SetForegroundColour("sea green")
                    else:
                        count -= 1
                    count += 1
                    even += 1


# -------------------------- CHICKEN RICE -----------------------------
class ChickenRice(wx.Panel):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(ChickenRice, self).__init__(parent)

        stall_name = "Chicken Rice"
        image_path = "images/chickenrice.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=stall_name, pos=(50, 100), size=(330, 400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " + text, pos=(60, 130))
            font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(font11)
            self.waiting_time_value = info_dict[stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 403))
        self.enter_text.SetFont(font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 400), size=(50, 25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 440))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 437), size=(50, 25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 397), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244, 440))
        minute.SetFont(font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)
        # ------------- display --------------
        with open("Menu/" + stall_name + ".txt", 'r') as stall:
            count = 0
            for line in stall.readlines()[1:]:
                food = line.strip().split('\t')  # 'food' is a list [no. food price]
                position1 = (410, 130 + count * 18)     # position of food
                position2 = (670, 130 + count * 18)     # position of price
                if len(food) != 1:
                    self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                    self.price = wx.StaticText(self, label=food[2], pos=position2)
                    self.food_name.SetFont(font11)      # set font
                    self.price.SetFont(font11)          # set font
                    if count % 2 != 0:              # alternate color line by line
                        self.food_name.SetForegroundColour("sea green")
                        self.price.SetForegroundColour("sea green")
                else:               # this line is a heading
                    self.heading = wx.StaticText(self, label=food[1], pos=position1)
                    self.heading.SetFont(font11)
                count += 1

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230, 540), size=(300, 50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))


class ChickenRice_T(ChickenRice):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(ChickenRice_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT DATE
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)


class ChickenRice_A(ChickenRice):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(ChickenRice_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date + chosen_hour + ":" + chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)


# -------------------------- HANDMADE NOODLES -------------------------
class HandmadeNoodles(wx.Panel):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(HandmadeNoodles, self).__init__(parent)

        stall_name = "Hand-made Noodles"
        image_path = "images/HandmadeNoodles.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=stall_name, pos=(50, 100), size=(330, 400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " + text, pos=(60, 130))
            font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(font11)
            self.waiting_time_value = info_dict[stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 403))
        self.enter_text.SetFont(font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 400), size=(50, 25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 440))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 437), size=(50, 25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 397), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244, 440))
        minute.SetFont(font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)
        # ------------- display --------------
        with open("Menu/" + stall_name + ".txt", 'r') as stall:
            count = 0
            for line in stall.readlines()[1:]:
                food = line.strip().split('\t')  # 'food' is a list [no. food price]
                position1 = (410, 130 + count * 18)
                position2 = (670, 130 + count * 18)
                if len(food) != 1:
                    self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                    self.price = wx.StaticText(self, label=food[2], pos=position2)
                    self.food_name.SetFont(font11)
                    self.price.SetFont(font11)
                    if count % 2 != 0:
                        self.food_name.SetForegroundColour("sea green")
                        self.price.SetForegroundColour("sea green")
                else:
                    self.heading = wx.StaticText(self, label=food[1], pos=position1)
                    self.heading.SetFont(font11)
                count += 1

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230, 540), size=(300, 50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))


class HandmadeNoodles_T(HandmadeNoodles):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(HandmadeNoodles_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT DATE
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)


class HandmadeNoodles_A(HandmadeNoodles):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(HandmadeNoodles_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date + chosen_hour + ":" + chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)


# ------------------------- MALAY BBQ ---------------------------------
class MalayBBQ(wx.Panel):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(MalayBBQ, self).__init__(parent)

        stall_name = "Malay BBQ"
        image_path = "images/MalayBBQ.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=stall_name, pos=(50, 100), size=(330,400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " +text, pos=(60, 130))
            font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(font11)
            self.waiting_time_value = info_dict[stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 383))
        self.enter_text.SetFont(font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 380), size=(50,25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 420))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 417), size=(50,25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 377), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244,420))
        minute.SetFont(font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)
        # ------------- display --------------
        with open("Menu/"+stall_name+".txt", 'r') as stall:
            count = 0
            for line in stall.readlines()[1:]:
                food = line.strip().split('\t')              # 'food' is a list [no. food price]
                position1 = (410, 130 + count * 18)
                position2 = (670, 130 + count * 18)
                if len(food) != 1:
                    self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                    self.price = wx.StaticText(self, label=food[2], pos=position2)
                    self.food_name.SetFont(font11)
                    self.price.SetFont(font11)
                    if count % 2 != 0:
                        self.food_name.SetForegroundColour("sea green")
                        self.price.SetForegroundColour("sea green")
                else:
                    self.heading = wx.StaticText(self, label=food[1], pos=position1)
                    self.heading.SetFont(font11)
                count += 1

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))

class MalayBBQ_T(MalayBBQ):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(MalayBBQ_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT DATE
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)

class MalayBBQ_A(MalayBBQ):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(MalayBBQ_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date + chosen_hour + ":" + chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)


# ----------------------- VEGETARIAN FOOD -----------------------------
class VegetarianFood(wx.Panel):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(VegetarianFood, self).__init__(parent)

        stall_name = "Vegetarian Food"
        image_path = "images/VegetarianFood.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=stall_name, pos=(50, 100), size=(330,400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " +text, pos=(60, 130))
            font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(font11)
            self.waiting_time_value = info_dict[stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 393))
        self.enter_text.SetFont(font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 390), size=(50, 25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 430))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 427), size=(50, 25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 387), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244, 430))
        minute.SetFont(font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)
        # ------------- display --------------
        with open("Menu/"+stall_name+".txt", 'r') as stall:
            count = 0
            for line in stall.readlines()[1:]:
                food = line.strip().split('\t')              # 'food' is a list [no., food, price]
                position1 = (410, 130 + count * 18)
                position2 = (670, 130 + count * 18)
                position_heading = (430, 130 + count * 18)
                if len(food) != 1:
                    self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                    self.price = wx.StaticText(self, label=food[2], pos=position2)
                    self.food_name.SetFont(font11)
                    self.price.SetFont(font11)
                    if count % 2 != 0:
                        self.food_name.SetForegroundColour("sea green")
                        self.price.SetForegroundColour("sea green")
                else:
                    self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                    self.heading.SetFont(font11bold)
                count += 1

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))


class VegetarianFood_T(VegetarianFood):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(VegetarianFood_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT TIME
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)


class VegetarianFood_A(VegetarianFood):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(VegetarianFood_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date+chosen_hour+":"+chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)


# --------------------------- XIAN CUISINE ----------------------------
class XianCuisine(wx.Panel):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(XianCuisine, self).__init__(parent)

        stall_name = "Xian Cuisine"
        image_path = "images/XianCuisine.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=stall_name, pos=(50, 100), size=(330,400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " +text, pos=(60, 130))
            font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(font11)
            self.waiting_time_value = info_dict[stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 393))
        self.enter_text.SetFont(font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 390), size=(50, 25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 430))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 427), size=(50, 25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 387), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244, 430))
        minute.SetFont(font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)
        # ------------- display --------------
        with open("Menu/"+stall_name+".txt", 'r') as stall:
            count = 0
            for line in stall.readlines()[1:]:
                food = line.strip().split('\t')              # 'food' is a list [no., food, price]
                position1 = (410, 130 + count * 18)
                position2 = (670, 130 + count * 18)
                position_heading = (430, 130 + count * 18)
                if len(food) != 1:
                    self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                    self.price = wx.StaticText(self, label=food[2], pos=position2)
                    self.food_name.SetFont(font11)
                    self.price.SetFont(font11)
                    if count % 2 != 0:
                        self.food_name.SetForegroundColour("sea green")
                        self.price.SetForegroundColour("sea green")
                else:
                    self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                    self.heading.SetFont(font11bold)
                count += 1

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))


class XianCuisine_T(XianCuisine):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(XianCuisine_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT TIME
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)


class XianCuisine_A(XianCuisine):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(XianCuisine_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date+chosen_hour+":"+chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)


# -------------------- JAPANESE KOREAN DELIGHT ------------------------
class JapaneseKoreanDelight(wx.Panel):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(JapaneseKoreanDelight, self).__init__(parent)

        stall_name = "Japanese Korean Delight"
        image_path = "images/JapKorDelight.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=stall_name, pos=(50, 100), size=(330,400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " +text, pos=(60, 130))
            font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(font11)
            self.waiting_time_value = info_dict[stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 413))
        self.enter_text.SetFont(font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 410), size=(50,25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 450))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 447), size=(50,25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 407), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244,450))
        minute.SetFont(font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)
        # ------------- display --------------
        with open("Menu/"+stall_name+".txt", 'r') as stall:
            count = 0
            for line in stall.readlines()[1:]:
                food = line.strip().split('\t')              # 'food' is a list [no. food price]
                position1 = (410, 130 + count * 18)
                position2 = (670, 130 + count * 18)
                if len(food) != 1:
                    self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                    self.price = wx.StaticText(self, label=food[2], pos=position2)
                    self.food_name.SetFont(font11)
                    self.price.SetFont(font11)
                    if count % 2 != 0:
                        self.food_name.SetForegroundColour("sea green")
                        self.price.SetForegroundColour("sea green")
                else:
                    self.heading = wx.StaticText(self, label=food[1], pos=position1)
                    self.heading.SetFont(font11)
                count += 1

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))


class JapaneseKoreanDelight_T(JapaneseKoreanDelight):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(JapaneseKoreanDelight_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT DATE
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)


class JapaneseKoreanDelight_A(JapaneseKoreanDelight):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(JapaneseKoreanDelight_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date + chosen_hour + ":" + chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)


# ---------------------------- BBQ DELIGHT ----------------------------
class BBQDelight(wx.Panel):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(BBQDelight, self).__init__(parent)

        stall_name = "BBQ Delight"
        image_path = "images/BBQDelight.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=stall_name, pos=(50, 100), size=(330,400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " +text, pos=(60, 130))
            font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(font11)
            self.waiting_time_value = info_dict[stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 393))
        self.enter_text.SetFont(font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 390), size=(50, 25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 430))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 427), size=(50, 25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 387), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244, 430))
        minute.SetFont(font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)
        # ------------- display --------------
        with open("Menu/"+stall_name+".txt", 'r') as stall:
            count = 0
            for line in stall.readlines()[1:]:
                food = line.strip().split('\t')              # 'food' is a list [no., food, price]
                position1 = (410, 130 + count * 18)
                position2 = (670, 130 + count * 18)
                position_heading = (430, 130 + count * 18)
                if len(food) != 1:
                    self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                    self.price = wx.StaticText(self, label=food[2], pos=position2)
                    self.food_name.SetFont(font11)
                    self.price.SetFont(font11)
                    if count % 2 != 0:
                        self.food_name.SetForegroundColour("sea green")
                        self.price.SetForegroundColour("sea green")
                else:
                    self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                    self.heading.SetFont(font11bold)
                count += 1

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))


class BBQDelight_T(BBQDelight):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(BBQDelight_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT TIME
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)


class BBQDelight_A(BBQDelight):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(BBQDelight_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date+chosen_hour+":"+chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)


# ----------------------- VIETNAMESE CUISINE --------------------------
class VietnameseCuisine(wx.Panel):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(VietnameseCuisine, self).__init__(parent)

        stall_name = "Vietnamese Cuisine"
        image_path = "images/VietnameseCuisine.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=stall_name, pos=(50, 100), size=(330,400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[stall_name][1], info_dict[stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " +text, pos=(60, 130))
            font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(font11)
            self.waiting_time_value = info_dict[stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 170))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 373))
        self.enter_text.SetFont(font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 370), size=(50, 25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 410))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 407), size=(50, 25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 367), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244, 410))
        minute.SetFont(font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)
        # ------------- display --------------
        with open("Menu/"+stall_name+".txt", 'r') as stall:
            count = 0
            for line in stall.readlines()[1:]:
                food = line.strip().split('\t')              # 'food' is a list [no., food, price]
                position1 = (410, 130 + count * 18)
                position2 = (670, 130 + count * 18)
                position_heading = (430, 130 + count * 18)
                if len(food) != 1:
                    self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                    self.price = wx.StaticText(self, label=food[2], pos=position2)
                    self.food_name.SetFont(font11)
                    self.price.SetFont(font11)
                    if count % 2 != 0:
                        self.food_name.SetForegroundColour("sea green")
                        self.price.SetForegroundColour("sea green")
                else:
                    self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                    self.heading.SetFont(font11bold)
                count += 1

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))


class VietnameseCuisine_T(VietnameseCuisine):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(VietnameseCuisine_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT TIME
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)


class VietnameseCuisine_A(VietnameseCuisine):
    """Author: Ta Quynh Nga"""
    def __init__(self, parent):
        super(VietnameseCuisine_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date+chosen_hour+":"+chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)


# -------------------------- ITALIAN PASTA ----------------------------
class ItalianPasta(wx.Panel):
    """Author: Ta Quynh Nga and William"""
    def __init__(self, parent):
        super(ItalianPasta, self).__init__(parent)

        self.stall_name = "Italian Pasta"
        image_path = "images/ItalianPasta.jpg"

        # ____________________________DISPLAY INFO ON THE LEFT_____________________________________
        # ---------------- name ------------------
        self.info_box = wx.StaticBox(self, label=self.stall_name, pos=(50, 100), size=(330,400))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.info_box.SetFont(font12)
        # --- operating hour and waiting time ----
        with open("Menu/stall_info.txt", 'r') as info_str:
            info_dict = json.loads(info_str.read())  # convert string into dictionary
            oper_hour_1, oper_hour_2 = info_dict[self.stall_name][1], info_dict[self.stall_name][2]
            text = oper_hour_1[:2] + ":" + oper_hour_1[2:] + " - " + oper_hour_2[:2] + ":" + oper_hour_2[2:]
            self.oper_hour_text = wx.StaticText(self, label="Operating hour: " +text, pos=(60, 130))
            self.font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
            self.oper_hour_text.SetFont(self.font11)
            self.waiting_time_value = info_dict[self.stall_name][0]
        # ------------- add an image ---------------
        self.image = wx.StaticBitmap(self, size=(500, 500), pos=(60, 160))
        self.image.SetBitmap(wx.Bitmap(image_path))
        # ---------- calculate waiting time --------
        self.enter_text = wx.StaticText(self, label="Enter no. of pax:", pos=(60, 393))
        self.enter_text.SetFont(self.font11)
        self.enter_space = wx.TextCtrl(self, pos=(180, 390), size=(50, 25))
        self.enter_space.SetFont(self.font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 430))
        self.waiting_time_text.SetFont(self.font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 427), size=(50, 25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(self.font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 387), size=(100, 30))
        self.font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(self.font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244, 430))
        minute.SetFont(self.font11)

        # __________________________DISPLAY MENU TO THE RIGHT_____________________________________
        self.menu_box = wx.StaticBox(self, label="Menu", pos=(400, 100), size=(330, 400))
        self.menu_box.SetFont(font12)

        # BACK BUTTON
        self.back_btn = wx.Button(self, label="Back", pos=(230,540), size=(300,50))
        font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.back_btn.SetFont(font12)
        self.back_btn.SetBackgroundColour("orange")
        self.back_btn.SetForegroundColour("white")

    def OnCalculate(self, event):
        """
        Author: Ta Quynh Nga
        This function calculates waiting time of the queuing line
        """
        try:
            result = int(self.enter_space.GetValue()) * self.waiting_time_value
        except:
            message = wx.MessageDialog(parent=None,
                                       message="Invalid input. \nPlease key in a whole number!")
            if message.ShowModal() == wx.ID_OK:
                self.enter_space.SetValue('')
                self.waiting_time_result.SetLabel('')
                message.Destroy()
        else:
            if result < 0 or float(self.enter_space.GetValue()) > result:
                message = wx.MessageDialog(parent=None,
                                           message="Invalid input. \nPlease key in a whole number!")
                if message.ShowModal() == wx.ID_OK:
                    self.enter_space.SetValue('')
                    self.waiting_time_result.SetLabel('')
                    message.Destroy()
            else:
                self.waiting_time_result.SetLabel(str(result))


class ItalianPasta_T(ItalianPasta):
    """Author: Ta Quynh Nga and William"""
    def __init__(self, parent):
        super(ItalianPasta_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT TIME
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)

        # DISPLAY MENU BY DAY IN A WEEK
        day_now = str(wx.DateTime.Format(wx.DateTime.UNow(), "%A"))
        # Monday Wednesday Friday
        if day_now == 'Monday' or day_now == "Wednesday" or day_now == "Friday":
            with open("Menu/" + self.stall_name + ".txt", 'r') as stall:
                count = 0   # change color alternatively among lines variable
                even = 0    # check if the order of line is even or odd
                for line in stall.readlines()[1:]:
                    food = line.strip().split('\t')  # 'food' is a list [no., food, price]
                    position1 = (410, 130 + count * 18)
                    position2 = (670, 130 + count * 18)
                    position_heading = (430, 130 + count * 18)
                    if len(food) == 1:               # this is a heading
                        self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                        self.heading.SetFont(self.font11bold)
                        even = 0
                    elif even % 2 == 0:              # display even lines
                        self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                        self.price = wx.StaticText(self, label=food[2], pos=position2)
                        self.food_name.SetFont(self.font11)
                        self.price.SetFont(self.font11)
                        if count % 2 != 0:           # change the color alternatively among lines
                            self.food_name.SetForegroundColour("sea green")
                            self.price.SetForegroundColour("sea green")
                    else:
                        count -= 1
                    count += 1
                    even += 1

        # Tuesday Thursday
        if day_now == 'Tuesday' or day_now == "Thursday":
            with open("Menu/" + self.stall_name + ".txt", 'r') as stall:
                count = 0   # change color alternatively among lines variable
                even = 0    # check if the order of line is even or odd
                for line in stall.readlines()[1:]:
                    food = line.strip().split('\t')  # 'food' is a list [no., food, price]
                    position1 = (410, 130 + count * 18)
                    position2 = (670, 130 + count * 18)
                    position_heading = (430, 130 + count * 18)
                    if len(food) == 1:               # this is a heading
                        self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                        self.heading.SetFont(self.font11bold)
                        even = 0
                    elif even % 2 != 0:              # display odd lines
                        self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                        self.price = wx.StaticText(self, label=food[2], pos=position2)
                        self.food_name.SetFont(self.font11)
                        self.price.SetFont(self.font11)
                        if count % 2 != 0:           # change the color alternatively among lines
                            self.food_name.SetForegroundColour("sea green")
                            self.price.SetForegroundColour("sea green")
                    else:
                        count -= 1
                    count += 1
                    even += 1


class ItalianPasta_A(ItalianPasta):
    """Author: Ta Quynh Nga and William"""
    def __init__(self, parent):
        super(ItalianPasta_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClick_Next_A)

        # DISPLAY CHOSEN TIME
        chosen_date = parent.date
        chosen_hour = parent.hour
        chosen_minute = parent.minute
        display_time = chosen_date+chosen_hour+":"+chosen_minute
        self.chosen_date_text = wx.StaticText(self, label=display_time, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date_text.SetFont(font20)

        # DISPLAY MENU BY DAY IN A WEEK
        weekday = parent.anotherday_panel.calendar.GetDate().Format("%A")
        # Monday Wednesday Friday
        if weekday == 'Monday' or weekday == "Wednesday" or weekday == "Friday":
            with open("Menu/" + self.stall_name + ".txt", 'r') as stall:
                count = 0
                even = 0
                for line in stall.readlines()[1:]:
                    food = line.strip().split('\t')  # 'food' is a list [no., food, price]
                    position1 = (410, 130 + count * 18)
                    position2 = (670, 130 + count * 18)
                    position_heading = (430, 130 + count * 18)
                    if len(food) == 1:
                        self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                        self.heading.SetFont(self.font11bold)
                        even = 0
                    elif even % 2 == 0:
                        self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                        self.price = wx.StaticText(self, label=food[2], pos=position2)
                        self.food_name.SetFont(self.font11)
                        self.price.SetFont(self.font11)
                        if count % 2 != 0:
                            self.food_name.SetForegroundColour("sea green")
                            self.price.SetForegroundColour("sea green")
                    else:
                        count -= 1
                    count += 1
                    even += 1

        # Tuesday Thursday
        if weekday == 'Tuesday' or weekday == "Thursday":
            with open("Menu/" + self.stall_name + ".txt", 'r') as stall:
                count = 0
                even = 0
                for line in stall.readlines()[1:]:
                    food = line.strip().split('\t')  # 'food' is a list [no., food, price]
                    position1 = (410, 130 + count * 18)
                    position2 = (670, 130 + count * 18)
                    position_heading = (430, 130 + count * 18)
                    if len(food) == 1:
                        self.heading = wx.StaticText(self, label=food[0], pos=position_heading)
                        self.heading.SetFont(self.font11bold)
                        even = 0
                    elif even % 2 != 0:
                        self.food_name = wx.StaticText(self, label=food[1], pos=position1)
                        self.price = wx.StaticText(self, label=food[2], pos=position2)
                        self.food_name.SetFont(self.font11)
                        self.price.SetFont(self.font11)
                        if count % 2 != 0:
                            self.food_name.SetForegroundColour("sea green")
                            self.price.SetForegroundColour("sea green")
                    else:
                        count -= 1
                    count += 1
                    even += 1


# -------------------------------- APP --------------------------------
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="NTU North Spine Canteen")
        self.frame.Show()
        return True


app = MyApp()
app.MainLoop()