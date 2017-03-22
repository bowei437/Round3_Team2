#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "httprequestworker.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;

private slots:
    void POST_problem();
    void handle_result(HttpRequestWorker *worker);

};

#endif // MAINWINDOW_H
