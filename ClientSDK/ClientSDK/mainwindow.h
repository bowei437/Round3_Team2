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
    HttpRequestWorker *worker;

    QString getRequestType();
    QString url_str;

private slots:
    void POST_problem();
    void handle_result(HttpRequestWorker *worker);

    void on_but_problem_clicked();
    void on_but_boundary_clicked();
    void on_but_goal_clicked();
    void on_but_obstacle_clicked();
    void on_but_path_clicked();
    void on_but_robot_clicked();
};

#endif // MAINWINDOW_H
