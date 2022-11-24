# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1278, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/*QPushButton {\n"
"    border: none; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #cce8f2;\n"
"}\n"
"*/")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(3, 2, 3, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setMaximumSize(QtCore.QSize(1677777, 16777215))
        self.frame_top.setStyleSheet("")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_top_left = QtWidgets.QFrame(self.frame_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top_left.sizePolicy().hasHeightForWidth())
        self.frame_top_left.setSizePolicy(sizePolicy)
        self.frame_top_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_left.setObjectName("frame_top_left")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top_left)
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.show_all_button = QtWidgets.QToolButton(self.frame_top_left)
        self.show_all_button.setMinimumSize(QtCore.QSize(60, 60))
        self.show_all_button.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.show_all_button.setFont(font)
        self.show_all_button.setToolTipDuration(1000)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/planning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_all_button.setIcon(icon)
        self.show_all_button.setIconSize(QtCore.QSize(34, 36))
        self.show_all_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.show_all_button.setObjectName("show_all_button")
        self.horizontalLayout_3.addWidget(self.show_all_button)
        self.help = QtWidgets.QToolButton(self.frame_top_left)
        self.help.setMinimumSize(QtCore.QSize(60, 60))
        self.help.setMaximumSize(QtCore.QSize(60, 60))
        self.help.setToolTipDuration(1000)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/working.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon1)
        self.help.setIconSize(QtCore.QSize(33, 33))
        self.help.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.help.setObjectName("help")
        self.horizontalLayout_3.addWidget(self.help)
        self.setting = QtWidgets.QToolButton(self.frame_top_left)
        self.setting.setMinimumSize(QtCore.QSize(60, 60))
        self.setting.setMaximumSize(QtCore.QSize(60, 60))
        self.setting.setToolTipDuration(1000)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/settings (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon2)
        self.setting.setIconSize(QtCore.QSize(33, 33))
        self.setting.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.setting.setObjectName("setting")
        self.horizontalLayout_3.addWidget(self.setting)
        self.update = QtWidgets.QToolButton(self.frame_top_left)
        self.update.setMinimumSize(QtCore.QSize(60, 60))
        self.update.setMaximumSize(QtCore.QSize(60, 60))
        self.update.setToolTipDuration(1000)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/all-inclusive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update.setIcon(icon3)
        self.update.setIconSize(QtCore.QSize(35, 35))
        self.update.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.update.setObjectName("update")
        self.horizontalLayout_3.addWidget(self.update)
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.index_button = QtWidgets.QToolButton(self.frame_top_left)
        self.index_button.setMinimumSize(QtCore.QSize(60, 60))
        self.index_button.setMaximumSize(QtCore.QSize(60, 60))
        self.index_button.setToolTipDuration(1000)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/documents.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.index_button.setIcon(icon4)
        self.index_button.setIconSize(QtCore.QSize(33, 33))
        self.index_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.index_button.setObjectName("index_button")
        self.horizontalLayout_3.addWidget(self.index_button)
        self.text_scale_up = QtWidgets.QToolButton(self.frame_top_left)
        self.text_scale_up.setMinimumSize(QtCore.QSize(60, 60))
        self.text_scale_up.setMaximumSize(QtCore.QSize(60, 60))
        self.text_scale_up.setToolTipDuration(1000)
        self.text_scale_up.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/zoom-in (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.text_scale_up.setIcon(icon5)
        self.text_scale_up.setIconSize(QtCore.QSize(34, 34))
        self.text_scale_up.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.text_scale_up.setObjectName("text_scale_up")
        self.horizontalLayout_3.addWidget(self.text_scale_up)
        self.text_scale_down = QtWidgets.QToolButton(self.frame_top_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_scale_down.sizePolicy().hasHeightForWidth())
        self.text_scale_down.setSizePolicy(sizePolicy)
        self.text_scale_down.setMinimumSize(QtCore.QSize(60, 60))
        self.text_scale_down.setMaximumSize(QtCore.QSize(60, 60))
        self.text_scale_down.setToolTipDuration(1000)
        self.text_scale_down.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.text_scale_down.setIcon(icon6)
        self.text_scale_down.setIconSize(QtCore.QSize(34, 34))
        self.text_scale_down.setShortcut("")
        self.text_scale_down.setCheckable(False)
        self.text_scale_down.setChecked(False)
        self.text_scale_down.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.text_scale_down.setObjectName("text_scale_down")
        self.horizontalLayout_3.addWidget(self.text_scale_down)
        self.horizontalLayout_2.addWidget(self.frame_top_left)
        self.frame_top_right = QtWidgets.QFrame(self.frame_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top_right.sizePolicy().hasHeightForWidth())
        self.frame_top_right.setSizePolicy(sizePolicy)
        self.frame_top_right.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_top_right.setMaximumSize(QtCore.QSize(450, 40))
        self.frame_top_right.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_top_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_top_right)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.progressBar = QLoadingProgressBar(self.frame_top_right)
        self.progressBar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.top_lable = QtWidgets.QLabel(self.frame_top_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_lable.sizePolicy().hasHeightForWidth())
        self.top_lable.setSizePolicy(sizePolicy)
        self.top_lable.setMinimumSize(QtCore.QSize(0, 0))
        self.top_lable.setMaximumSize(QtCore.QSize(16666, 16777215))
        self.top_lable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.top_lable.setObjectName("top_lable")
        self.horizontalLayout_6.addWidget(self.top_lable)
        self.horizontalLayout_2.addWidget(self.frame_top_right, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.frame_center)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame_center_left = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center_left.sizePolicy().hasHeightForWidth())
        self.frame_center_left.setSizePolicy(sizePolicy)
        self.frame_center_left.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_center_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center_left.setObjectName("frame_center_left")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_center_left)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listView_all = QFileListView(self.frame_center_left)
        self.listView_all.setObjectName("listView_all")
        self.verticalLayout_6.addWidget(self.listView_all)
        self.frame_center_center = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center_center.sizePolicy().hasHeightForWidth())
        self.frame_center_center.setSizePolicy(sizePolicy)
        self.frame_center_center.setMinimumSize(QtCore.QSize(380, 0))
        self.frame_center_center.setMaximumSize(QtCore.QSize(1677777, 16777215))
        self.frame_center_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center_center.setObjectName("frame_center_center")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_center_center)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_search = QtWidgets.QFrame(self.frame_center_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_search.sizePolicy().hasHeightForWidth())
        self.frame_search.setSizePolicy(sizePolicy)
        self.frame_search.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search.setObjectName("frame_search")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_search)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_search_left = QtWidgets.QFrame(self.frame_search)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_search_left.sizePolicy().hasHeightForWidth())
        self.frame_search_left.setSizePolicy(sizePolicy)
        self.frame_search_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search_left.setObjectName("frame_search_left")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_search_left)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.file_edit = QtWidgets.QLineEdit(self.frame_search_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_edit.sizePolicy().hasHeightForWidth())
        self.file_edit.setSizePolicy(sizePolicy)
        self.file_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.file_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.file_edit.setStyleSheet("font: 75 9pt \"微软雅黑\";\n"
"font: 12pt \"宋体\";")
        self.file_edit.setText("")
        self.file_edit.setObjectName("file_edit")
        self.verticalLayout_3.addWidget(self.file_edit)
        self.keywords_edit = QtWidgets.QLineEdit(self.frame_search_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keywords_edit.sizePolicy().hasHeightForWidth())
        self.keywords_edit.setSizePolicy(sizePolicy)
        self.keywords_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.keywords_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.keywords_edit.setStyleSheet("font: 12pt \"宋体\";")
        self.keywords_edit.setText("")
        self.keywords_edit.setObjectName("keywords_edit")
        self.verticalLayout_3.addWidget(self.keywords_edit)
        self.horizontalLayout_4.addWidget(self.frame_search_left)
        self.frame_search_right = QtWidgets.QFrame(self.frame_search)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_search_right.sizePolicy().hasHeightForWidth())
        self.frame_search_right.setSizePolicy(sizePolicy)
        self.frame_search_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search_right.setObjectName("frame_search_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_search_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.file_button = QtWidgets.QPushButton(self.frame_search_right)
        self.file_button.setMinimumSize(QtCore.QSize(0, 30))
        self.file_button.setMaximumSize(QtCore.QSize(70, 30))
        self.file_button.setObjectName("file_button")
        self.verticalLayout_4.addWidget(self.file_button)
        self.search_button = QtWidgets.QPushButton(self.frame_search_right)
        self.search_button.setMinimumSize(QtCore.QSize(0, 30))
        self.search_button.setMaximumSize(QtCore.QSize(70, 30))
        self.search_button.setObjectName("search_button")
        self.verticalLayout_4.addWidget(self.search_button)
        self.horizontalLayout_4.addWidget(self.frame_search_right)
        self.verticalLayout_2.addWidget(self.frame_search)
        self.frame_screen = QtWidgets.QFrame(self.frame_center_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_screen.sizePolicy().hasHeightForWidth())
        self.frame_screen.setSizePolicy(sizePolicy)
        self.frame_screen.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_screen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_screen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_screen.setObjectName("frame_screen")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_screen)
        self.horizontalLayout_8.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.frame_screen)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.comboBox = QComboCheckBox(self.frame_screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.verticalLayout_2.addWidget(self.frame_screen)
        self.splitter_2 = QtWidgets.QSplitter(self.frame_center_center)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(3)
        self.splitter_2.setObjectName("splitter_2")
        self.tableView = QFileTableView(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableView.setGridStyle(QtCore.Qt.NoPen)
        self.tableView.setWordWrap(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(300)
        self.tableView.horizontalHeader().setSortIndicatorShown(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.listView_error = QFileListView(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.listView_error.sizePolicy().hasHeightForWidth())
        self.listView_error.setSizePolicy(sizePolicy)
        self.listView_error.setObjectName("listView_error")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.frame_center_right = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center_right.sizePolicy().hasHeightForWidth())
        self.frame_center_right.setSizePolicy(sizePolicy)
        self.frame_center_right.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_center_right.setStyleSheet("")
        self.frame_center_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center_right.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_center_right.setObjectName("frame_center_right")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_center_right)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textframe = QTextFrame(self.frame_center_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textframe.sizePolicy().hasHeightForWidth())
        self.textframe.setSizePolicy(sizePolicy)
        self.textframe.setMinimumSize(QtCore.QSize(300, 0))
        self.textframe.setFrameShape(QtWidgets.QFrame.Box)
        self.textframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textframe.setObjectName("textframe")
        self.verticalLayout_7.addWidget(self.textframe)
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.frame_center)
        self.frame_bottom = QtWidgets.QFrame(self.frame)
        self.frame_bottom.setMinimumSize(QtCore.QSize(0, 16))
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_bottom.setFont(font)
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setLineWidth(0)
        self.frame_bottom.setObjectName("frame_bottom")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.show_error_button = QtWidgets.QPushButton(self.frame_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_error_button.sizePolicy().hasHeightForWidth())
        self.show_error_button.setSizePolicy(sizePolicy)
        self.show_error_button.setMaximumSize(QtCore.QSize(16, 16))
        self.show_error_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/提醒.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_error_button.setIcon(icon7)
        self.show_error_button.setIconSize(QtCore.QSize(13, 13))
        self.show_error_button.setObjectName("show_error_button")
        self.horizontalLayout_5.addWidget(self.show_error_button)
        self.bottom_lable = QtWidgets.QLabel(self.frame_bottom)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bottom_lable.setFont(font)
        self.bottom_lable.setObjectName("bottom_lable")
        self.horizontalLayout_5.addWidget(self.bottom_lable)
        self.verticalLayout.addWidget(self.frame_bottom)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_all_button.setToolTip(_translate("MainWindow", "显示全部"))
        self.show_all_button.setText(_translate("MainWindow", "显示全部"))
        self.help.setToolTip(_translate("MainWindow", "使用说明"))
        self.help.setText(_translate("MainWindow", "使用说明"))
        self.setting.setToolTip(_translate("MainWindow", "设置"))
        self.setting.setText(_translate("MainWindow", "软件设置"))
        self.update.setToolTip(_translate("MainWindow", "检查更新"))
        self.update.setText(_translate("MainWindow", "检查更新"))
        self.index_button.setToolTip(_translate("MainWindow", "建立索引"))
        self.index_button.setText(_translate("MainWindow", "建立索引"))
        self.text_scale_up.setToolTip(_translate("MainWindow", "放大"))
        self.text_scale_up.setText(_translate("MainWindow", "放大"))
        self.text_scale_down.setToolTip(_translate("MainWindow", "缩小"))
        self.text_scale_down.setText(_translate("MainWindow", "缩小"))
        self.top_lable.setText(_translate("MainWindow", "搜索就绪"))
        self.file_edit.setPlaceholderText(_translate("MainWindow", "请选择文件夹"))
        self.keywords_edit.setPlaceholderText(_translate("MainWindow", "请输入关键词，回车"))
        self.file_button.setText(_translate("MainWindow", "选择"))
        self.search_button.setText(_translate("MainWindow", "搜索"))
        self.label.setText(_translate("MainWindow", "类型：  "))
        self.show_error_button.setToolTip(_translate("MainWindow", "显示错误"))
        self.bottom_lable.setText(_translate("MainWindow", "准备就绪！"))
from qcombocheckbox import QComboCheckBox
from qfilelistview import QFileListView
from qfiletableview import QFileTableView
from qloadingprogressbar import QLoadingProgressBar
from qtextframe import QTextFrame
import icon_rc
