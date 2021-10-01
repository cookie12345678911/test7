import PyPDF2
class FloatObject(PyPDF2.generic.FloatObject):
    def __add__(self, other):
        return self.as_numeric() + other
    def __radd__(self, other):
        return self.as_numeric() + other
    def __sub__(self, other):
        return self.as_numeric() - other
    def __rsub__(self, other):
        return -self.as_numeric() + other
PyPDF2.generic.FloatObject = FloatObject

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pdfformfiller import PdfFormFiller

def addPage(infile, outfile):
    # Linuxでは、'/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf'など
    pdfmetrics.registerFont(TTFont('IPAexGothic', 'usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf'))
    sty = ParagraphStyle('sty', alignment=TA_CENTER, fontName='IPAexGothic', fontSize=9)
    ff = PdfFormFiller(infile)
    for i in range(ff.pdf.getNumPages()):
        p = ff.pdf.getPage(i)
        ff.add_text('ページ %d'%(i+1), i, (0,p.mediaBox[3]-30), p.mediaBox.getUpperRight(), sty)
    ff.write(outfile)

addPage("./test.pdf","./test2.pdf")
