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
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGraphicsView *graphicsView;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QPushButton *but_problem;
    QPushButton *but_boundary;
    QPushButton *but_goal;
    QPushButton *but_obstacle;
    QPushButton *but_path;
    QPushButton *but_robot;
    QLabel *label_rqst_body;
    QPlainTextEdit *rqst_body;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_cur_uid;
    QLabel *cur_uid;
    QHBoxLayout *horizontalLayout;
    QLabel *label_rpsn_code;
    QLabel *rpsn_code;
    QWidget *horizontalLayoutWidget_2;
    QHBoxLayout *horizontalLayout_2;
    QComboBox *combo_rqst_type;
    QLabel *label_rqst_uid;
    QLineEdit *rqst_uid;
    QLabel *label_rqst_oid;
    QLineEdit *rqst_oid;
    QLabel *label_rqts_rid;
    QLineEdit *rqst_rid;
    QMenuBar *menuBar;
    QMenu *menuGUI_Client_Pathfinding_Team_2;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(622, 524);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        graphicsView = new QGraphicsView(centralWidget);
        graphicsView->setObjectName(QStringLiteral("graphicsView"));
        graphicsView->setGeometry(QRect(20, 40, 461, 421));
        verticalLayoutWidget = new QWidget(centralWidget);
        verticalLayoutWidget->setObjectName(QStringLiteral("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(490, 40, 113, 421));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        but_problem = new QPushButton(verticalLayoutWidget);
        but_problem->setObjectName(QStringLiteral("but_problem"));

        verticalLayout->addWidget(but_problem);

        but_boundary = new QPushButton(verticalLayoutWidget);
        but_boundary->setObjectName(QStringLiteral("but_boundary"));

        verticalLayout->addWidget(but_boundary);

        but_goal = new QPushButton(verticalLayoutWidget);
        but_goal->setObjectName(QStringLiteral("but_goal"));

        verticalLayout->addWidget(but_goal);

        but_obstacle = new QPushButton(verticalLayoutWidget);
        but_obstacle->setObjectName(QStringLiteral("but_obstacle"));

        verticalLayout->addWidget(but_obstacle);

        but_path = new QPushButton(verticalLayoutWidget);
        but_path->setObjectName(QStringLiteral("but_path"));

        verticalLayout->addWidget(but_path);

        but_robot = new QPushButton(verticalLayoutWidget);
        but_robot->setObjectName(QStringLiteral("but_robot"));

        verticalLayout->addWidget(but_robot);

        label_rqst_body = new QLabel(verticalLayoutWidget);
        label_rqst_body->setObjectName(QStringLiteral("label_rqst_body"));

        verticalLayout->addWidget(label_rqst_body);

        rqst_body = new QPlainTextEdit(verticalLayoutWidget);
        rqst_body->setObjectName(QStringLiteral("rqst_body"));

        verticalLayout->addWidget(rqst_body);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        label_cur_uid = new QLabel(verticalLayoutWidget);
        label_cur_uid->setObjectName(QStringLiteral("label_cur_uid"));

        horizontalLayout_3->addWidget(label_cur_uid);

        cur_uid = new QLabel(verticalLayoutWidget);
        cur_uid->setObjectName(QStringLiteral("cur_uid"));

        horizontalLayout_3->addWidget(cur_uid);


        verticalLayout->addLayout(horizontalLayout_3);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        label_rpsn_code = new QLabel(verticalLayoutWidget);
        label_rpsn_code->setObjectName(QStringLiteral("label_rpsn_code"));

        horizontalLayout->addWidget(label_rpsn_code);

        rpsn_code = new QLabel(verticalLayoutWidget);
        rpsn_code->setObjectName(QStringLiteral("rpsn_code"));

        horizontalLayout->addWidget(rpsn_code);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayoutWidget_2 = new QWidget(centralWidget);
        horizontalLayoutWidget_2->setObjectName(QStringLiteral("horizontalLayoutWidget_2"));
        horizontalLayoutWidget_2->setGeometry(QRect(10, 0, 601, 31));
        horizontalLayout_2 = new QHBoxLayout(horizontalLayoutWidget_2);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        combo_rqst_type = new QComboBox(horizontalLayoutWidget_2);
        combo_rqst_type->setObjectName(QStringLiteral("combo_rqst_type"));

        horizontalLayout_2->addWidget(combo_rqst_type);

        label_rqst_uid = new QLabel(horizontalLayoutWidget_2);
        label_rqst_uid->setObjectName(QStringLiteral("label_rqst_uid"));

        horizontalLayout_2->addWidget(label_rqst_uid);

        rqst_uid = new QLineEdit(horizontalLayoutWidget_2);
        rqst_uid->setObjectName(QStringLiteral("rqst_uid"));

        horizontalLayout_2->addWidget(rqst_uid);

        label_rqst_oid = new QLabel(horizontalLayoutWidget_2);
        label_rqst_oid->setObjectName(QStringLiteral("label_rqst_oid"));

        horizontalLayout_2->addWidget(label_rqst_oid);

        rqst_oid = new QLineEdit(horizontalLayoutWidget_2);
        rqst_oid->setObjectName(QStringLiteral("rqst_oid"));

        horizontalLayout_2->addWidget(rqst_oid);

        label_rqts_rid = new QLabel(horizontalLayoutWidget_2);
        label_rqts_rid->setObjectName(QStringLiteral("label_rqts_rid"));

        horizontalLayout_2->addWidget(label_rqts_rid);

        rqst_rid = new QLineEdit(horizontalLayoutWidget_2);
        rqst_rid->setObjectName(QStringLiteral("rqst_rid"));

        horizontalLayout_2->addWidget(rqst_rid);

        MainWindow->setCentralWidget(centralWidget);
        graphicsView->raise();
        verticalLayoutWidget->raise();
        horizontalLayoutWidget_2->raise();
        label_rpsn_code->raise();
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 622, 20));
        menuGUI_Client_Pathfinding_Team_2 = new QMenu(menuBar);
        menuGUI_Client_Pathfinding_Team_2->setObjectName(QStringLiteral("menuGUI_Client_Pathfinding_Team_2"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuGUI_Client_Pathfinding_Team_2->menuAction());

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Large Scale Assignment 6", 0));
        but_problem->setText(QApplication::translate("MainWindow", "Problem", 0));
        but_boundary->setText(QApplication::translate("MainWindow", "Boundary", 0));
        but_goal->setText(QApplication::translate("MainWindow", "Goal", 0));
        but_obstacle->setText(QApplication::translate("MainWindow", "Obstacles", 0));
        but_path->setText(QApplication::translate("MainWindow", "Path", 0));
        but_robot->setText(QApplication::translate("MainWindow", "Robot", 0));
        label_rqst_body->setText(QApplication::translate("MainWindow", "Request Body:", 0));
        label_cur_uid->setText(QApplication::translate("MainWindow", "Current Uid:", 0));
        cur_uid->setText(QApplication::translate("MainWindow", "####", 0));
        label_rpsn_code->setText(QApplication::translate("MainWindow", "Response Code:", 0));
        rpsn_code->setText(QApplication::translate("MainWindow", "###", 0));
        combo_rqst_type->clear();
        combo_rqst_type->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "GET", 0)
         << QApplication::translate("MainWindow", "POST", 0)
         << QApplication::translate("MainWindow", "PUT", 0)
         << QApplication::translate("MainWindow", "DELETE", 0)
        );
        label_rqst_uid->setText(QApplication::translate("MainWindow", "Request Uid:", 0));
        label_rqst_oid->setText(QApplication::translate("MainWindow", "Request Obstacle id: ", 0));
        label_rqts_rid->setText(QApplication::translate("MainWindow", "Request Robot id: ", 0));
        menuGUI_Client_Pathfinding_Team_2->setTitle(QApplication::translate("MainWindow", "GUI Client Pathfinding Team 2", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
