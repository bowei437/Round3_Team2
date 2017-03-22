/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QPushButton *but1;
    QLineEdit *uid;
    QGraphicsView *graphicsView;
    QLabel *statuslabel;
    QLabel *response;
    QLabel *uidlabel;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(483, 496);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        but1 = new QPushButton(centralWidget);
        but1->setObjectName(QStringLiteral("but1"));
        but1->setGeometry(QRect(380, 40, 80, 21));
        uid = new QLineEdit(centralWidget);
        uid->setObjectName(QStringLiteral("uid"));
        uid->setGeometry(QRect(30, 10, 113, 21));
        graphicsView = new QGraphicsView(centralWidget);
        graphicsView->setObjectName(QStringLiteral("graphicsView"));
        graphicsView->setGeometry(QRect(10, 40, 361, 321));
        statuslabel = new QLabel(centralWidget);
        statuslabel->setObjectName(QStringLiteral("statuslabel"));
        statuslabel->setGeometry(QRect(10, 370, 91, 16));
        response = new QLabel(centralWidget);
        response->setObjectName(QStringLiteral("response"));
        response->setGeometry(QRect(10, 390, 461, 51));
        uidlabel = new QLabel(centralWidget);
        uidlabel->setObjectName(QStringLiteral("uidlabel"));
        uidlabel->setGeometry(QRect(10, 10, 21, 16));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 483, 20));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0));
        but1->setText(QApplication::translate("MainWindow", "POST_problem", 0));
        statuslabel->setText(QApplication::translate("MainWindow", "Response Status:", 0));
        response->setText(QApplication::translate("MainWindow", "TextLabel", 0));
        uidlabel->setText(QApplication::translate("MainWindow", "Uid:", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
