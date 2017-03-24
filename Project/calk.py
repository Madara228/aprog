import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
	QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon


class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()


	def initUI(self):

		QToolTip.setFont(QFont('SansSerif', 10))

		self.setToolTip('This is a <b>QWidget</b> widget')

		btn = QPushButton('Просто кнопка', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(1, 1)

		btn = QPushButton('Просто кнопка', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(90, 1)	

		btn = QPushButton('Просто кнопка', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(180, 1)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('PhotoEditor')
		self.setWindowIcon(QIcon(''))
		self.show()


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())