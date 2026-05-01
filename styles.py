# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
from qt_material import apply_stylesheet
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR)

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme(app):
    apply_stylesheet(
        app, 
        theme='dark_teal.xml',
        invert_secondary=True,
        extra={
            'primaryColor': PRIMARY_COLOR,
            'primaryLightColor': DARKER_PRIMARY_COLOR,
            'secondaryColor': DARKEST_PRIMARY_COLOR,
        }
    )

    app.setStyleSheet(app.styleSheet() + qss)