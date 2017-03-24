#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QNetworkReply>
#include <QMessageBox>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    worker(new HttpRequestWorker(this)),
    m_scene(new QGraphicsScene(this))
{

    ui->setupUi(this);

    //connect request worker to parser handle_result
    connect(worker, SIGNAL(on_execution_finished(HttpRequestWorker*, QString)), this, SLOT(handle_result(HttpRequestWorker*, QString)));

    //set url
    url_str  = "http://ec2-54-200-185-55.us-west-2.compute.amazonaws.com:8082/v3/";

    //set secene
    ui->view_field->setScene(m_scene);

    //initialize
    m_boundary = NULL;
    m_goal = NULL;
    m_obstacleList.clear();
    m_robotList.clear();
    m_pathList.clear();

}

MainWindow::~MainWindow() {
    delete ui;
}

QString MainWindow::getRequestType()
{
    QString requestType = "";
    switch(ui->combo_rqst_type->currentIndex()){
    case 0:
        requestType = "GET";
        break;
    case 1:
        requestType = "POST";
        break;
    case 2:
        requestType = "PUT";
        break;
    case 3:
        requestType = "DELETE";
        break;
    }
    return requestType;

}


void MainWindow::parseJson(QByteArray response)
{
    qDebug() << "1";
    QJsonArray tempArray;
    QJsonParseError error;
    QJsonDocument Jdoc = QJsonDocument::fromJson(response, &error);

    //qDebug() << "response: " << response;
    //qDebug() << "error: " << error.errorString();
    if(error.error != QJsonParseError::NoError || error.offset >= response.size()){
        QMessageBox::information(this, "", "Bad json from server");
        return;
    }

    QJsonObject JObject = Jdoc.object();
    QJsonArray JArray = Jdoc.array();

    switch(m_rqst){
    case PROBLEM:
        qDebug() << "2";
        if(JObject[boundary_str] != QJsonValue::Undefined)
            BoundaryScene(JObject[boundary_str].toObject());

        if(JObject[goal_str] != QJsonValue::Undefined)
            GoalScene(JObject[goal_str].toObject());

        if(JObject[obstacles_str] != QJsonValue::Undefined)
            ObstaclesScene(JObject[obstacles_str].toArray());

        if(JObject[robots_str] != QJsonValue::Undefined)
            RobotsScene(JObject[robots_str].toArray());

        if(JObject[path_str] != QJsonValue::Undefined)
            PathScene(JObject[path_str].toObject());
        break;
    case BOUNDARY:
        if(JObject[boundary_info_str] != QJsonValue::Undefined)
            BoundaryScene(JObject);
        break;
    case GOAL:
        if(JObject[coordinates_str] != QJsonValue::Undefined)
            GoalScene(JObject[goal_str].toObject());
        break;
    case OBSTACLES:
        if(JObject[coordinates_str] != QJsonValue::Undefined  && ui->rqst_oid->text() != ""){
            tempArray.append(JObject[obstacles_str].toObject());
            ObstaclesScene(tempArray);
        }else
            ObstaclesScene(JArray);

        break;
    case ROBOTS:
        if(JObject[coordinates_str] != QJsonValue::Undefined  && ui->rqst_rid->text() != ""){
            tempArray.append(JObject[robot_str].toObject());
            RobotsScene(tempArray);
        }else
            RobotsScene(JObject[robots_str].toArray());
        break;
    case PATH:
        if(JObject[coordinates_str] != QJsonValue::Undefined)
            PathScene(JObject);
        break;
    }
}

void MainWindow::getProblemId(QByteArray response)
{
    QJsonParseError error;
    QJsonDocument Jdoc = QJsonDocument::fromJson(response, &error);

    //qDebug() << "response: " << response;
    //qDebug() << "error: " << error.errorString();
    if(error.error != QJsonParseError::NoError || error.offset >= response.size()){
        QMessageBox::information(this, "", "Bad json from server");
        return;
    }

    QJsonObject JObject = Jdoc.object();
    QString temp = QString::number(JObject[problem_id_str].toInt());

    ui->cur_prob_id->setText(temp);
}

void MainWindow::BoundaryScene(QJsonObject update)
{
    qDebug() << "3";

    //remove old objects in display
    if(m_boundary != NULL)
        m_scene->removeItem(m_boundary);

    const QVector<QPointF> pointsList = getPointList(update[coordinates_str].toArray());

    QPolygonF boundary(pointsList);
    QRectF sizer = boundary.boundingRect();
    QPen color;
    color = QPen(Qt::black);
    color.setWidthF(sizer.height()/400);

    m_scene->setSceneRect(boundary.boundingRect());
    m_boundary = m_scene->addPolygon(boundary, color);

    ui->view_field->fitInView( m_scene->sceneRect(), Qt::KeepAspectRatio );

}

void MainWindow::ObstaclesScene(QJsonArray list)
{
    qDebug() << "4";
    //remove old obstacles
    int listSize = m_obstacleList.size();
    for(int i = 0; i < listSize; i++)
        m_scene->removeItem(m_obstacleList.at(i));
    m_obstacleList.clear();

    QPen color;
    color = QPen(Qt::black);

    QBrush fill;
    fill.setColor(Qt::blue);
    fill.setStyle(Qt::SolidPattern);

    for(int i = 0; i < list.size(); i++){
        QJsonObject temp = list[i].toObject();
        const QVector<QPointF> pointsList = getPointList(temp[coordinates_str].toArray());

        QPolygonF obstacle(pointsList);
        QGraphicsPolygonItem *ObstacleHandle = m_scene->addPolygon(obstacle, color, fill);
        m_obstacleList.append(ObstacleHandle);

    }

}

void MainWindow::GoalScene(QJsonObject update)
{
    qDebug() << "5";
    //remove old goal
    if(m_goal != NULL)
        m_scene->removeItem(m_goal);

    QRectF sizer = m_scene->itemsBoundingRect();
    QPen shp_color;
    shp_color = QPen(Qt::black);
    shp_color.setWidthF(sizer.height()/400);


    QBrush fill;
    fill.setColor(Qt::yellow);
    fill.setStyle(Qt::SolidPattern);

    QJsonObject coords = update[coordinates_str].toObject();

    m_goal = m_scene->addEllipse(coords[latitude_str].toDouble(),
                                 coords[longitude_str].toDouble(),
                                 sizer.height()/80,sizer.height()/80,
                                 shp_color, fill);
}

void MainWindow::RobotsScene(QJsonArray list)
{
    qDebug() << "6";
    //remove old robots
    int listSize = m_robotList.size();
    for(int i = 0; i < listSize; i++)
        m_scene->removeItem(m_robotList.at(i));
    m_robotList.clear();

    QRectF sizer = m_scene->itemsBoundingRect();
    QPen shp_color;
    shp_color = QPen(Qt::black);
    shp_color.setWidthF(sizer.height()/400);

    QBrush fill;
    fill.setColor(Qt::green);
    fill.setStyle(Qt::SolidPattern);

    for(int i = 0; i < list.size(); i++){
        QJsonObject temp = list[i].toObject();
        QJsonObject coords = temp[coordinates_str].toObject();

        QGraphicsEllipseItem *RobotHandle = m_scene->addEllipse(coords[latitude_str].toDouble(),
                                                                coords[longitude_str].toDouble(),
                                                                sizer.height()/80,sizer.height()/80,
                                                                shp_color, fill);
        m_robotList.append(RobotHandle);
    }

}

void MainWindow::PathScene(QJsonObject update)
{
    qDebug() << "7";
    //remove old path
    int listSize = m_pathList.size();
    for(int i = 0; i < listSize; i++)
        m_scene->removeItem(m_pathList.at(i));
    m_pathList.clear();

    QRectF sizer = m_scene->itemsBoundingRect();
    QPen color;
    color = QPen(Qt::darkRed);
    color.setWidthF(sizer.height()/200);

    const QVector<QPointF> pointsList = getPointList(update[coordinates_str].toArray());

    for(int i = 0; i < pointsList.size() - 1; i++){
        QLineF temp(pointsList.at(i), pointsList.at(i+1));

        QGraphicsLineItem *PathHandle = m_scene->addLine(temp, color);
        m_pathList.append(PathHandle);
    }
}

QVector<QPointF> MainWindow::getPointList(QJsonArray list)
{
    QVector<QPointF> points;

    for(int i = 0; i < list.size(); i++){
        QJsonObject temp = list[i].toObject();
        points.append(QPointF(temp[latitude_str].toDouble(), temp[longitude_str].toDouble()));
    }

    return points;
}



void MainWindow::handle_result(HttpRequestWorker *worker, QString StatusCode) {
   ui->status->setText("Got Response");
   ui->rpsn_code->setText(StatusCode);
      QString msg;

    if (worker->error_type == QNetworkReply::NoError) {
        // communication was successful
        msg = "Success - Response: " + worker->response;
    }
    else {
        // an error occurred
        msg = "Error: " + worker->error_str;

        return;
    }
    QMessageBox::information(this, "", msg);

    if(ui->rqst_uid->text() != "")
        ui->cur_prob_id->setText(ui->rqst_uid->text());

    //hopefully the user isnt fast enough to change the request type after sending out the request lol
    if(getRequestType() == "GET")
        parseJson(worker->response);
    else if(getRequestType() == "POST" && m_rqst == PROBLEM)
        getProblemId(worker->response);

}


void MainWindow::on_but_problem_clicked()
{
    qDebug() << "Problem clicked";
    QString json;
    QString requestType = getRequestType();
    QString url;

    if(requestType == "POST")
        url = url_str;
    else if(requestType == "GET")
        url = url_str + "id=" + ui->rqst_uid->text() + "/";
    else if(requestType == "DELETE")
        url = url_str + "id=" + ui->rqst_uid->text() + "/";
    else{
        QMessageBox::information(this, "", "Not A Valid Request");
        return;
    }

    json = "";

    HttpRequestInput input(url, requestType);

    input.add_json(json);
    worker->execute(&input);

    m_rqst = request::PROBLEM;
    ui->status->setText("Sent Request");
}

void MainWindow::on_but_boundary_clicked()
{
    QString json;
    QString requestType = getRequestType();
    QString url;

    if(requestType == "GET"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Boundary";
        json = "";
    }else if(requestType == "PUT"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Boundary";
        json = ui->rqst_body->toPlainText();
    }else{
        QMessageBox::information(this, "", "Not A Valid Request");
        return;
    }

    HttpRequestInput input(url, requestType);

    input.add_json(json);
    worker->execute(&input);

    m_rqst = request::BOUNDARY;
    ui->status->setText("Sent Request");
}

void MainWindow::on_but_goal_clicked()
{
    QString json;
    QString requestType = getRequestType();
    QString url;

    if(requestType == "GET"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Goal";
        json = "";
    }else if(requestType == "PUT"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Goal";
        json = ui->rqst_body->toPlainText();
    }else{
        QMessageBox::information(this, "", "Not A Valid Request");
        return;
    }

    HttpRequestInput input(url, requestType);

    input.add_json(json);
    worker->execute(&input);

    m_rqst = request::GOAL;
    ui->status->setText("Sent Request");
}

void MainWindow::on_but_obstacle_clicked()
{
    QString json;
    QString requestType = getRequestType();
    QString url;

    if(requestType == "GET" && ui->rqst_oid->text() == ""){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Obstacles";
        json = "";
    }else if(requestType == "GET"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Obstacles/obstacle_id=" + ui->rqst_oid->text();
        json = "";
    }else if(requestType == "DELETE"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Obstacles/obstacle_id=" + ui->rqst_oid->text();
        json = "";
    }else if(requestType == "PUT"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Obstacles/obstacle_id=" + ui->rqst_oid->text();
        json = ui->rqst_body->toPlainText();
    }else if(requestType == "POST"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Obstacles";
        json = ui->rqst_body->toPlainText();
    }else{
        QMessageBox::information(this, "", "Not A Valid Request");
        return;
    }

    HttpRequestInput input(url, requestType);

    input.add_json(json);
    worker->execute(&input);

    m_rqst = request::OBSTACLES;
    ui->status->setText("Sent Request");
}

void MainWindow::on_but_path_clicked()
{
    QString json;
    QString requestType = getRequestType();
    QString url;

    if(requestType == "GET"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Path";
        json = "";
    }else{
        QMessageBox::information(this, "", "Not A Valid Request");
        return;
    }

    HttpRequestInput input(url, requestType);

    input.add_json(json);
    worker->execute(&input);

    m_rqst = request::PATH;
    ui->status->setText("Sent Request");
}

void MainWindow::on_but_robot_clicked()
{
    QString json;
    QString requestType = getRequestType();
    QString url;

    if(requestType == "GET" && ui->rqst_rid->text() == ""){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Robot";
        json = "";
    }else if(requestType == "GET"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Robot/rid=" + ui->rqst_rid->text();
        json = "";
    }else if(requestType == "DELETE"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Robot/rid=" + ui->rqst_rid->text();
        json = "";
    }else if(requestType == "PUT"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Robot/rid=" + ui->rqst_rid->text();
        json = ui->rqst_body->toPlainText();
    }else if(requestType == "POST"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Robot";
        json = ui->rqst_body->toPlainText();
    }else{
        QMessageBox::information(this, "", "Not A Valid Request");
        return;
    }

    HttpRequestInput input(url, requestType);

    input.add_json(json);
    worker->execute(&input);

    m_rqst = request::ROBOTS;
    ui->status->setText("Sent Request");
}
