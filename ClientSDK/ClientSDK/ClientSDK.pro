#-------------------------------------------------
#
# Project created by QtCreator 2017-03-21T12:12:54
#
#-------------------------------------------------

QT       += core gui
QT += network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = ClientSDK
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    httprequestworker.cpp

HEADERS  += mainwindow.h \
    httprequestworker.h \
    jsonkeys.h

FORMS    += mainwindow.ui
