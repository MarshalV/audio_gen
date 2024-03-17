  
button_style_1 = """
        QPushButton {
    padding: 0 1px 0 1px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB28B, stop:1 #FFB28B); 
    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #FFB28B, stop:1 #FFB28B);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #FFB28B, stop:1 #FFB28B);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #FFB28B, stop:1 #FFB28B);
    border-width: 0px;
    border-radius: 10px;
    color: #0a0a0a;
    font-weight: Catallina;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #e9f5db, stop:0.5 #e9f5db, stop:1 #e9f5db);
}

QPushButton:hover {
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #edeec9, stop:0.5 #edeec9, stop:1 #edeec9);
    border-color: #fffafa;
}
        """
    
button_style_2 = """
        QPushButton {
    padding: 0 1px 0 1px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FFB28B, stop:1 #FFB28B); 
    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #FFB28B, stop:1 #FFB28B);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #FFB28B, stop:1 #FFB28B);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #FFB28B, stop:1 #FFB28B);
    border-width: 0px;
    border-radius: 10px;
    color: #0a0a0a;
    font-weight: Catallina;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #cfe1b9, stop:0.5 #cfe1b9, stop:1 #cfe1b9);
}

QPushButton:hover {
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #edeec9, stop:0.5 #edeec9, stop:1 #edeec9);
    border-color: #fffafa;
}
        """
    
button_style_3 = """
        QPushButton {
    padding: 0 1px 0 1px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0a0a0a, stop:1 #0a0a0a); 
    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #0a0a0a, stop:1 #0a0a0a);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #0a0a0a, stop:1 #0a0a0a);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0a0a0a, stop:1 #0a0a0a);
    border-width: 0px;
    border-radius: 10px;
    color: #0a0a0a;
    font-weight: Catallina;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #b5c99a, stop:0.5 #b5c99a, stop:1 #b5c99a);
}

QPushButton:hover {
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #edeec9, stop:0.5 #edeec9, stop:1 #edeec9);
    border-color: #fffafa;
}
        """
    
Combo_style_L = """
        QComboBox {
    border: 1px solid #b5c99a;
    border-radius: 10px;
    padding: 1px 3px 1px 3px;
    min-width: 6em;
    background: #cfe1b9;
    selection-background-color: #d3d3d3;
}

QComboBox:editable {
    background: white;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: right top;
    width: 15px;

    border-left-width: 1px;
    border-left-color: #b5c99a;
    border-left-style: solid;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
}

QComboBox::down-arrow {
    image: url(:/path/to/your/arrow-down.png);
}

QComboBox::down-arrow:on {
    /* shift the arrow when pressed */
    top: 1px;
    left: 1px;
}

QComboBox QAbstractItemView {
    border: 1px solid #b5c99a;
    selection-background-color: #cfe1b9;
}
        """
      
LineEdit_style_L =  """
    QLineEdit {
    border: 1px solid #b5c99a;
    border-radius: 8px;
    padding: 2px;
    background-color: #cfe1b9;
    selection-background-color: #d3d3d3;
}

QLineEdit:focus {
    border: 2px solid #e9f5db;
}

QLineEdit::hover {
    border: 1px solid #e9f5db;
}

QLineEdit:disabled {
    background-color: #e9f5db;
    color: #a0a0a0;
}

QLineEdit::placeholder {
    color: #a0a0a0;
}

QLineEdit QToolTip {
    border: 1px solid #4a90e2;
    background-color: #cfe1b9;
    color: #333333;
}"""
    
QFrame_style_L = """
    QFrame {
    background-color: #b5c99a;
    border: 1px solid #97a97c;
    border-radius: 5px;
    padding: 1px;
}

QFrame:hover {
    border: 1px solid #97a97c;
}

QFrame::disabled {
    background-color: #d9d9d9;
    color: #97a97c;
}

QFrame QToolTip {
    border: 1px solid #4a90e2;
    background-color: #fffafa;
    color: #97a97c;
}"""
    
TableWidget_style_L = """
    QTabWidget {
    background-color: #cfe1b9;
    border: 1px solid #b5c99a;
    border-radius: 5px;
}

QTabBar::tab {
    background-color: #cfe1b9;
    color: #0a0a0a;
    padding: 8px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}

QTabBar::tab:selected {
    background-color: #b5c99a;
    color: #0a0a0a;
    border-bottom: 1px solid #4a90e2;
}

QTabWidget::pane {
    border: 1px solid #87986a;
    border-top: none;
}

QTabWidget QToolTip {
    border: 1px solid #4a90e2;
    background-color: #cfe1b9;
    color: #0a0a0a;
}

QTabWidget QLabel {
    color: #0a0a0a;
    font-family:Catallina, sans-serif; /* Пример установки шрифта */
    font-size: 12px; /* Пример установки размера шрифта */
}"""
    
QWidget_style_L = """
    QWidget {
    background-color: #E6E6FA;
    color: #333333;}

"""
    
QWidget_style_3 = """
    QWidget {
    background-color: #97A97C;
    color: #97A97C;}

"""
    
QTextEdit_style_L = """
    QTextEdit {
    background-color: #e9f5db;
    color: #333333;
    border: 1px solid #cfe1b9;
    border-radius: 8px;
    font-family: PoiretOne, sans-serif;
    font-size: 14px;
}

QTextEdit QToolTip {
    border: 1px solid #4a90e2;
    background-color: #cfe1b9;
    color: #333333;
}"""
    
Qline_style_L = """
QLabel {
    color: #000000;
    font-family: PoiretOne, sans-serif;
    font-size: 12px;
    background: transparent;
    border: none;
}


QLabel QToolTip {
    border: 1px solid #4a90e2;
    background-color: #f5f5f5;
    color: #333333;
}"""

CheckBox_style = """
QCheckBox {
    spacing: 2px;
    color: #333333;
    background: transparent;
}

QCheckBox::indicator {
    width: 12px;
    height: 12px;
    border-radius: 6px; /* Половина ширины/высоты для создания круглого чекбокса */
}

QCheckBox::indicator:checked {
    background-color: #b5c99a; /* Цвет фона для отмеченного состояния */
    border: 1px solid #b5c99a; /* Цвет границы для отмеченного состояния */
}

QCheckBox::indicator:unchecked {
    background-color: transparent; /* Прозрачный фон для неотмеченного состояния */
    border: 1px solid #97a97c; /* Цвет границы для неотмеченного состояния */
}

QCheckBox:hover {
    color: #b5c99a;
}

QCheckBox:disabled {
    color: #a0a0a0;
}

QCheckBox QToolTip {
    border: 1px solid #4a90e2;
    background-color: #f5f5f5;
    color: #333333;
}
"""

ScrollArea_style = """
QScrollArea {
    background: #e9f5db;
    border: 1px solid #cfe1b9;
    border-radius: 8px; /* Закругленные углы */
}

QScrollBar:vertical {
    border: none;
    background: #e9f5db;
    width: 10px;
    margin: 0px 1px 0px 1px;
    border-radius: 10px; /* Закругленные полосы прокрутки */
}

QScrollBar::handle:vertical {
    background: #87986a;
    border-radius: 8px;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    border: none;
    background: #e9f5db;
    height: 10px;
    margin: 1px 0px 1px 0px;
    border-radius: 10px; /* Закругленные полосы прокрутки */
}

QScrollBar::handle:horizontal {
    background: #87986a;
    border-radius: 8px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0px;
}

QScrollArea QWidget {
    background: transparent;
}

QScrollArea QToolTip {
    border: 1px solid #718355;
    background-color: #87986a;
    color: #333333;
}"""

QTableView_style = """
QTableView {
    background-color: #cfe1b9;
    border: 1px solid #97a97c;
    border-radius: 8px; /* Закругленные углы */
}

QTableView::item {
    padding: 2px;
    border-bottom: 1px solid #e9f5db;
}

QTableView::item:selected {
    background-color: #b5c99a;
    color: #ffffff;
}

QHeaderView:section {
    background-color: #b5c99a;
    color: #ffffff;
    padding: 2px;
    border-top-left-radius: 4px; /* Закругленные углы в заголовках */
    border-top-right-radius: 4px;
}

QTableView QToolTip {
    border: 1px solid #b5c99a;
    background-color: #cfe1b9;
    color: #333333;
}"""

QToolTip_style = """QToolTip {
    border: 1px solid #4a90e2;
    background-color: #f5f5f5;
    color: #333333;
    border-radius: 5px; /* Закругленные углы */
    padding: 5px;
}"""

QTreeWidget_style = """QTreeWidget {
    background-color: #e9f5db;
    border: 1px solid #718355;
    border-radius: 8px; /* Закругленные углы */
}

QTreeWidget::item {
    padding: 5px;
    border-bottom: 1px solid #d3d3d3;
}

QTreeWidget::item:selected {
    background-color: #97a97c;
    color: #ffffff;
}

QTreeWidget::branch:closed,
QTreeWidget::branch:open {
    image: url(:/path/to/your/branch.png); /* Укажите путь к изображению для развернутого и свернутого элемента */
}

QHeaderView:section {
    background-color: #97a97c;
    color: #ffffff;
    padding: 5px;
    border-top-left-radius: 5px; /* Закругленные углы в заголовках */
    border-top-right-radius: 5px;
}

QTreeWidget QToolTip {
    border: 1px solid #4a90e2;
    background-color: #f5f5f5;
    color: #333333;
}"""

QSlider_style = """QSlider {
    border: none;
    background: #f5f5f5;
    height: 10px;
    border-radius: 5px; /* Закругленные углы */
}

QSlider::groove:horizontal {
    background: #d3d3d3;
    border-radius: 5px; /* Закругленные углы для грува */
}

QSlider::handle:horizontal {
    background: #4a90e2;
    width: 14px;
    height: 14px;
    border-radius: 7px; /* Закругленные углы для ползунка */
}

QSlider::add-page:horizontal {
    background: #4a90e2;
    border-radius: 5px; /* Закругленные углы для залитой части грува */
}

QSlider::sub-page:horizontal {
    background: #d3d3d3;
    border-radius: 5px; /* Закругленные углы для оставшейся части грува */
}

QSlider:disabled {
    background: #d9d9d9;
}

QSlider QToolTip {
    border: 1px solid #4a90e2;
    background-color: #f5f5f5;
    color: #333333;
}"""














