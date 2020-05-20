import wx
import json
import time
import wx.adv

format = "%A, %d/%m/%y, %H:%M"
realtime = time.strftime(format, time.localtime())
choice_hour = ['00', '01', '02', '03', '05', '06', '07', '08', '09', '10',
               '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
               '21', '22', '23']
choice_minute = []
for i in range(60):
    if i%5 == 0:
        if len(str(i))==1:
            choice_minute.append("0"+str(i))
        else:
            choice_minute.append(str(i))


# ---------------------------------------- FRAME ----------------------------------
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(800, 650))

        self.panel = MyPanel(self)
        self.today_panel = Today(self)
        self.anotherday_panel = AnotherDay(self)
        self.miniwok_a = MiniWok_A(self)
        self.miniwok_t = MiniWok_T(self)

        self.today_panel.Hide()
        self.anotherday_panel.Hide()
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.sizer.Add(self.today_panel, 1, wx.EXPAND)
        self.sizer.Add(self.anotherday_panel, 1, wx.EXPAND)
        self.sizer.Add(self.miniwok_a, 1, wx.EXPAND)
        self.sizer.Add(self.miniwok_t, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        # Create the icon for the app
        self.SetIcon(wx.Icon("images/icon.png", wx.BITMAP_TYPE_PNG))

    def OnClickToday(self, event):
        """ Go to Today panel after click on "View Today's Stores"."""
        self.panel.Hide()
        self.today_panel.Show()        #####
        self.anotherday_panel.Hide()
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()
        self.Layout()

    def OnClickAnother(self, event):
        """Go to Another panel after click on 'View stores by other dates'. """
        self.panel.Hide()
        self.today_panel.Hide()
        self.anotherday_panel.Show()   #####
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()
        self.Layout()

    def OnClickBack_Panel(self, event):
        """Go back to Today panel."""
        self.panel.Show()           #####
        self.today_panel.Hide()
        self.anotherday_panel.Hide()
        self.miniwok_a.Hide()
        self.miniwok_t.Hide()
        self.Layout()

    def OnClick_MiniWok_T(self, event):
        """Go to today's Mini Wok menu."""
        self.panel.Hide()
        self.today_panel.Hide()
        self.anotherday_panel.Hide()
        self.miniwok_a.Hide()      #####
        self.miniwok_t.Show()
        self.Layout()

    def OnClick_MiniWok_A(self, event):
        """Go to another day's Mini Wok menu."""
        with open("date_time.txt", 'w') as file_w:
            file_w.write(str(self.anotherday_panel.calendar.GetDate().Format(format)))
            print("Write successfully")
        self.panel.Hide()
        self.today_panel.Hide()
        self.anotherday_panel.Hide()
        self.miniwok_a.Show()      #####
        self.miniwok_t.Hide()
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
    def __init__(self, parent):
        super(Today, self).__init__(parent)

        # DISPLAY REAL-TIME
        realtime_text = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        realtime_text.SetFont(font20)

        # STORE BUTTONS
        # --- line 1
        self.MiniWok_btn = wx.Button(self, label="Mini Wok", pos=(50, 100), size=(120, 50))
        self.ChickenRice_btn = wx.Button(self, label="Chicken Rice", pos=(195, 100), size=(120, 50))
        self.HandmadeNoodles_btn = wx.Button(self, label="Hand-made \nNoodles", pos=(335, 100), size=(120, 50))
        self.MalayBBQ_btn = wx.Button(self, label="Malay BBQ", pos=(475, 100), size=(120, 50))
        self.VegetarianFood_btn = wx.Button(self, label="Vegetarian Food", pos=(615, 100), size=(120, 50))
        # --- line 2
        self.XianCuisine_btn = wx.Button(self, label="Xian Cuisine", pos=(50, 170), size=(120, 50))
        self.JapaneseKoreanDelight_btn = wx.Button(self, label="Japanese\nKorean Delight", pos=(195, 170), size=(120, 50))
        self.BBQDelight_btn = wx.Button(self, label="BBQ Delight", pos=(335, 170), size=(120, 50))
        self.VietnameseCuisine_btn = wx.Button(self, label="Vietnamese \nCuisine", pos=(475, 170), size=(120, 50))
        self.ItalianPasta_btn = wx.Button(self, label="Italian Pasta", pos=(615, 170), size=(120, 50))
        # ------ font -----
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
        self.Next_btn.Bind(wx.EVT_BUTTON, parent.OnClick_MiniWok_A)

        # CREATE CALENDAR TO PICK A DATE
        self.calendar = wx.adv.CalendarCtrl(self, pos=(230, 100), size=(300,200), style=wx.adv.CAL_SHOW_HOLIDAYS)

        # DISPLAY CHOSEN DATE
        # Display current date and time
        self.chosen_date_str = str(wx.DateTime.Format(wx.DateTime.UNow(),format))
        self.chosen_date = wx.StaticText(self, label=self.chosen_date_str, pos=(230,35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date.SetFont(font20)
        self.chosen_date.Bind(wx.adv.EVT_CALENDAR_SEL_CHANGED, self.DisplayTime)

        # ENTER HOUR AND MINUTE
        self.time_text = wx.StaticText(self, label="Time: ", pos=(230, 350))
        self.time_text.SetFont(font20)
        self.hour_input = wx.ComboBox(self, value='00', pos=(330,350), size=(45,50), choices=choice_hour, style=wx.CB_DROPDOWN)
        self.colon = wx.StaticText(self, label=":", pos=(380,350))
        self.minute_input = wx.ComboBox(self, value='00', pos=(400,350), size=(45,50), choices=choice_minute, style=wx.CB_DROPDOWN)
        font11_normal = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_NORMAL)
        self.hour_input.SetFont(font11_normal)
        self.minute_input.SetFont(font11_normal)
        self.colon.SetFont(font20)

    def DisplayTime(self, event):
        chosen_date_str = str(self.calendar.GetDate().Format(format))
        self.chosen_date.SetLabelText(chosen_date_str)


# ------------------------- STORE PANELS ------------------------------------
class MiniWok(wx.Panel):
    def __init__(self, parent):
        super(MiniWok, self).__init__(parent)

        stall_name = "Mini Wok"
        image_path = "images/miniwok.jpg"

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
        self.enter_space = wx.TextCtrl(self, pos=(180, 390), size=(50,25))
        self.enter_space.SetFont(font11)
        self.waiting_time_text = wx.StaticText(self, label="Waiting time: ", pos=(60, 430))
        self.waiting_time_text.SetFont(font11)
        self.waiting_time_result = wx.TextCtrl(self, pos=(180, 427), size=(50,25), style=wx.TE_READONLY)
        self.waiting_time_result.SetFont(font11)
        self.calculate_btn = wx.Button(self, label="Calculate", pos=(240, 387), size=(100, 30))
        font11bold = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.calculate_btn.SetFont(font11bold)
        self.calculate_btn.SetForegroundColour('white')
        self.calculate_btn.SetBackgroundColour('sea green')
        self.calculate_btn.Bind(wx.EVT_BUTTON, self.OnCalculate)
        minute = wx.StaticText(self, label="minute(s)", pos=(244,430))
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
        result = int(self.enter_space.GetValue())*self.waiting_time_value
        self.waiting_time_result.SetLabel(str(result))

class MiniWok_T(MiniWok):
    def __init__(self, parent):
        super(MiniWok_T, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickToday)

        # DISPLAY CURRENT DATE
        self.date = wx.StaticText(self, label=realtime, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.date.SetFont(font20)

class MiniWok_A(MiniWok):
    def __init__(self, parent):
        super(MiniWok_A, self).__init__(parent)

        # BACK BUTTON
        self.back_btn.Bind(wx.EVT_BUTTON, parent.OnClickAnother)
        # with open('date_time.txt', 'r') as file_w:

        # NEXT BUTTON
        with open('date_time.txt', 'r') as file_r:
            chosen_date = file_r.read()
        self.chosen_date = wx.StaticText(self, label=parent.chosen_date, pos=(230, 35))
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.chosen_date.SetFont(font20)


# ----------------------------------- APP -----------------------------
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="NTU North Spine Canteen")
        self.frame.Show()
        return True

app = MyApp()
app.MainLoop()