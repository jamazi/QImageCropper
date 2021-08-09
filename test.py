from PyQt5.Qt import QApplication
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap

from QImageSelect import QImageSelect


def main(argv):
    import random

    app = QApplication(argv)

    if len(argv) > 1:
        sample = random.choice(argv[1:])
    else:
        sample = QPixmap(600, 400)
        sample.fill(random.choice([Qt.red, Qt.yellow, Qt.green, Qt.blue]))
    pixmap = QImageSelect.spawn(title="select image", image=sample, maximum_size=QSize(600, 400))
    if pixmap:
        QImageSelect.spawn(title="result", image=pixmap, maximum_size=QSize(200, 200))


if __name__ == "__main__":
    import sys

    main(sys.argv)
