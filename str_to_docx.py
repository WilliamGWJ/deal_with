import win32com
from win32com.client import Dispath, constants


w = win32com.client.Dispatch('Word.Application')
w.Visiable = 1
w.DisplayAlerts = 0
doc = w.Documents.Add()
my