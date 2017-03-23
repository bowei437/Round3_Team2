#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QJsonObject>
#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonParseError>
#include <QGraphicsRectItem>
#include <QGraphicsEllipseItem>
#include <QGraphicsScene>

#include "httprequestworker.h"
#include "jsonkeys.h"

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
    enum request{   PROBLEM,
                    BOUNDARY,
                    GOAL,
                    OBSTACLES,
                    PATH,
                    ROBOTS
                };

    Ui::MainWindow *ui;
    HttpRequestWorker *worker;

    QString getRequestType();
    QString url_str;
    request m_rqst;

    QGraphicsScene *m_scene;

    void parseJson(QByteArray response);
    void BoundaryScene(QJsonObject update);
    void ObstaclesScene(QJsonArray list);
    void GoalScene(QJsonObject update);
    void RobotsScene(QJsonArray list);
    void PathScene(QJsonObject update);

    //void resizeEvent(QResizeEvent *);
    QVector<QPointF> getPointList(QJsonArray list);
private slots:
    void POST_problem();
    void handle_result(HttpRequestWorker *worker, QString StatusCode);

    void on_but_problem_clicked();
    void on_but_boundary_clicked();
    void on_but_goal_clicked();
    void on_but_obstacle_clicked();
    void on_but_path_clicked();
    void on_but_robot_clicked();
};

#endif // MAINWINDOW_H
