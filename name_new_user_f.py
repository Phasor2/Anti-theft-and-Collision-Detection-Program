from PyQt5 import QtWidgets
from name_a_new_user import Ui_name_a_new_user

class name_a_new_userwindow(QtWidgets.QMainWindow,Ui_name_a_new_user):
    def comparecode(self):
        pass

    def backspacecode(self):
        self.lineEdit.backspace()

    def appendcode(self,n):
        self.lineEdit.insert(str(n))


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Button instantiation
        self.b1.clicked.connect(lambda: self.appendcode(1))
        self.b2.clicked.connect(lambda: self.appendcode(2))
        self.b3.clicked.connect(lambda: self.appendcode(3))
        self.b4.clicked.connect(lambda: self.appendcode(4))
        self.b5.clicked.connect(lambda: self.appendcode(5))
        self.b6.clicked.connect(lambda: self.appendcode(6))
        self.b7.clicked.connect(lambda: self.appendcode(7))
        self.b8.clicked.connect(lambda: self.appendcode(8))
        self.b9.clicked.connect(lambda: self.appendcode(9))
        self.b0.clicked.connect(lambda: self.appendcode(0))

        self.bq.clicked.connect(lambda: self.appendcode(q))
        self.bw.clicked.connect(lambda: self.appendcode(w))
        self.be.clicked.connect(lambda: self.appendcode(e))
        self.br.clicked.connect(lambda: self.appendcode(r))
        self.bt.clicked.connect(lambda: self.appendcode(t))
        self.by.clicked.connect(lambda: self.appendcode(y))
        self.bu.clicked.connect(lambda: self.appendcode(u))
        self.bi.clicked.connect(lambda: self.appendcode(i))
        self.bo.clicked.connect(lambda: self.appendcode(o))
        self.bp.clicked.connect(lambda: self.appendcode(p))
        self.ba.clicked.connect(lambda: self.appendcode(a))
        self.bs.clicked.connect(lambda: self.appendcode(s))
        self.bd.clicked.connect(lambda: self.appendcode(d))
        self.bf.clicked.connect(lambda: self.appendcode(f))
        self.bg.clicked.connect(lambda: self.appendcode(g))
        self.bh.clicked.connect(lambda: self.appendcode(h))
        self.bj.clicked.connect(lambda: self.appendcode(j))
        self.bk.clicked.connect(lambda: self.appendcode(k))
        self.bl.clicked.connect(lambda: self.appendcode(l))
        self.bz.clicked.connect(lambda: self.appendcode(z))
        self.bx.clicked.connect(lambda: self.appendcode(x))
        self.bc.clicked.connect(lambda: self.appendcode(c))
        self.bv.clicked.connect(lambda: self.appendcode(v))
        self.bb.clicked.connect(lambda: self.appendcode(b))
        self.bn.clicked.connect(lambda: self.appendcode(n))
        self.bm.clicked.connect(lambda: self.appendcode(m))

        self.bspace.clicked.connect(lambda: self.appendcode(' '))


        self.bback.clicked.connect(self.backspacecode)



