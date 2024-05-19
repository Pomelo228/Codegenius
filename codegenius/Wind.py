
import sys


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget,QFileDialog)
import donload
import cv2  # Для работы с изображениями
import numpy as np  # Для работы с массивами
class Ui_MainWindow(object):
    def download_action(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_path)
            self.okno.setPixmap(pixmap)
            self.okno.setScaledContents(True)
            # Загружаем изображение
            self.okno.setPixmap(pixmap)
        self.downloadButton.clicked.connect(self.download_action)# Устанавливаем изображение в виджет

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 614)
        MainWindow.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.5 rgba(0, 63, 0, 255));\n"
"font family:Noto Sans SC")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.okno = QLabel(self.centralwidget)
        self.okno.setObjectName(u"okno")
        self.okno.setGeometry(QRect(11, 11, 941, 511))
        self.okno.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.okno.setPixmap(QPixmap(u":/icon/icon/download_24dp_FILL0_wght400_GRAD0_opsz24.png"))
        self.okno.setScaledContents(False)
        self.okno.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.downloadButton = QPushButton(self.centralwidget)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setGeometry(QRect(210, 540, 181, 24))
        self.downloadButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(85, 255, 0);\n"
"font: 14pt \"Wide Latin\";")
        self.Deleit = QPushButton(self.centralwidget)
        self.Deleit.setObjectName(u"Deleit")
        self.Deleit.setGeometry(QRect(400, 540, 161, 24))
        self.Deleit.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(85, 255, 0);\n"
"font: 14pt \"Wide Latin\";")
        self.downloadButton.clicked.connect(self.download_action)
        self.Expect = QPushButton(self.centralwidget)
        self.Expect.setObjectName(u"Expect")
        self.Expect.setGeometry(QRect(570, 540, 381, 24))
        self.Expect.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(85, 255, 0);\n"
"font: 14pt \"Wide Latin\";")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(960, 20, 431, 141))
        self.frame.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"border-radius: 5px;\n"
"background-color: qradialgradient(spread:pad, cx:0.602273, cy:0.517, radius:0.518, fx:0.931184, fy:0.117494, stop:0 rgba(0, 0, 0, 255), stop:0.892045 rgba(85, 255, 0, 255));")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.semeistvo = QLineEdit(self.frame)
        self.semeistvo.setObjectName(u"semeistvo")
        self.semeistvo.setGeometry(QRect(10, 72, 395, 25))
        self.semeistvo.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(85, 255, 0);\n"
"font: 14pt \"Wide Latin\";")
        self.rod = QLineEdit(self.frame)
        self.rod.setObjectName(u"rod")
        self.rod.setGeometry(QRect(10, 41, 395, 25))
        self.rod.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(85, 255, 0);\n"
"font: 14pt \"Wide Latin\";")
        self.otrid = QLineEdit(self.frame)
        self.otrid.setObjectName(u"otrid")
        self.otrid.setGeometry(QRect(10, 103, 395, 25))
        self.otrid.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(85, 255, 0);\n"
"font: 14pt \"Wide Latin\";")
        self.klass = QLineEdit(self.frame)
        self.klass.setObjectName(u"klass")
        self.klass.setGeometry(QRect(10, 10, 395, 25))
        self.klass.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(85, 255, 0);\n"
"font: 14pt \"Wide Latin\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Classification of artiodactyls", None))
#if QT_CONFIG(tooltip)
        self.okno.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>srsfef</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.okno.setText("")
        self.downloadButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u043e\u0442\u043e", None))
        self.Deleit.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u043e\u0442\u043e ", None))
        self.Expect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043e\u0436\u0434\u0438\u0442\u0435 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438.....", None))
        self.semeistvo.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043c\u0435\u0439\u0441\u0442\u0432\u043e:", None))
        self.rod.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0434:", None))
        self.otrid.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u044f\u0434:", None))
        self.klass.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441:", None))
    # retranslateUi
    import cv2  # Для работы с изображениями
    import numpy as np  # Для работы с массивами

    # Функция для обработки изображения и передачи его на вход нейронной сети
    def process_image(image_path):
        image = cv2.imread(image_path)
        if image is not None:
            return image

        else:
            print("Ошибка при загрузке изображения")
        return None
        # Возвращаем результат

    # Обработчик кнопки для запуска обработки изображения
    def process_image_action(self):
        pixmap = self.okno.pixmap()  # Получаем pixmap из QLabel
        if pixmap is not None:
            pixmap.toImage().save("temp_image.jpg")  # Сохраняем pixmap как временное изображение
        processed_image = process_image("temp_image.jpg")  # Обрабатываем изображение
        processed_pixmap = QPixmap.fromImage(QImage(processed_image.data, processed_image.shape[1], processed_image.shape[0],processed_image.shape[1] * 3,QImage.Format_RGB888))
        self.okno.setPixmap(processed_pixmap)  # Отображаем обработанное изображение в okno

if __name__== "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
