from PyQt5 import QtCore, QtWidgets
import pymysql

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        self.connect_db()
        #主窗口
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 10, 621, 441))
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")

        #登录页面
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.page.setStyleSheet("#page{border-image:url(Pic/login_bg.jpg)}")
        self.Loginbtn = QtWidgets.QPushButton(self.page)
        self.Loginbtn.setGeometry(QtCore.QRect(250, 310, 80, 51))
        self.Loginbtn.setObjectName("Loginbtn")
        self.Loginbtn.setStyleSheet("color:White ; background-color: #27156c ; font-weight:bold")
        self.username = QtWidgets.QLineEdit(self.page)
        self.username.setGeometry(QtCore.QRect(172, 120, 241, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.page)
        self.password.setGeometry(QtCore.QRect(170, 200, 241, 31))
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(170, 100, 80, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("color:white")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(170, 180, 80, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:white")
        self.loginHint = QtWidgets.QLabel(self.page)
        self.loginHint.setGeometry(QtCore.QRect(170, 260, 241, 31))
        self.loginHint.setText("")
        self.loginHint.setObjectName("loginHint")
        self.loginHint.setStyleSheet("color:Red ;font-weight:bold")

        #主页
        self.stackedWidget.addWidget(self.page)
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.home.setStyleSheet("#home{border-image:url(Pic/home_bg.jpg)}")

        self.movietble = QtWidgets.QTableWidget(self.home)
        self.movietble.setMouseTracking(True)
        self.movietble.setTabletTracking(True)
        self.movietble.setAcceptDrops(True)
        self.movietble.setStatusTip("")
        self.movietble.setAccessibleDescription("")
        self.movietble.setAutoFillBackground(True)
        self.movietble.setLineWidth(1)
        self.movietble.setMidLineWidth(0)
        self.movietble.setDragEnabled(True)
        self.movietble.setAlternatingRowColors(False)
        self.movietble.setShowGrid(True)
        self.movietble.setGeometry(QtCore.QRect(10, 10, 601, 351))
        self.movietble.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.movietble.setWordWrap(False)
        self.movietble.setCornerButtonEnabled(True)
        self.movietble.setRowCount(1000)
        self.movietble.setObjectName("movietble")
        self.movietble.setColumnCount(6)


        #初始化表格单元格
        for i in range(1000):
            item = QtWidgets.QTableWidgetItem()
            self.movietble.setVerticalHeaderItem(i, item)

        for i in range(self.movietble.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            self.movietble.setHorizontalHeaderItem(i, item)

        for i in range(1000):
            for j in range(self.movietble.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                self.movietble.setItem(i, j, item)


        self.movietble.horizontalHeader().setVisible(True)
        self.movietble.horizontalHeader().setCascadingSectionResizes(True)
        self.movietble.verticalHeader().setVisible(False)
        #self.movietble.verticalHeader().setSortIndicatorShown(True)
        #self.movietble.horizontalHeader().setSortIndicatorShown(True)
        #self.movietble.verticalHeader().setSortIndicatorShown(True)
        self.movietble.verticalHeader().setStretchLastSection(True)

        self.editbtn = QtWidgets.QPushButton(self.home)
        self.editbtn.setGeometry(QtCore.QRect(450, 375, 80, 51))
        self.editbtn.setObjectName("editbtn")
        self.editbtn.setStyleSheet("color:White ; background-color: #208c9f ; font-weight:bold")
        self.deletebtn = QtWidgets.QPushButton(self.home)
        self.deletebtn.setGeometry(QtCore.QRect(540, 375, 80, 51))
        self.deletebtn.setObjectName("deletebtn")#633722
        self.deletebtn.setStyleSheet("color:White ; background-color: #633722 ; font-weight:bold")
        self.importbtn = QtWidgets.QPushButton(self.home)
        self.importbtn.setGeometry(QtCore.QRect(270, 375, 80, 51))
        self.importbtn.setObjectName("importbtn")
        self.importbtn.setStyleSheet("color:white ; background-color: #483896 ; font-weight:bold")

        self.searchbtn = QtWidgets.QPushButton(self.home)
        self.searchbtn.setGeometry(QtCore.QRect(360, 375, 80, 51))
        self.searchbtn.setObjectName("searchbtn")
        self.searchbtn.setStyleSheet("color:White ; background-color: #753776 ; font-weight:bold")

        self.importbtn_2 = QtWidgets.QPushButton(self.home)
        self.importbtn_2.setGeometry(QtCore.QRect(3, 375, 80, 51))
        self.importbtn_2.setObjectName("importbtn_2")
        self.importbtn_2.setStyleSheet("color:White ; background-color: #27706e ; font-weight:bold")

        #导入电影页面
        self.stackedWidget.addWidget(self.home)
        self.Importpage = QtWidgets.QWidget()
        self.Importpage.setObjectName("Importpage")
        self.Importpage.setStyleSheet("#Importpage{border-image:url(Pic/bg.jpg)}")
        self.Cancelbtn = QtWidgets.QPushButton(self.Importpage)
        self.Cancelbtn.setGeometry(QtCore.QRect(450, 375, 80, 51))
        self.Cancelbtn.setObjectName("Cancelbtn")
        self.Importbtn = QtWidgets.QPushButton(self.Importpage)
        self.Importbtn.setGeometry(QtCore.QRect(540, 375, 80, 51))
        self.Importbtn.setObjectName("Importbtn")
        self.label_3 = QtWidgets.QLabel(self.Importpage)
        self.label_3.setGeometry(QtCore.QRect(190, 20, 200, 31))
        self.label_3.setObjectName("label_3")



        self.label_4 = QtWidgets.QLabel(self.Importpage)
        self.label_4.setGeometry(QtCore.QRect(190, 80, 80, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Importpage)
        self.label_5.setGeometry(QtCore.QRect(190, 120, 80, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Importpage)
        self.label_6.setGeometry(QtCore.QRect(190, 160, 80, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Importpage)
        self.label_7.setGeometry(QtCore.QRect(190, 200, 80, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Importpage)
        self.label_8.setGeometry(QtCore.QRect(190, 240, 80, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Importpage)
        self.label_9.setGeometry(QtCore.QRect(190, 280, 80, 31))
        self.label_9.setObjectName("label_9")

        self.idinp = QtWidgets.QLineEdit(self.Importpage)
        self.idinp.setGeometry(QtCore.QRect(280, 85, 151, 20))
        self.idinp.setObjectName("idinp")
        self.idinp.setText('')
        self.nameinp = QtWidgets.QLineEdit(self.Importpage)
        self.nameinp.setGeometry(QtCore.QRect(280, 125, 151, 20))
        self.nameinp.setObjectName("nameinp")
        self.nameinp.setText('')
        self.rateinp = QtWidgets.QLineEdit(self.Importpage)
        self.rateinp.setGeometry(QtCore.QRect(280, 205, 151, 20))
        self.rateinp.setObjectName("rateinp")
        self.rateinp.setText('')
        self.typeinp = QtWidgets.QLineEdit(self.Importpage)
        self.typeinp.setGeometry(QtCore.QRect(280, 165, 151, 20))
        self.typeinp.setObjectName("typeinp")
        self.typeinp.setText('')
        self.linkinp = QtWidgets.QLineEdit(self.Importpage)
        self.linkinp.setGeometry(QtCore.QRect(280, 285, 151, 20))
        self.linkinp.setObjectName("linkinp")
        self.linkinp.setText('')
        self.yearinp = QtWidgets.QLineEdit(self.Importpage)
        self.yearinp.setGeometry(QtCore.QRect(280, 245, 151, 20))
        self.yearinp.setObjectName("yearinp")
        self.yearinp.setText('')
        self.Hint = QtWidgets.QLabel(self.Importpage)
        self.Hint.setGeometry(QtCore.QRect(190, 340, 241, 31))
        self.Hint.setText("")
        self.Hint.setObjectName("Hint")

        self.Importbtn.setStyleSheet("color:white ; background-color: #483896 ; font-weight:bold")
        self.label_3.setStyleSheet("color:white ; font-weight: bold;")
        # self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setStyleSheet("color:white ; font-weight: bold;")
        self.label_5.setStyleSheet("color:white ; font-weight: bold;")
        self.label_6.setStyleSheet("color:white ; font-weight: bold;")
        self.label_7.setStyleSheet("color:white ; font-weight: bold;")
        self.label_8.setStyleSheet("color:white ; font-weight: bold;")
        self.label_9.setStyleSheet("color:white ; font-weight: bold;")
        self.Hint.setStyleSheet("font-size: 14px ; color:red ; font-weight: bold;")

        #搜索电影页面
        self.stackedWidget.addWidget(self.Importpage)
        self.searchpage = QtWidgets.QWidget()
        self.searchpage.setObjectName("searchpage")
        self.searchpage.setStyleSheet("#searchpage{border-image:url(Pic/search_bg.jpg)}")
        self.Searchbtn = QtWidgets.QPushButton(self.searchpage)
        self.Searchbtn.setGeometry(QtCore.QRect(540, 375, 80, 51))
        self.Searchbtn.setObjectName("Searchbtn")
        self.Cancelbtn_2 = QtWidgets.QPushButton(self.searchpage)
        self.Cancelbtn_2.setGeometry(QtCore.QRect(450, 375, 80, 51))
        self.Cancelbtn_2.setObjectName("Cancelbtn_2")
        self.label_10 = QtWidgets.QLabel(self.searchpage)
        self.label_10.setGeometry(QtCore.QRect(190, 20, 241, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.searchpage)
        self.label_11.setGeometry(QtCore.QRect(190, 280, 80, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.searchpage)
        self.label_12.setGeometry(QtCore.QRect(190, 200, 80, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.searchpage)
        self.label_13.setGeometry(QtCore.QRect(190, 240, 80, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.searchpage)
        self.label_14.setGeometry(QtCore.QRect(190, 120, 80, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.searchpage)
        self.label_15.setGeometry(QtCore.QRect(190, 80, 80, 31))
        self.label_15.setObjectName("label_15")
        self.idinp_2 = QtWidgets.QLineEdit(self.searchpage)
        self.idinp_2.setGeometry(QtCore.QRect(190, 50, 241, 20))
        self.idinp_2.setObjectName("idinp_2")
        self.label_16 = QtWidgets.QLabel(self.searchpage)
        self.label_16.setGeometry(QtCore.QRect(190, 160, 80, 31))
        self.label_16.setObjectName("label_16")
        self.Hint_2 = QtWidgets.QLabel(self.searchpage)
        self.Hint_2.setGeometry(QtCore.QRect(190, 340, 241, 31))
        self.Hint_2.setText("")
        self.Hint_2.setObjectName("Hint_2")
        self.show4 = QtWidgets.QLabel(self.searchpage)
        self.show4.setGeometry(QtCore.QRect(280, 200, 151, 31))
        self.show4.setText("")
        self.show4.setObjectName("show4")

        self.show5 = QtWidgets.QLabel(self.searchpage)
        self.show5.setGeometry(QtCore.QRect(280, 240, 151, 31))
        self.show5.setText("")
        self.show5.setObjectName("show5")

        self.show1 = QtWidgets.QLabel(self.searchpage)
        self.show1.setGeometry(QtCore.QRect(280, 80, 151, 31))
        self.show1.setText("")
        self.show1.setObjectName("show1")

        self.show6 = QtWidgets.QLineEdit(self.searchpage)
        self.show6.setGeometry(QtCore.QRect(280, 280, 151, 31))
        self.show6.setObjectName("show6")

        self.show2 = QtWidgets.QLabel(self.searchpage)
        self.show2.setGeometry(QtCore.QRect(280, 120, 151, 31))
        self.show2.setText("")
        self.show2.setObjectName("show2")
        self.show3 = QtWidgets.QLabel(self.searchpage)
        self.show3.setGeometry(QtCore.QRect(280, 160, 151, 31))
        self.show3.setText("")
        self.show3.setObjectName("show3")

        self.label_10.setStyleSheet("color:White; font-weight:bold")
        self.label_11.setStyleSheet("color:White; font-weight:bold")
        self.label_12.setStyleSheet("color:White; font-weight:bold")
        self.label_13.setStyleSheet("color:White; font-weight:bold")
        self.label_14.setStyleSheet("color:White; font-weight:bold")
        self.label_15.setStyleSheet("color:White; font-weight:bold")
        self.label_16.setStyleSheet("color:White; font-weight:bold")
        self.show1.setStyleSheet("color:White; font-weight:bold")
        self.show2.setStyleSheet("color:White; font-weight:bold")
        self.show3.setStyleSheet("color:White; font-weight:bold")
        self.show4.setStyleSheet("color:White; font-weight:bold")
        self.show5.setStyleSheet("color:White; font-weight:bold")
        self.show6.setStyleSheet("color:Black; font-weight:bold")
        self.Hint_2.setStyleSheet("color:red; font-weight:bold")
        self.Searchbtn.setStyleSheet("color:White ; background-color: #753776 ; font-weight:bold")

        #编辑电影页面
        self.stackedWidget.addWidget(self.searchpage)
        self.editpage = QtWidgets.QWidget()
        self.editpage.setObjectName("editpage")
        self.editpage.setStyleSheet("#editpage{border-image:url(Pic/change_bg.jpg)}")
        self.Cancelbtn_3 = QtWidgets.QPushButton(self.editpage)
        self.Cancelbtn_3.setGeometry(QtCore.QRect(450, 375, 80, 51))
        self.Cancelbtn_3.setObjectName("Cancelbtn_3")
        self.Submitbtn = QtWidgets.QPushButton(self.editpage)
        self.Submitbtn.setGeometry(QtCore.QRect(540, 375, 80, 51))
        self.Submitbtn.setObjectName("Submitbtn")
        self.Submitbtn.setStyleSheet("color:White ; background-color: #208c9f ; font-weight:bold")
        self.show2_2 = QtWidgets.QLabel(self.editpage)
        self.show2_2.setGeometry(QtCore.QRect(230, 160, 91, 31))
        self.show2_2.setText("")
        self.show2_2.setObjectName("show2_2")
        self.show2_2.setStyleSheet("color:White; font-weight:bold")


        self.show6_2 = QtWidgets.QLineEdit(self.editpage)
        self.show6_2.setGeometry(QtCore.QRect(230, 320, 91, 31))
        self.show6_2.setObjectName("idinp_3")


        self.show1_2 = QtWidgets.QLabel(self.editpage)
        self.show1_2.setGeometry(QtCore.QRect(230, 120, 91, 31))
        self.show1_2.setText("")
        self.show1_2.setObjectName("show1_2")
        self.show1_2.setStyleSheet("color:White; font-weight:bold")
        self.label_17 = QtWidgets.QLabel(self.editpage)
        self.label_17.setGeometry(QtCore.QRect(190, 20, 241, 31))
        self.label_17.setObjectName("label_17")
        self.label_17.setStyleSheet("color:White; font-weight:bold")
        self.show3_2 = QtWidgets.QLabel(self.editpage)
        self.show3_2.setGeometry(QtCore.QRect(230, 200, 91, 31))
        self.show3_2.setText("")
        self.show3_2.setObjectName("show3_2")
        self.show3_2.setStyleSheet("color:White; font-weight:bold")
        self.show4_2 = QtWidgets.QLabel(self.editpage)
        self.show4_2.setGeometry(QtCore.QRect(230, 240, 91, 31))
        self.show4_2.setText("")
        self.show4_2.setObjectName("show4_2")
        self.show4_2.setStyleSheet("color:White; font-weight:bold")
        self.label_18 = QtWidgets.QLabel(self.editpage)
        self.label_18.setGeometry(QtCore.QRect(140, 240, 80, 31))
        self.label_18.setObjectName("label_18")
        self.label_18.setStyleSheet("color:White; font-weight:bold")
        self.label_19 = QtWidgets.QLabel(self.editpage)
        self.label_19.setGeometry(QtCore.QRect(140, 280, 80, 31))
        self.label_19.setObjectName("label_19")
        self.label_19.setStyleSheet("color:White; font-weight:bold")
        self.Hint_3 = QtWidgets.QLabel(self.editpage)
        self.Hint_3.setGeometry(QtCore.QRect(140, 360, 341, 31))
        self.Hint_3.setText("")
        self.Hint_3.setObjectName("Hint_3")
        self.Hint_3.setStyleSheet("color:Red; font-weight:bold")
        self.label_20 = QtWidgets.QLabel(self.editpage)
        self.label_20.setGeometry(QtCore.QRect(140, 120, 80, 31))
        self.label_20.setObjectName("label_20")
        self.label_20.setStyleSheet("color:White; font-weight:bold")
        self.label_21 = QtWidgets.QLabel(self.editpage)
        self.label_21.setGeometry(QtCore.QRect(140, 320, 80, 31))
        self.label_21.setObjectName("label_21")
        self.label_21.setStyleSheet("color:White; font-weight:bold")
        self.idinp_3 = QtWidgets.QLineEdit(self.editpage)
        self.idinp_3.setGeometry(QtCore.QRect(190, 50, 171, 20))
        self.idinp_3.setObjectName("idinp_3")
        self.label_22 = QtWidgets.QLabel(self.editpage)
        self.label_22.setGeometry(QtCore.QRect(140, 160, 80, 31))
        self.label_22.setObjectName("label_22")
        self.label_22.setStyleSheet("color:White; font-weight:bold")
        self.label_23 = QtWidgets.QLabel(self.editpage)
        self.label_23.setGeometry(QtCore.QRect(140, 200, 80, 31))
        self.label_23.setObjectName("label_23")
        self.label_23.setStyleSheet("color:White; font-weight:bold")
        self.show5_2 = QtWidgets.QLabel(self.editpage)
        self.show5_2.setGeometry(QtCore.QRect(230, 280, 91, 31))
        self.show5_2.setText("")
        self.show5_2.setObjectName("show5_2")
        self.show5_2.setStyleSheet("color:White; font-weight:bold")
        self.nameinp_2 = QtWidgets.QLineEdit(self.editpage)
        self.nameinp_2.setGeometry(QtCore.QRect(330, 159, 151, 31))
        self.nameinp_2.setObjectName("nameinp_2")
        self.nameinp_2.setText('')
        self.yearinp_2 = QtWidgets.QLineEdit(self.editpage)
        self.yearinp_2.setGeometry(QtCore.QRect(330, 279, 151, 31))
        self.yearinp_2.setObjectName("yearinp_2")
        self.yearinp_2.setText('')
        self.typeinp_2 = QtWidgets.QLineEdit(self.editpage)
        self.typeinp_2.setGeometry(QtCore.QRect(330, 199, 151, 31))
        self.typeinp_2.setObjectName("typeinp_2")
        self.typeinp_2.setText('')
        self.linkinp_2 = QtWidgets.QLineEdit(self.editpage)
        self.linkinp_2.setGeometry(QtCore.QRect(330, 319, 151, 31))
        self.linkinp_2.setObjectName("linkinp_2")
        self.linkinp_2.setText('')
        self.rateinp_2 = QtWidgets.QLineEdit(self.editpage)
        self.rateinp_2.setGeometry(QtCore.QRect(330, 239, 151, 31))
        self.rateinp_2.setObjectName("rateinp_2")
        self.rateinp_2.setText('')
        self.idinp_4 = QtWidgets.QLineEdit(self.editpage)
        self.idinp_4.setGeometry(QtCore.QRect(330, 119, 151, 31))
        self.idinp_4.setObjectName("idinp_4")
        self.idinp_4.setText('')
        self.show1_3 = QtWidgets.QLabel(self.editpage)
        self.show1_3.setGeometry(QtCore.QRect(230, 80, 51, 31))
        self.show1_3.setObjectName("show1_3")
        self.show1_3.setStyleSheet("font-size:11px ; color:White; font-weight:bold")

        self.show1_4 = QtWidgets.QLabel(self.editpage)
        self.show1_4.setGeometry(QtCore.QRect(330, 80, 21, 31))
        self.show1_4.setObjectName("show1_4")
        self.show1_4.setStyleSheet("font-size:11px ; color:White; font-weight:bold")
        self.UpdateSearchbtn = QtWidgets.QPushButton(self.editpage)
        self.UpdateSearchbtn.setGeometry(QtCore.QRect(370, 50, 61, 21))
        self.UpdateSearchbtn.setObjectName("UpdateSearchbtn")

        #删除电影页面
        self.stackedWidget.addWidget(self.editpage)
        self.deletepage = QtWidgets.QWidget()
        self.deletepage.setObjectName("deletepage")
        self.deletepage.setStyleSheet("#deletepage{border-image:url(Pic/login_bg.jpg)}")
        self.Cancelbtn_4 = QtWidgets.QPushButton(self.deletepage)
        self.Cancelbtn_4.setGeometry(QtCore.QRect(450, 375, 80, 51))
        self.Cancelbtn_4.setObjectName("Cancelbtn_4")
        self.Delete = QtWidgets.QPushButton(self.deletepage)
        self.Delete.setGeometry(QtCore.QRect(540, 375, 80, 51))
        self.Delete.setObjectName("Delete")
        self.Delete.setStyleSheet("color:White ; background-color: #633722 ; font-weight:bold")
        self.show2_3 = QtWidgets.QLabel(self.deletepage)
        self.show2_3.setGeometry(QtCore.QRect(280, 120, 151, 31))
        self.show2_3.setText("")
        self.show2_3.setObjectName("show2_3")
        self.show2_3.setStyleSheet("color:White; font-weight:bold")

        self.show6_3= QtWidgets.QLineEdit(self.deletepage)
        self.show6_3.setGeometry(QtCore.QRect(280, 280, 151, 31))
        self.show6_3.setObjectName("show6_3")
        self.show6_3.setStyleSheet("color:Black; font-weight:bold")


        self.show1_5 = QtWidgets.QLabel(self.deletepage)
        self.show1_5.setGeometry(QtCore.QRect(280, 80, 151, 31))
        self.show1_5.setText("")
        self.show1_5.setObjectName("show1_5")
        self.show1_5.setStyleSheet("color:White; font-weight:bold")

        self.label_24 = QtWidgets.QLabel(self.deletepage)
        self.label_24.setGeometry(QtCore.QRect(190, 20, 241, 31))
        self.label_24.setObjectName("label_24")
        self.label_24.setStyleSheet("color:White; font-weight:bold")

        self.show3_3 = QtWidgets.QLabel(self.deletepage)
        self.show3_3.setGeometry(QtCore.QRect(280, 160, 151, 31))
        self.show3_3.setText("")
        self.show3_3.setObjectName("show3_3")
        self.show3_3.setStyleSheet("color:White; font-weight:bold")
        self.show4_3 = QtWidgets.QLabel(self.deletepage)
        self.show4_3.setGeometry(QtCore.QRect(280, 200, 151, 31))
        self.show4_3.setText("")
        self.show4_3.setObjectName("show4_3")
        self.show4_3.setStyleSheet("color:White; font-weight:bold")
        self.label_25 = QtWidgets.QLabel(self.deletepage)
        self.label_25.setGeometry(QtCore.QRect(190, 200, 80, 31))
        self.label_25.setObjectName("label_25")
        self.label_25.setStyleSheet("color:White; font-weight:bold")
        self.label_26 = QtWidgets.QLabel(self.deletepage)
        self.label_26.setGeometry(QtCore.QRect(190, 240, 80, 31))
        self.label_26.setObjectName("label_26")
        self.label_26.setStyleSheet("color:White; font-weight:bold")
        self.Hint_4 = QtWidgets.QLabel(self.deletepage)
        self.Hint_4.setGeometry(QtCore.QRect(190, 340, 241, 31))
        self.Hint_4.setText("")
        self.Hint_4.setObjectName("Hint_4")
        self.Hint_4.setStyleSheet("color:Red; font-weight:bold")
        self.label_27 = QtWidgets.QLabel(self.deletepage)
        self.label_27.setGeometry(QtCore.QRect(190, 80, 80, 31))
        self.label_27.setObjectName("label_27")
        self.label_27.setStyleSheet("color:White; font-weight:bold")
        self.label_28 = QtWidgets.QLabel(self.deletepage)
        self.label_28.setGeometry(QtCore.QRect(190, 280, 80, 31))
        self.label_28.setObjectName("label_28")
        self.label_28.setStyleSheet("color:White; font-weight:bold")
        self.idinp_5 = QtWidgets.QLineEdit(self.deletepage)
        self.idinp_5.setGeometry(QtCore.QRect(190, 50, 171, 20))
        self.idinp_5.setObjectName("idinp_5")
        self.label_29 = QtWidgets.QLabel(self.deletepage)
        self.label_29.setGeometry(QtCore.QRect(190, 120, 80, 31))
        self.label_29.setObjectName("label_29")
        self.label_29.setStyleSheet("color:White; font-weight:bold")
        self.label_30 = QtWidgets.QLabel(self.deletepage)
        self.label_30.setGeometry(QtCore.QRect(190, 160, 80, 31))
        self.label_30.setObjectName("label_30")
        self.label_30.setStyleSheet("color:White; font-weight:bold")
        self.show5_3 = QtWidgets.QLabel(self.deletepage)
        self.show5_3.setGeometry(QtCore.QRect(280, 240, 151, 31))
        self.show5_3.setText("")
        self.show5_3.setObjectName("show5_3")
        self.show5_3.setStyleSheet("color:White; font-weight:bold")
        self.DeleteSearchbtn = QtWidgets.QPushButton(self.deletepage)
        self.DeleteSearchbtn.setGeometry(QtCore.QRect(370, 50, 61, 21))
        self.DeleteSearchbtn.setObjectName("DeleteSearchbtn")
        self.stackedWidget.addWidget(self.deletepage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #按钮页面跳转实现
        self.importbtn.clicked.connect(self.frameController)
        self.searchbtn.clicked.connect(self.frameController)
        self.deletebtn.clicked.connect(self.frameController)
        self.editbtn.clicked.connect(self.frameController)
        self.Cancelbtn.clicked.connect(self.cancel_btn)
        self.Cancelbtn_2.clicked.connect(self.cancel_btn)
        self.Cancelbtn_3.clicked.connect(self.cancel_btn)
        self.Cancelbtn_4.clicked.connect(self.cancel_btn)
        self.importbtn_2.clicked.connect(self.frameController)
        self.Loginbtn.clicked.connect(self.login_btn)

        self.Importbtn.clicked.connect(self.import_movie)
        self.Searchbtn.clicked.connect(self.search_movie)
        self.UpdateSearchbtn.clicked.connect(self.edit_search)
        self.Submitbtn.clicked.connect(self.edit_movie)
        self.DeleteSearchbtn.clicked.connect(self.delete_search)
        self.Delete.clicked.connect(self.delete_movie)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Management System"))
        self.Loginbtn.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "User Name："))
        self.label_2.setText(_translate("MainWindow", "Password："))
        #self.movietble.setSortingEnabled(True)
        item = self.movietble.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.movietble.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.movietble.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.movietble.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.movietble.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.movietble.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rate"))
        item = self.movietble.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Year"))
        item = self.movietble.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Link"))
        #__sortingEnabled = self.movietble.isSortingEnabled()
        #self.movietble.setSortingEnabled(False)

        self.update_movie_tables()

        #self.movietble.setSortingEnabled(__sortingEnabled)

        self.editbtn.setText(_translate("MainWindow", "Edit"))
        self.deletebtn.setText(_translate("MainWindow", "Delete"))
        self.importbtn.setText(_translate("MainWindow", "Import"))
        self.searchbtn.setText(_translate("MainWindow", "Search"))
        self.importbtn_2.setText(_translate("MainWindow", "Exit"))
        self.Cancelbtn.setText(_translate("MainWindow", "Cancel"))
        self.Importbtn.setText(_translate("MainWindow", "Import"))
        self.label_3.setText(_translate("MainWindow", "Please Enter Movie Info："))
        self.label_4.setText(_translate("MainWindow", "ID:"))
        self.label_5.setText(_translate("MainWindow", "Name："))
        self.label_6.setText(_translate("MainWindow", "Type："))
        self.label_7.setText(_translate("MainWindow", "Rate："))
        self.label_8.setText(_translate("MainWindow", "Year："))
        self.label_9.setText(_translate("MainWindow", "Link："))
        self.Searchbtn.setText(_translate("MainWindow", "Search"))
        self.Cancelbtn_2.setText(_translate("MainWindow", "Cancel"))
        self.label_10.setText(_translate("MainWindow", "Please Enter Movie ID/Name："))
        self.label_11.setText(_translate("MainWindow", "Link："))
        self.label_12.setText(_translate("MainWindow", "Rate："))
        self.label_13.setText(_translate("MainWindow", "Year："))
        self.label_14.setText(_translate("MainWindow", "Name："))
        self.label_15.setText(_translate("MainWindow", "ID:"))
        self.label_16.setText(_translate("MainWindow", "Type："))
        self.Cancelbtn_3.setText(_translate("MainWindow", "Cancel"))
        self.Submitbtn.setText(_translate("MainWindow", "Submit"))
        self.label_17.setText(_translate("MainWindow", "Please Enter Movie ID/Name："))
        self.label_18.setText(_translate("MainWindow", "Rate："))
        self.label_19.setText(_translate("MainWindow", "Year："))
        self.label_20.setText(_translate("MainWindow", "ID:"))
        self.label_21.setText(_translate("MainWindow", "Link："))
        self.label_22.setText(_translate("MainWindow", "Name："))
        self.label_23.setText(_translate("MainWindow", "Type："))
        self.show1_3.setText(_translate("MainWindow", "Original"))
        self.show1_4.setText(_translate("MainWindow", "New"))
        self.UpdateSearchbtn.setText(_translate("MainWindow", "Search"))
        self.Cancelbtn_4.setText(_translate("MainWindow", "Cancel"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.label_24.setText(_translate("MainWindow", "Please Enter Movie ID/Name："))
        self.label_25.setText(_translate("MainWindow", "Rate："))
        self.label_26.setText(_translate("MainWindow", "Year："))
        self.label_27.setText(_translate("MainWindow", "ID:"))
        self.label_28.setText(_translate("MainWindow", "Link："))
        self.label_29.setText(_translate("MainWindow", "Name："))
        self.label_30.setText(_translate("MainWindow", "Type："))
        self.DeleteSearchbtn.setText(_translate("MainWindow", "Search"))

    def frameController(self):  # 页面控制函数
        self.idinp.setText('')
        self.nameinp.setText('')
        self.typeinp.setText('')
        self.rateinp.setText('')
        self.yearinp.setText('')
        self.linkinp.setText('')
        self.Hint.setText('')
        self.idinp_2.setText('')
        self.Hint_2.setText('')
        self.Hint_3.setText('')
        self.Hint_4.setText('')
        self.show1.setText('')
        self.show2.setText('')
        self.show3.setText('')
        self.show4.setText('')
        self.show5.setText('')
        self.show6.setText('')
        self.username.setText('')
        self.password.setText('')
        self.show1_5.setText('')
        self.show2_3.setText('')
        self.show3_3.setText('')
        self.show4_3.setText('')
        self.show5_3.setText('')
        self.show6_3.setText('')
        self.idinp_5.setText('')
        self.Hint_3.setText('')
        self.show1_2.setText('')
        self.show2_2.setText('')
        self.show3_2.setText('')
        self.show4_2.setText('')
        self.show5_2.setText('')
        self.show6_2.setText('')
        self.idinp_3.setText('')
        self.loginHint.setText('')

        sender = self.sender().objectName()  # 获取当前信号 sender
        index = {
            "importbtn": 2,  # import
            'searchbtn': 3,
            'editbtn' : 4,
            'deletebtn' : 5,
            'Cancelbtn' : 1,
            'Cancelbtn_2' : 1,
            'Cancelbtn_3' : 1,
            'Cancelbtn_4' : 1,
            'Cancelbtn_5' : 1,
            'importbtn_2' : 0
        }
        self.stackedWidget.setCurrentIndex(index[sender])  # 根据信号 index 设置所显示的页面

    def login_btn(self):
        if self.username.text() == 'root' and self.password.text() == '123456':
            self.stackedWidget.setCurrentIndex(1)  #登录成功
        else:
            self.loginHint.setText('Login Failed,Please Try Again.')

    def connect_db(self):
        # 连接数据库
        self.db = pymysql.connect(host="localhost", user="root", password="123456", database="movie")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # 通配符，意思是查询表里所有内容
        cursor.execute("select * from video")
        self.db.commit()
        # 使用 fetchone() 方法获取所有行数据.
        self.data = cursor.fetchall()
        self.rowNum = len(self.data)  # 数据条数
        # 关闭数据库连接
        self.db.close()

    def import_movie(self):
        # 执行sql语句
        if self.idinp.text()=='' or  self.nameinp.text()=='' or self.typeinp.text()=='' or self.rateinp.text()=='':
            self.Hint.setText('ID,Name,Type,Rate must be filled.')
            self.idinp.setText('')
            self.nameinp.setText('')
            self.typeinp.setText('')
            self.rateinp.setText('')
        else:
            # 打开数据库连接
            db = pymysql.connect(host="localhost", user="root", password="123456", database="movie")
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            cursor.execute(
                "select * from video where id='{}'".format(self.idinp.text()))
            db.commit()
            # 使用 fetchone() 方法获取所有行数据.
            data = cursor.fetchall()
            if data == ():
                sql_str = "insert into video values ('{}','{}','{}',{},'{}','{}');".format(self.idinp.text(),
                                                                                           self.nameinp.text(),
                                                                                           self.typeinp.text(),
                                                                                           float(self.rateinp.text()),
                                                                                           self.yearinp.text(),
                                                                                           self.linkinp.text())
                cursor.execute(sql_str)
                # 提交到数据库执行
                db.commit()
                self.Hint.setText('Imported Successfully!')
                self.idinp.setText('')
                self.nameinp.setText('')
                self.typeinp.setText('')
                self.rateinp.setText('')
                self.yearinp.setText('')
                self.linkinp.setText('')
                # 关闭数据库连接
                db.close()
            else:
                self.Hint.setText('This ID Is Existed.')

    def search_movie(self):
        # 打开数据库连接     数据库地址
        db = pymysql.connect(host="localhost", user="root", password="123456", database="movie")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 通配符，意思是查询表里所有内容
        cursor.execute("select * from video where id='{}' or name like '{}%'".format(self.idinp_2.text(),self.idinp_2.text()))
        db.commit()
        # 使用 fetchone() 方法获取所有行数据.
        data = cursor.fetchall()
        if data == ():
            self.Hint_2.setText('No Movie Found.')
            self.show1.setText('')
            self.show2.setText('')
            self.show3.setText('')
            self.show4.setText('')
            self.show5.setText('')
            self.show6.setText('')
        else:
            self.Hint_2.setText('')
            self.show1.setText(str(data[0][0]))
            self.show2.setText(str(data[0][1]))
            self.show3.setText(str(data[0][2]))
            self.show4.setText(str(data[0][3]))
            self.show5.setText(str(data[0][4]))
            self.show6.setText(str(data[0][5]))

    def edit_search(self):
        self.deletable = 0
        # 打开数据库连接     数据库地址
        db = pymysql.connect(host="localhost", user="root", password="123456", database="movie")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 通配符，意思是查询表里所有内容
        cursor.execute(
            "select * from video where id='{}' or name like '{}%'".format(self.idinp_3.text(), self.idinp_3.text()))
        db.commit()
        # 使用 fetchone() 方法获取所有行数据.
        data = cursor.fetchall()
        if data == ():
            self.Hint_3.setText('No Movie Found.')
            self.show1_2.setText('')
            self.show2_2.setText('')
            self.show3_2.setText('')
            self.show4_2.setText('')
            self.show5_2.setText('')
            self.show6_2.setText('')
        else:
            self.Hint_3.setText('')
            self.changable = 1
            self.Hint_4.setText('')
            self.show1_2.setText(str(data[0][0]))
            self.show2_2.setText(str(data[0][1]))
            self.show3_2.setText(str(data[0][2]))
            self.show4_2.setText(str(data[0][3]))
            self.show5_2.setText(str(data[0][4]))
            self.show6_2.setText(str(data[0][5]))

    def edit_movie(self):
        if self.show1_2.text()!='':
            if self.idinp_4.text() != '' and self.nameinp_2.text() != '' and self.typeinp_2.text() != '' and self.rateinp_2.text() != '':
                # 打开数据库连接     数据库地址
                db = pymysql.connect(host="localhost", user="root", password="123456", database="movie")
                # 使用 cursor() 方法创建一个游标对象 cursor
                cursor = db.cursor()
                # 通配符，意思是查询表里所有内容
                cursor.execute(
                    "delete from video where id='{}' or name like '{}%'".format(self.idinp_3.text(),
                                                                                self.idinp_3.text()))
                db.commit()

                sql_str = "insert into video values ('{}','{}','{}',{},'{}','{}');".format(self.idinp_4.text(),
                                                                                           self.nameinp_2.text(),
                                                                                           self.typeinp_2.text(),
                                                                                           float(self.rateinp_2.text()),
                                                                                           self.yearinp_2.text(),
                                                                                           self.linkinp_2.text())
                cursor.execute(sql_str)
                # 提交到数据库执行
                db.commit()
                db.close()
                self.Hint_3.setText('Updated Successfully.')
                self.show1_2.setText('')
                self.show2_2.setText('')
                self.show3_2.setText('')
                self.show4_2.setText('')
                self.show5_2.setText('')
                self.show6_2.setText('')
                self.idinp_3.setText('')
                self.idinp_4.setText('')
                self.nameinp_2.setText('')
                self.typeinp_2.setText('')
                self.rateinp_2.setText('')
                self.yearinp_2.setText('')
                self.linkinp_2.setText('')


            else:
                self.Hint_3.setText('ID,Name,Type,Rate must be filled.')
        else:
            self.Hint_3.setText('Operation Failed.')

    def delete_search(self):
        self.deletable = 0
        # 打开数据库连接     数据库地址
        db = pymysql.connect(host="localhost", user="root", password="123456", database="movie")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 通配符，意思是查询表里所有内容
        cursor.execute(
            "select * from video where id='{}' or name like '{}%'".format(self.idinp_5.text(), self.idinp_5.text()))
        db.commit()
        # 使用 fetchone() 方法获取所有行数据.
        data = cursor.fetchall()
        if data == ():
            self.Hint_4.setText('No Movie Found.')
            self.show1_5.setText('')
            self.show2_3.setText('')
            self.show3_3.setText('')
            self.show4_3.setText('')
            self.show5_3.setText('')
            self.show6_3.setText('')
        else:
            self.deletable = 1
            self.Hint_4.setText('')
            self.show1_5.setText(str(data[0][0]))
            self.show2_3.setText(str(data[0][1]))
            self.show3_3.setText(str(data[0][2]))
            self.show4_3.setText(str(data[0][3]))
            self.show5_3.setText(str(data[0][4]))
            self.show6_3.setText(str(data[0][5]))

    def delete_movie(self):
        if self.show1_5.text()!='':
            # 打开数据库连接     数据库地址
            db = pymysql.connect(host="localhost", user="root", password="123456", database="movie")
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            # 通配符，意思是查询表里所有内容
            cursor.execute(
                "delete from video where id='{}' or name like '{}%'".format(self.idinp_5.text(), self.idinp_5.text()))
            db.commit()
            self.Hint_4.setText('Deleted Successfully.')
            self.show1_5.setText('')
            self.show2_3.setText('')
            self.show3_3.setText('')
            self.show4_3.setText('')
            self.show5_3.setText('')
            self.show6_3.setText('')
            self.deletable = 0
        else:
            self.Hint_4.setText('Operation Failed.')
            self.show1_5.setText('')
            self.show2_3.setText('')
            self.show3_3.setText('')
            self.show4_3.setText('')
            self.show5_3.setText('')
            self.show6_3.setText('')

    def update_movie_tables(self):
        self.connect_db()
        # for i in range(1000):
        #     item = QtWidgets.QTableWidgetItem()
        #     self.movietble.setVerticalHeaderItem(i, item)
        #
        # for i in range(self.movietble.columnCount()):
        #     item = QtWidgets.QTableWidgetItem()
        #     self.movietble.setHorizontalHeaderItem(i, item)

        for i in range(1000):
            for j in range(self.movietble.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                self.movietble.setItem(i, j, item)

        for i in range(self.rowNum):
            for j in range(self.movietble.columnCount()):
                item = self.movietble.item(i, j)
                item.setText(QtCore.QCoreApplication.translate("MainWindow", str(self.data[i][j])))

    def cancel_btn(self):
        self.update_movie_tables()
        self.stackedWidget.setCurrentIndex(1)  # 回到主界面



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
