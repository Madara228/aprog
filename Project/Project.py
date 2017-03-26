import sys
from PIL import Image
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication,QDesktopWidget,QHBoxLayout
from PyQt5.QtWidgets import QLabel,QGridLayout,QLabel,qApp,QAction,QMainWindow,QFileDialog,QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon,QColor
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap


class MyWindow(QMainWindow):

	def __init__(self):
		super().__init__()

		self.initUI()


	def initUI(self):

		exitAction = QAction("&Выход", self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip("Выход")
		exitAction.triggered.connect(qApp.quit)

		openAction = QAction("&Открыть", self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip("Открытие")
		openAction.triggered.connect(self.openPhoto)
		self.statusBar()

		menu = self.menuBar()
		fileMenu = menu.addMenu("&Файл")
		fileMenu.addAction(exitAction)
		fileMenu.addAction(openAction)

		grid = QGridLayout()
		grid.setSpacing(60)


		self.question = QLabel()
		grid.addWidget(self.question,5,5)



		self.nextButton = QPushButton("Оттенок серого")
		self.nextButton.resize(self.nextButton.sizeHint())
		self.nextButton.move(1, 800)
		self.nextButton.clicked.connect(self.setFiltr_grown)


		btn = QPushButton('Просто кнопка', self)
		btn.resize(btn.sizeHint())
		btn.move(90, 800)  

		btn = QPushButton('', self)
		btn.resize(btn.sizeHint())
		btn.move(180, 800)



		pixmap = QPixmap("photo_edit_icon.png")

		self.lbl = QLabel(self)
		self.lbl.setPixmap(pixmap)
		
		self.setCentralWidget(self.lbl)

		self.move(500, 500)
		self.setWindowTitle('')
		self.setWindowIcon(QIcon('photo_edit_icon.png'))
		self.show()



	def closeEvent(self, event):

		reply = QMessageBox.question(self, 'Message',
		"Вы действительно хотите выйти??", QMessageBox.Yes |
		QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


	def openPhoto(self):
		fname = QFileDialog.getOpenFileName(self,'Открыть файл', '.')
		self.lbl.setPixmap(QPixmap(fname[0]))


	def setFiltr_grown():
		im = Image.open(fname +".jpg")

		pixels = im.load()

		x,y = im.size

		for i in range(x):
			for j in range(y):
				r = pixels[i, j][0]
				g = pixels[i, j][1]
				b = pixels[i, j][2]
				S = (r + g + b) // 3
				S = r,g,b


if __name__ == '__main__':

	app = QApplication(sys.argv)
	wi = MyWindow()
	sys.exit(app.exec_())