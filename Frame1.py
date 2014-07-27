#Boa:Frame:Frame1

import wx

import cs9000core

from wx.lib.anchors import LayoutAnchors

dictScreenToCArray=[]
dictScreenToPArray=[]

def create(parent):
    cs9000core.__init__()
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNLOADWIREFILE, wxID_FRAME1BTNRUNPROGRAM, 
 wxID_FRAME1BTNSAVEWIREFILE, wxID_FRAME1BTNSENDPROGRAM, wxID_FRAME1NOTEBOOK1, 
 wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, wxID_FRAME1PANEL3, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, 
 wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT14, 
 wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT16, wxID_FRAME1STATICTEXT17, 
 wxID_FRAME1STATICTEXT18, wxID_FRAME1STATICTEXT19, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, 
 wxID_FRAME1STATICTEXT9, wxID_FRAME1STATUSBAR1, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, 
 wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, wxID_FRAME1TXTCOUNT1, 
 wxID_FRAME1TXTCOUNT2, wxID_FRAME1TXTCUTACCEL, wxID_FRAME1TXTCUTCLEAR, 
 wxID_FRAME1TXTCUTSPEED, wxID_FRAME1TXTFEEDACCEL, wxID_FRAME1TXTFEEDSPEED, 
 wxID_FRAME1TXTLEFTCUT, wxID_FRAME1TXTLEFTGAP, wxID_FRAME1TXTLEFTINSBO, 
 wxID_FRAME1TXTLEFTINSCUT, wxID_FRAME1TXTLEFTSTRIP, wxID_FRAME1TXTMODE, 
 wxID_FRAME1TXTRIGHTGAP, wxID_FRAME1TXTRIGHTINSBO, wxID_FRAME1TXTRIGHTINSCUT, 
 wxID_FRAME1TXTRIGHTSTRIP, wxID_FRAME1TXTV50, wxID_FRAME1TXTV51, 
 wxID_FRAME1TXTV52, wxID_FRAME1TXTV53, wxID_FRAME1TXTV54, wxID_FRAME1TXTV55, 
 wxID_FRAME1TXTV56, wxID_FRAME1TXTV60, wxID_FRAME1TXTV63, wxID_FRAME1TXTV66, 
 wxID_FRAME1TXTV69, wxID_FRAME1TXTV6C, wxID_FRAME1TXTV6F, wxID_FRAME1TXTV72, 
 wxID_FRAME1TXTV75, wxID_FRAME1TXTV78, wxID_FRAME1TXTV7B, wxID_FRAME1TXTV7E, 
 wxID_FRAME1TXTV81, wxID_FRAME1TXTV84, wxID_FRAME1TXTV87, wxID_FRAME1TXTV8A, 
 wxID_FRAME1TXTV8D, wxID_FRAME1TXTV90, wxID_FRAME1TXTV93, wxID_FRAME1TXTV96, 
 wxID_FRAME1TXTV99, wxID_FRAME1TXTV9C, wxID_FRAME1TXTWIRELENGTH, 
] = [wx.NewId() for _init_ctrls in range(81)]

[wxID_FRAME1MENUFILEFILECLOSE, wxID_FRAME1MENUFILEFILEEXIT, 
 wxID_FRAME1MENUFILEFILEOPEN, wxID_FRAME1MENUFILEFILESAVE, 
 wxID_FRAME1MENUFILEFILESAVEAS, 
] = [wx.NewId() for _init_coll_menuFile_Items in range(5)]

[wxID_FRAME1MENUHELPABOUT] = [wx.NewId() for _init_coll_menuHelp_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'File')
        parent.Append(menu=self.menuHelp, title=u'Help')

    def _init_coll_menuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Display general information',
              id=wxID_FRAME1MENUHELPABOUT, kind=wx.ITEM_NORMAL, text=u'About')
        self.Bind(wx.EVT_MENU, self.OnMenuHelpAboutMenu,
              id=wxID_FRAME1MENUHELPABOUT)

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Open file', id=wxID_FRAME1MENUFILEFILEOPEN,
              kind=wx.ITEM_NORMAL, text=u'Open')
        parent.Append(help=u'Save file', id=wxID_FRAME1MENUFILEFILESAVE,
              kind=wx.ITEM_NORMAL, text=u'Save')
        parent.Append(help=u'Save File with new name',
              id=wxID_FRAME1MENUFILEFILESAVEAS, kind=wx.ITEM_NORMAL,
              text=u'Save As')
        parent.Append(help=u'Close file', id=wxID_FRAME1MENUFILEFILECLOSE,
              kind=wx.ITEM_NORMAL, text=u'Close')
        parent.Append(help=u'Exit application', id=wxID_FRAME1MENUFILEFILEEXIT,
              kind=wx.ITEM_NORMAL, text=u'Exit')
        self.Bind(wx.EVT_MENU, self.OnMenuFileFileexitMenu,
              id=wxID_FRAME1MENUFILEFILEEXIT)
        self.Bind(wx.EVT_MENU, self.OnMenuFileFilecloseMenu,
              id=wxID_FRAME1MENUFILEFILECLOSE)
        self.Bind(wx.EVT_MENU, self.OnMenuFileFileopenMenu,
              id=wxID_FRAME1MENUFILEFILEOPEN)
        self.Bind(wx.EVT_MENU, self.OnMenuFileFilesaveMenu,
              id=wxID_FRAME1MENUFILEFILESAVE)
        self.Bind(wx.EVT_MENU, self.OnMenuFileFilesaveasMenu,
              id=wxID_FRAME1MENUFILEFILESAVEAS)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=True,
              text=u'Pages0')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text=u'Pages1')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text='Pages2')

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'status')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.menuFile = wx.Menu(title=u'File')

        self.menuHelp = wx.Menu(title=u'Help')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuHelp_Items(self.menuHelp)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(555, 154), size=wx.Size(618, 514),
              style=wx.DEFAULT_FRAME_STYLE, title=u'CS9000')
        self._init_utils()
        self.SetClientSize(wx.Size(610, 487))
        self.SetMenuBar(self.menuBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(610, 448), style=0)
        self.notebook1.SetConstraints(LayoutAnchors(self.notebook1, True, True,
              False, False))
        self.notebook1.SetAutoLayout(True)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(602, 422),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(602, 422),
              style=wx.TAB_TRAVERSAL)

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(602, 422),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel3, pos=wx.Point(16, 16), size=wx.Size(56, 21),
              style=0, value='textCtrl1')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel3, pos=wx.Point(16, 48), size=wx.Size(56, 21),
              style=0, value='textCtrl2')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel3, pos=wx.Point(16, 80), size=wx.Size(56, 21),
              style=0, value='textCtrl3')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self.panel3, pos=wx.Point(16, 112), size=wx.Size(56, 21),
              style=0, value='textCtrl4')

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self.panel3, pos=wx.Point(16, 152), size=wx.Size(56, 21),
              style=0, value='textCtrl5')

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self.panel3, pos=wx.Point(16, 192), size=wx.Size(56, 21),
              style=0, value='textCtrl6')

        self.txtv60 = wx.TextCtrl(id=wxID_FRAME1TXTV60, name=u'txtv60',
              parent=self.panel2, pos=wx.Point(80, 160), size=wx.Size(96, 21),
              style=wx.TE_RIGHT, value=u'txtv60')
        self.txtv60.SetToolTipString(u'$60')

        self.txtv63 = wx.TextCtrl(id=wxID_FRAME1TXTV63, name=u'txtv63',
              parent=self.panel2, pos=wx.Point(80, 192), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv63')
        self.txtv63.SetToolTipString(u'textCtrl7')

        self.txtv66 = wx.TextCtrl(id=wxID_FRAME1TXTV66, name=u'txtv66',
              parent=self.panel2, pos=wx.Point(80, 224), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv66')

        self.txtv69 = wx.TextCtrl(id=wxID_FRAME1TXTV69, name=u'txtv69',
              parent=self.panel2, pos=wx.Point(80, 256), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv69')

        self.txtv6c = wx.TextCtrl(id=wxID_FRAME1TXTV6C, name=u'txtv6c',
              parent=self.panel2, pos=wx.Point(80, 288), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv6c')

        self.txtv6f = wx.TextCtrl(id=wxID_FRAME1TXTV6F, name=u'txtv6f',
              parent=self.panel2, pos=wx.Point(80, 320), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv6f')

        self.txtv72 = wx.TextCtrl(id=wxID_FRAME1TXTV72, name=u'txtv72',
              parent=self.panel2, pos=wx.Point(80, 352), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv72')

        self.txtv75 = wx.TextCtrl(id=wxID_FRAME1TXTV75, name=u'txtv75',
              parent=self.panel2, pos=wx.Point(264, 160), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv75')

        self.txtv78 = wx.TextCtrl(id=wxID_FRAME1TXTV78, name=u'txtv78',
              parent=self.panel2, pos=wx.Point(264, 192), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv78')

        self.txtv7b = wx.TextCtrl(id=wxID_FRAME1TXTV7B, name=u'txtv7b',
              parent=self.panel2, pos=wx.Point(264, 224), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv7b')

        self.txtv7e = wx.TextCtrl(id=wxID_FRAME1TXTV7E, name=u'txtv7e',
              parent=self.panel2, pos=wx.Point(264, 256), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv7e')

        self.txtv81 = wx.TextCtrl(id=wxID_FRAME1TXTV81, name=u'txtv81',
              parent=self.panel2, pos=wx.Point(264, 288), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv81')

        self.txtv84 = wx.TextCtrl(id=wxID_FRAME1TXTV84, name=u'txtv84',
              parent=self.panel2, pos=wx.Point(264, 320), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv84')

        self.txtv87 = wx.TextCtrl(id=wxID_FRAME1TXTV87, name=u'txtv87',
              parent=self.panel2, pos=wx.Point(264, 352), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv87')

        self.txtv8a = wx.TextCtrl(id=wxID_FRAME1TXTV8A, name=u'txtv8a',
              parent=self.panel2, pos=wx.Point(488, 160), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv8a')

        self.txtv8d = wx.TextCtrl(id=wxID_FRAME1TXTV8D, name=u'txtv8d',
              parent=self.panel2, pos=wx.Point(488, 192), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv8d')

        self.txtv90 = wx.TextCtrl(id=wxID_FRAME1TXTV90, name=u'txtv90',
              parent=self.panel2, pos=wx.Point(488, 224), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv90')

        self.txtv93 = wx.TextCtrl(id=wxID_FRAME1TXTV93, name=u'txtv93',
              parent=self.panel2, pos=wx.Point(488, 256), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv93')

        self.txtv96 = wx.TextCtrl(id=wxID_FRAME1TXTV96, name=u'txtv96',
              parent=self.panel2, pos=wx.Point(488, 288), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv96')

        self.txtv99 = wx.TextCtrl(id=wxID_FRAME1TXTV99, name=u'txtv99',
              parent=self.panel2, pos=wx.Point(488, 320), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv99')

        self.txtv9c = wx.TextCtrl(id=wxID_FRAME1TXTV9C, name=u'txtv9c',
              parent=self.panel2, pos=wx.Point(488, 352), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv9c')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Cutter clear', name='staticText1', parent=self.panel2,
              pos=wx.Point(16, 168), size=wx.Size(57, 13), style=0)

        self.txtv50 = wx.TextCtrl(id=wxID_FRAME1TXTV50, name=u'txtv50',
              parent=self.panel2, pos=wx.Point(80, 16), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv50')

        self.txtv51 = wx.TextCtrl(id=wxID_FRAME1TXTV51, name=u'txtv51',
              parent=self.panel2, pos=wx.Point(80, 40), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv51')

        self.txtv52 = wx.TextCtrl(id=wxID_FRAME1TXTV52, name=u'txtv52',
              parent=self.panel2, pos=wx.Point(80, 64), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv52')

        self.txtv53 = wx.TextCtrl(id=wxID_FRAME1TXTV53, name=u'txtv53',
              parent=self.panel2, pos=wx.Point(80, 88), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv53')

        self.txtv54 = wx.TextCtrl(id=wxID_FRAME1TXTV54, name=u'txtv54',
              parent=self.panel2, pos=wx.Point(312, 16), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv54')

        self.txtv55 = wx.TextCtrl(id=wxID_FRAME1TXTV55, name=u'txtv55',
              parent=self.panel2, pos=wx.Point(312, 40), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv55')

        self.txtv56 = wx.TextCtrl(id=wxID_FRAME1TXTV56, name=u'txtv56',
              parent=self.panel2, pos=wx.Point(312, 64), size=wx.Size(100, 21),
              style=wx.TE_RIGHT, value=u'txtv56')

        self.btnSendProgram = wx.Button(id=wxID_FRAME1BTNSENDPROGRAM,
              label=u'SendProgram', name=u'btnSendProgram', parent=self.panel2,
              pos=wx.Point(80, 384), size=wx.Size(88, 23), style=0)
        self.btnSendProgram.Bind(wx.EVT_BUTTON, self.OnBtnSendProgramButton,
              id=wxID_FRAME1BTNSENDPROGRAM)

        self.btnRunProgram = wx.Button(id=wxID_FRAME1BTNRUNPROGRAM,
              label=u'RunProgram', name=u'btnRunProgram', parent=self.panel2,
              pos=wx.Point(208, 384), size=wx.Size(75, 23), style=0)
        self.btnRunProgram.Bind(wx.EVT_BUTTON, self.OnBtnRunProgramButton,
              id=wxID_FRAME1BTNRUNPROGRAM)

        self.txtCount2 = wx.TextCtrl(id=wxID_FRAME1TXTCOUNT2, name=u'txtCount2',
              parent=self.panel1, pos=wx.Point(80, 40), size=wx.Size(72, 21),
              style=0, value=u'txtCount2')

        self.txtWireLength = wx.TextCtrl(id=wxID_FRAME1TXTWIRELENGTH,
              name=u'txtWireLength', parent=self.panel1, pos=wx.Point(224, 96),
              size=wx.Size(68, 21), style=0, value=u'txtWireLength')

        self.txtLeftStrip = wx.TextCtrl(id=wxID_FRAME1TXTLEFTSTRIP,
              name=u'txtLeftStrip', parent=self.panel1, pos=wx.Point(24, 136),
              size=wx.Size(72, 21), style=0, value=u'txtLeftStrip')

        self.txtLeftGap = wx.TextCtrl(id=wxID_FRAME1TXTLEFTGAP,
              name=u'txtLeftGap', parent=self.panel1, pos=wx.Point(112, 96),
              size=wx.Size(64, 21), style=0, value=u'txtLeftGap')

        self.txtRightGap = wx.TextCtrl(id=wxID_FRAME1TXTRIGHTGAP,
              name=u'txtRightGap', parent=self.panel1, pos=wx.Point(352, 96),
              size=wx.Size(64, 21), style=0, value=u'txtRightGap')

        self.txtRightStrip = wx.TextCtrl(id=wxID_FRAME1TXTRIGHTSTRIP,
              name=u'txtRightStrip', parent=self.panel1, pos=wx.Point(416, 136),
              size=wx.Size(80, 21), style=0, value=u'txtRightStrip')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Count2', name='staticText2', parent=self.panel1,
              pos=wx.Point(40, 48), size=wx.Size(35, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Wire Length', name='staticText3', parent=self.panel1,
              pos=wx.Point(232, 80), size=wx.Size(58, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Left Strip', name='staticText4', parent=self.panel1,
              pos=wx.Point(32, 120), size=wx.Size(44, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Left Gap', name='staticText5', parent=self.panel1,
              pos=wx.Point(120, 80), size=wx.Size(41, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Right Gap', name='staticText6', parent=self.panel1,
              pos=wx.Point(360, 80), size=wx.Size(47, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Right Strip', name='staticText7', parent=self.panel1,
              pos=wx.Point(424, 120), size=wx.Size(50, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Mode', name='staticText8', parent=self.panel1,
              pos=wx.Point(56, 304), size=wx.Size(32, 16), style=0)

        self.txtMode = wx.TextCtrl(id=wxID_FRAME1TXTMODE, name=u'txtMode',
              parent=self.panel1, pos=wx.Point(96, 304), size=wx.Size(56, 21),
              style=0, value=u'txtMode')

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Cutter Speed', name='staticText9', parent=self.panel1,
              pos=wx.Point(184, 352), size=wx.Size(64, 13), style=0)

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Cutter Accel', name='staticText10', parent=self.panel1,
              pos=wx.Point(184, 384), size=wx.Size(59, 13), style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Feed Speed', name='staticText11', parent=self.panel1,
              pos=wx.Point(32, 349), size=wx.Size(57, 13), style=0)

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'Feed Accel', name='staticText12', parent=self.panel1,
              pos=wx.Point(40, 384), size=wx.Size(52, 13), style=0)

        self.txtCutSpeed = wx.TextCtrl(id=wxID_FRAME1TXTCUTSPEED,
              name=u'txtCutSpeed', parent=self.panel1, pos=wx.Point(248, 344),
              size=wx.Size(56, 21), style=0, value=u'txtCutSpeed')

        self.txtCutAccel = wx.TextCtrl(id=wxID_FRAME1TXTCUTACCEL,
              name=u'txtCutAccel', parent=self.panel1, pos=wx.Point(248, 376),
              size=wx.Size(56, 21), style=0, value=u'txtCutAccel')

        self.txtFeedSpeed = wx.TextCtrl(id=wxID_FRAME1TXTFEEDSPEED,
              name=u'txtFeedSpeed', parent=self.panel1, pos=wx.Point(96, 344),
              size=wx.Size(56, 21), style=0, value=u'txtFeedSpeed')

        self.txtFeedAccel = wx.TextCtrl(id=wxID_FRAME1TXTFEEDACCEL,
              name=u'txtFeedAccel', parent=self.panel1, pos=wx.Point(96, 376),
              size=wx.Size(56, 21), style=0, value=u'txtFeedAccel')

        self.txtLeftInsCut = wx.TextCtrl(id=wxID_FRAME1TXTLEFTINSCUT,
              name=u'txtLeftInsCut', parent=self.panel1, pos=wx.Point(152, 184),
              size=wx.Size(56, 21), style=0, value=u'txtLeftInsCut')

        self.txtLeftInsBO = wx.TextCtrl(id=wxID_FRAME1TXTLEFTINSBO,
              name=u'txtLeftInsBO', parent=self.panel1, pos=wx.Point(152, 216),
              size=wx.Size(56, 21), style=0, value=u'txtLeftInsBO')

        self.txtRightInsCut = wx.TextCtrl(id=wxID_FRAME1TXTRIGHTINSCUT,
              name=u'txtRightInsCut', parent=self.panel1, pos=wx.Point(320,
              184), size=wx.Size(60, 21), style=0, value=u'txtRightInsCut')

        self.txtRightInsBO = wx.TextCtrl(id=wxID_FRAME1TXTRIGHTINSBO,
              name=u'txtRightInsBO', parent=self.panel1, pos=wx.Point(320, 216),
              size=wx.Size(56, 21), style=0, value=u'txtRightInsBO')

        self.txtLeftCut = wx.TextCtrl(id=wxID_FRAME1TXTLEFTCUT,
              name=u'txtLeftCut', parent=self.panel1, pos=wx.Point(32, 184),
              size=wx.Size(60, 21), style=0, value=u'txtLeftCut')

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'Wire Cut', name='staticText13', parent=self.panel1,
              pos=wx.Point(40, 168), size=wx.Size(42, 13), style=0)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label=u'Left Ins Cut', name='staticText14', parent=self.panel1,
              pos=wx.Point(152, 168), size=wx.Size(57, 13), style=0)

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label=u'Left Ins BO', name='staticText15', parent=self.panel1,
              pos=wx.Point(152, 240), size=wx.Size(54, 13), style=0)

        self.staticText16 = wx.StaticText(id=wxID_FRAME1STATICTEXT16,
              label=u'Right Ins Cut', name='staticText16', parent=self.panel1,
              pos=wx.Point(320, 168), size=wx.Size(63, 13), style=0)

        self.staticText17 = wx.StaticText(id=wxID_FRAME1STATICTEXT17,
              label=u'Right Ins BO', name='staticText17', parent=self.panel1,
              pos=wx.Point(320, 240), size=wx.Size(60, 13), style=0)

        self.btnLoadWireFile = wx.Button(id=wxID_FRAME1BTNLOADWIREFILE,
              label=u'Load', name=u'btnLoadWireFile', parent=self.panel1,
              pos=wx.Point(416, 328), size=wx.Size(75, 23), style=0)
        self.btnLoadWireFile.Bind(wx.EVT_BUTTON, self.OnBtnLoadWireFileButton,
              id=wxID_FRAME1BTNLOADWIREFILE)

        self.btnSaveWireFile = wx.Button(id=wxID_FRAME1BTNSAVEWIREFILE,
              label=u'Save', name=u'btnSaveWireFile', parent=self.panel1,
              pos=wx.Point(416, 376), size=wx.Size(75, 23), style=0)
        self.btnSaveWireFile.Bind(wx.EVT_BUTTON, self.OnBtnSaveWireFileButton,
              id=wxID_FRAME1BTNSAVEWIREFILE)

        self.txtCutClear = wx.TextCtrl(id=wxID_FRAME1TXTCUTCLEAR,
              name=u'txtCutClear', parent=self.panel1, pos=wx.Point(32, 216),
              size=wx.Size(56, 21), style=0, value=u'txtCutClear')

        self.staticText18 = wx.StaticText(id=wxID_FRAME1STATICTEXT18,
              label=u'Cutter Clear', name='staticText18', parent=self.panel1,
              pos=wx.Point(32, 240), size=wx.Size(59, 13), style=0)

        self.txtCount1 = wx.TextCtrl(id=wxID_FRAME1TXTCOUNT1, name=u'txtCount1',
              parent=self.panel1, pos=wx.Point(80, 16), size=wx.Size(72, 21),
              style=0, value=u'txtCount1')

        self.staticText19 = wx.StaticText(id=wxID_FRAME1STATICTEXT19,
              label=u'Count1', name='staticText19', parent=self.panel1,
              pos=wx.Point(40, 24), size=wx.Size(35, 13), style=0)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        dictScreenToCArray.extend([(self.txtv50,0),(self.txtv51,1),(self.txtv52,2),(self.txtv53,3),\
                              (self.txtv54,4),(self.txtv55,5),(self.txtv56,6)])
        dictScreenToPArray.extend([(self.txtv60,0),(self.txtv63,1),(self.txtv66,2),(self.txtv69,3),\
                              (self.txtv6c,4),(self.txtv6f,5),(self.txtv72,6),(self.txtv75,7),\
                              (self.txtv78,8),(self.txtv7b,9),(self.txtv7e,10),(self.txtv81,11),\
                              (self.txtv84,12),(self.txtv87,13),(self.txtv8a,14),(self.txtv8d,15),\
                              (self.txtv90,16),(self.txtv93,17),(self.txtv96,18),(self.txtv99,19),\
                              (self.txtv9c,20)])

    def OnMenuFileFileexitMenu(self, event):
        self.Close()
        event.Skip()

    def OnMenuFileFilecloseMenu(self, event):
        event.Skip()

    def OnMenuFileFileopenMenu(self, event):
        dlg = wx.FileDialog(self, 'Choose a file', '.', '', '*.*', wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                #gInputFname=filename
                cs9000core.ReadArraysFromFile(filename)
                Frame1.UpdateScreenArrays(self)
        finally:
            dlg.Destroy()

    def OnMenuFileFilesaveMenu(self, event):
        #gInputFname=filename
        Frame1.UpdateInternalArrays(self)
        cs9000core.WriteArraysToFile("")

    def OnMenuFileFilesaveasMenu(self, event):
        dlg = wx.FileDialog(self, 'Choose a file', '.', '', '*.*', wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                #gInputFname=filename
                Frame1.UpdateInternalArrays(self)
                cs9000core.WriteArraysToFile(filename)
        finally:
            dlg.Destroy()

    def OnMenuHelpAboutMenu(self, event):
        cs9000core.Ocommand()
        cs9000core.Dcommand()
        #event.Skip()


    def UpdateScreenArrays(self):
        """
        dictScreenToCArray = [(self.txtv50,0),(self.txtv51,1),(self.txtv52,2),(self.txtv53,3),\
                              (self.txtv54,4),(self.txtv55,5),(self.txtv56,6)]
        dictScreenToPArray = [(self.txtv60,0),(self.txtv63,1),(self.txtv66,2),(self.txtv69,3),\
                              (self.txtv6c,4),(self.txtv6f,5),(self.txtv72,6),(self.txtv75,7),\
                              (self.txtv78,8),(self.txtv7b,9),(self.txtv7e,10),(self.txtv81,11),\
                              (self.txtv84,12),(self.txtv87,13),(self.txtv8a,14),(self.txtv8d,15),\
                              (self.txtv90,16),(self.txtv93,17),(self.txtv96,18),(self.txtv99,19),\
                              (self.txtv9c,20)]
        """
        #self.txtv50.ChangeValue(str(cs9000core.gControlArray[0]))
        for val in dictScreenToCArray:
            val[0].ChangeValue(str(cs9000core.gControlArray[val[1]]))

        #self.txtv60.ChangeValue(str(cs9000core.gPositionArray[0]))
        for val in dictScreenToPArray:
            val[0].ChangeValue(str(cs9000core.gPositionArray[val[1]]))

    def UpdateInternalArrays(self):
        """
        dictScreenToCArray = [(self.txtv50,0),(self.txtv51,1),(self.txtv52,2),(self.txtv53,3),\
                              (self.txtv54,4),(self.txtv55,5),(self.txtv56,6)]
        dictScreenToPArray = [(self.txtv60,0),(self.txtv63,1),(self.txtv66,2),(self.txtv69,3),\
                              (self.txtv6c,4),(self.txtv6f,5),(self.txtv72,6),(self.txtv75,7),\
                              (self.txtv78,8),(self.txtv7b,9),(self.txtv7e,10),(self.txtv81,11),\
                              (self.txtv84,12),(self.txtv87,13),(self.txtv8a,14),(self.txtv8d,15),\
                              (self.txtv90,16),(self.txtv93,17),(self.txtv96,18),(self.txtv99,19),\
                              (self.txtv9c,20)]
        """
        for val in dictScreenToCArray:
            cs9000core.gControlArray[val[1]]=int(val[0].GetValue)
        for val in dictScreenToPArray:
            cs9000core.gPositionArray[val[1]]=int(val[0].GetValue)

    def OnBtnSendProgramButton(self, event):
        cs9000core.Ocommand()
        cs9000core.Dcommand()
        #event.Skip()

    def OnBtnRunProgramButton(self, event):
        cs9000core.Pcommand()
        #event.Skip()




    def UpdateArrayFromWireDiagram(self):
        """
        self.txtCount.ChangeValue(str(cs9000core.gPositionArray[12]))   #txtv84 87
        self.txtWireLength.ChangeValue(str(
        self.txtLeftStrip.ChangeValue(str(
        self.txtLeftGap.ChangeValue(str(
        self.txtRightGap.ChangeValue(str(
        self.txtRightStrip.ChangeValue(str(
        self.txtMode.ChangeValue(str(cs9000core.gControlArray[5]))      #txtv55
        self.txtCutSpeed.ChangeValue(str(cs9000core.gControlArray[0]))  #txtv50
        self.txtCutAccel.ChangeValue(str(cs9000core.gControlArray[1]))  #txtv51
        self.txtFeedSpeed.ChangeValue(str(cs9000core.gControlArray[2])) #txtv52
        self.txtFeedAccel.ChangeValue(str(cs9000core.gControlArray[3])) #txtv53

        cs9000core.gControlArray[0]=int(self.txtv50.GetValue)
        cs9000core.gControlArray[1]=int(self.txtv51.GetValue)
        cs9000core.gControlArray[2]=int(self.txtv52.GetValue)
        cs9000core.gControlArray[3]=int(self.txtv53.GetValue)
        cs9000core.gControlArray[4]=int(self.txtv54.GetValue)
        cs9000core.gControlArray[5]=int(self.txtv55.GetValue)
        cs9000core.gControlArray[6]=int(self.txtv56.GetValue)
        
        scale = 1.0/cs9000core.STEPSPERINCH
        
        dictCArrayToWireDiag = []
        dictCArrayToWireDiag.append((self.txtMode.ChangeValue,self.txtv55.GetValue))
        
        for val in dictCArrayToWireDiag:
            val[0]=val[1]()
            
                                self.txtCutSpeed.ChangeValue : self.txtv50.GetValue,\
                                self.txtCutAccel.ChangeValue : self.txtv54.GetValue,\
                                self.txtFeedSpeed.ChangeValue : self.txtv52.GetValue,\
                                self.txtFeedAccel.ChangeValue : self.txtv53.GetValue,\
                                self.txtCutAccel.ChangeValue : str(scale*int(self.txtv60.GetValue)),\
                                self.txtCount.ChangeValue : self.txtv84.GetValue,\
                                self.txtWireLength.ChangeValue : str(scale*int(self.txtv75.GetValue)),\
                                self.txtLeftStrip.ChangeValue : ,\
                                self.txtLeftGap.ChangeValue : ,\
                                self.txtRightGap.ChangeValue : ,\
                                self.txtRightStrip.ChangeValue : ,\
                                }
        
            for key, value in dictCArrayToWireDiag:
                key(value)
        
        cs9000core.STEPSPERINCH
        """
        #txtCountyo
        

    def UpdateArraysToWireDiagram(self):
        #dictCArrayToWireDiag = {0:self.txtCutSpeed.ChangeValue
        """
        self.txtMode.ChangeValue(str(cs9000core.gControlArray[5]))      #txtv55
        self.txtCutSpeed.ChangeValue(str(cs9000core.gControlArray[0]))  #txtv50
        self.txtCutAccel.ChangeValue(str(cs9000core.gControlArray[1]))  #txtv51
        self.txtFeedSpeed.ChangeValue(str(cs9000core.gControlArray[2])) #txtv52
        self.txtFeedAccel.ChangeValue(str(cs9000core.gControlArray[3])) #txtv53
        scale = 1.0/cs9000core.STEPSPERINCH
        self.txtCutAccel.ChangeValue(str(scale*cs9000core.gPositionArray[0]))  #txtv51
        cs9000core.STEPSPERINCH
        self.txtCount.ChangeValue(str(cs9000core.gPositionArray[12]))   #txtv84
        self.txtWireLength.ChangeValue(str(scale*cs9000core.gPositionArray[7])) #txtv75
        self.txtLeftStrip.ChangeValue(str(
        self.txtLeftGap.ChangeValue(str(
        self.txtRightGap.ChangeValue(str(
        self.txtRightStrip.ChangeValue(str(
        """
        #txtCount

    def OnBtnLoadWireFileButton(self, event):
        event.Skip()

    def OnBtnSaveWireFileButton(self, event):
        event.Skip()
        
        
"""
[60]= cutter clear (25)
[63] = right wire end insulation cut
[69] = right wire end back off cutter
[66] = left wire end insulation cut	(269)
[6C] = left wire end back off cutter (264)
[6F] = RS
[72] = (RS - RG)
[75] = WL = total_wire_length
[78] = (WL - LS)
[7B] = (WL - LS) + LG
[84] = counter1
[87] = counter2
[8A] = 0
[8D] = 0
[99] = cut wire (360)
"""

"""    
        self.txtv50.ChangeValue(str(cs9000core.gControlArray[0]))
        self.txtv51.ChangeValue(str(cs9000core.gControlArray[1]))
        self.txtv52.ChangeValue(str(cs9000core.gControlArray[2]))
        self.txtv53.ChangeValue(str(cs9000core.gControlArray[3]))
        self.txtv54.ChangeValue(str(cs9000core.gControlArray[4]))
        self.txtv55.ChangeValue(str(cs9000core.gControlArray[5]))
        self.txtv56.ChangeValue(str(cs9000core.gControlArray[6]))
        self.txtv60.ChangeValue(str(cs9000core.gPositionArray[0]))
        self.txtv63.ChangeValue(str(cs9000core.gPositionArray[1]))
        self.txtv66.ChangeValue(str(cs9000core.gPositionArray[2]))
        self.txtv69.ChangeValue(str(cs9000core.gPositionArray[3]))
        self.txtv6c.ChangeValue(str(cs9000core.gPositionArray[4]))
        self.txtv6f.ChangeValue(str(cs9000core.gPositionArray[5]))
        self.txtv72.ChangeValue(str(cs9000core.gPositionArray[6]))
        self.txtv75.ChangeValue(str(cs9000core.gPositionArray[7]))
        self.txtv78.ChangeValue(str(cs9000core.gPositionArray[8]))
        self.txtv7b.ChangeValue(str(cs9000core.gPositionArray[9]))
        self.txtv7e.ChangeValue(str(cs9000core.gPositionArray[10]))
        self.txtv81.ChangeValue(str(cs9000core.gPositionArray[11]))
        self.txtv84.ChangeValue(str(cs9000core.gPositionArray[12]))
        self.txtv87.ChangeValue(str(cs9000core.gPositionArray[13]))
        self.txtv8a.ChangeValue(str(cs9000core.gPositionArray[14]))
        self.txtv8d.ChangeValue(str(cs9000core.gPositionArray[15]))
        self.txtv90.ChangeValue(str(cs9000core.gPositionArray[16]))
        self.txtv93.ChangeValue(str(cs9000core.gPositionArray[17]))
        self.txtv96.ChangeValue(str(cs9000core.gPositionArray[18]))
        self.txtv99.ChangeValue(str(cs9000core.gPositionArray[19]))
        self.txtv9c.ChangeValue(str(cs9000core.gPositionArray[20]))
"""
        
"""
        #control array
        cs9000core.gControlArray[0]=int(self.txtv50.GetValue)
        cs9000core.gControlArray[1]=int(self.txtv51.GetValue)
        cs9000core.gControlArray[2]=int(self.txtv52.GetValue)
        cs9000core.gControlArray[3]=int(self.txtv53.GetValue)
        cs9000core.gControlArray[4]=int(self.txtv54.GetValue)
        cs9000core.gControlArray[5]=int(self.txtv55.GetValue)
        cs9000core.gControlArray[6]=int(self.txtv56.GetValue)
        #position array
        cs9000core.gPositionArray[0]=int(self.txtv60.GetValue)
        cs9000core.gPositionArray[1]=int(self.txtv63.GetValue)
        cs9000core.gPositionArray[2]=int(self.txtv66.GetValue)
        cs9000core.gPositionArray[3]=int(self.txtv69.GetValue)
        cs9000core.gPositionArray[4]=int(self.txtv6c.GetValue)
        cs9000core.gPositionArray[5]=int(self.txtv6f.GetValue)
        cs9000core.gPositionArray[6]=int(self.txtv72.GetValue)
        cs9000core.gPositionArray[7]=int(self.txtv75.GetValue)
        cs9000core.gPositionArray[8]=int(self.txtv78.GetValue)
        cs9000core.gPositionArray[9]=int(self.txtv7b.GetValue)
        cs9000core.gPositionArray[10]=int(self.txtv7e.GetValue)
        cs9000core.gPositionArray[11]=int(self.txtv81.GetValue)
        cs9000core.gPositionArray[12]=int(self.txtv84.GetValue)
        cs9000core.gPositionArray[13]=int(self.txtv87.GetValue)
        cs9000core.gPositionArray[14]=int(self.txtv8a.GetValue)
        cs9000core.gPositionArray[15]=int(self.txtv8d.GetValue)
        cs9000core.gPositionArray[16]=int(self.txtv90.GetValue)
        cs9000core.gPositionArray[17]=int(self.txtv93.GetValue)
        cs9000core.gPositionArray[18]=int(self.txtv96.GetValue)
        cs9000core.gPositionArray[19]=int(self.txtv99.GetValue)
        cs9000core.gPositionArray[20]=int(self.txtv9c.GetValue)
"""
        
        
