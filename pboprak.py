# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Main_Frame
###########################################################################

class Main_Frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		Grid = wx.FlexGridSizer( 0, 1, 0, 0 )
		Grid.SetFlexibleDirection( wx.BOTH )
		Grid.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"HELLO WX", wx.Point( -1,-1 ), wx.Size( 500,40 ), wx.ALIGN_CENTRE )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 24, 74, 90, 90, False, "Arial" ) )
		self.m_staticText5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		
		Grid.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		Grid.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"Anung Firdauzy P", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_textCtrl1.SetFont( wx.Font( 9, 73, 90, 90, False, "Comic Sans MS" ) )
		
		Grid.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nim", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		Grid.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"192410101122", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_textCtrl2.SetFont( wx.Font( 9, 73, 90, 90, False, "Comic Sans MS" ) )
		
		Grid.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( Grid )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

