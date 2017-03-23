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
    url_str  = "http://ec2-54-200-185-55.us-west-2.compute.amazonaws.com:8081/v3/";

    //set secene
    ui->view_field->setScene(m_scene);

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

//TODO change *_info to coordinates
void MainWindow::parseJson(QByteArray response)
{
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
        if(JObject[boundary_str] != QJsonValue::Undefined)
            BoundaryScene(JObject[boundary_str].toObject());

        if(JObject[goal_str] != QJsonValue::Undefined)
            GoalScene(JObject[goal_str].toObject());

        if(JObject[obstacles_str] != QJsonValue::Undefined)
            ObstaclesScene(JObject[obstacles_str].toArray());

        if(JObject[robots_str] != QJsonValue::Undefined)
            RobotsScene(JObject[robots_str].toArray());
        break;
    case BOUNDARY:
        if(JObject[boundary_info_str] != QJsonValue::Undefined)
            BoundaryScene(JObject);
        break;
    case GOAL:
        if(JObject[coordinates_str] != QJsonValue::Undefined)
            GoalScene(JObject);
        break;
    case OBSTACLES:
        if(JObject[coordinates_str] != QJsonValue::Undefined  && ui->rqst_oid->text() == ""){
            tempArray.append(JObject);
            ObstaclesScene(tempArray);
        }else
            ObstaclesScene(JArray);
        break;
    case ROBOTS:
        if(JObject[coordinates_str] != QJsonValue::Undefined  && ui->rqst_rid->text() == ""){
            tempArray.append(JObject);
            RobotsScene(tempArray);
        }else
            ObstaclesScene(JArray);
        break;
    case PATH:
        if(JObject[coordinates_str] != QJsonValue::Undefined)
            PathScene(JObject);
        break;
    }
}

void MainWindow::BoundaryScene(QJsonObject update)
{
    if(update[shape_str].toString() == "string") //no defaults
        return;

    const QVector<QPointF> pointsList = getPointList(update[boundary_info_str].toArray());

    QPolygonF boundary(pointsList);

    QPen color;
    color = QPen(Qt::black);

   /* QPointF topleft(-500,-500);
    QPointF bottomright(0,0);
    QRectF sceneRect(topleft, bottomright);

    QPointF topleft2(-475,-475);
    QPointF bottomright2(-25,-25);
    QRectF viewRect(topleft2, bottomright2);

    m_scene->setSceneRect(sceneRect);
    m_scene->addRect(viewRect);*/

    m_scene->setSceneRect(boundary.boundingRect());
    m_scene->addPolygon(boundary, color);

    ui->view_field->fitInView( m_scene->sceneRect(), Qt::KeepAspectRatio );

}

void MainWindow::ObstaclesScene(QJsonArray list)
{
    QPen color;
    color = QPen(Qt::black);

    QBrush fill;
    fill.setColor(Qt::blue);
    fill.setStyle(Qt::SolidPattern);

    for(int i = 0; i < list.size(); i++){
        QJsonObject temp = list[i].toObject();
        const QVector<QPointF> pointsList = getPointList(temp[obstacle_info_str].toArray());

        QPolygonF obstacle(pointsList);
        m_scene->addPolygon(obstacle, color, fill);

    }

}

void MainWindow::GoalScene(QJsonObject update)
{
    QPen shp_color;
    shp_color = QPen(Qt::black);


    QBrush fill;
    fill.setColor(Qt::yellow);
    fill.setStyle(Qt::SolidPattern);

    m_scene->addEllipse(-40,-460,5,5,shp_color, fill);
}

void MainWindow::RobotsScene(QJsonArray list)
{

    QPen shp_color;
    shp_color = QPen(Qt::black);


    QBrush fill;
    fill.setColor(Qt::green);
    fill.setStyle(Qt::SolidPattern);

    m_scene->addEllipse(-460,-40,5,5,shp_color, fill);

}

void MainWindow::PathScene(QJsonObject update)
{
    QPen color;
    color = QPen(Qt::black);

    m_scene->addLine(-460, -40, -400, -400, color);
    m_scene->addLine(-400, -400, -40, -460, color);
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


/*void MainWindow::resizeEvent(QResizeEvent *) {

    qDebug() << "resize event called";
    QRectF bounds = m_scene->itemsBoundingRect();
    bounds.setWidth(bounds.width()*0.9);         // to tighten-up margins
    bounds.setHeight(bounds.height()*0.9);       // same as above
    ui->view_field->fitInView(bounds, Qt::KeepAspectRatio);
    ui->view_field->centerOn(0, 0);
}*/

void MainWindow::POST_problem() {




    //input.add_var("key1", "value1");
    //input.add_var("key2", "value2");
    //worker->execute(&input);
}

void MainWindow::handle_result(HttpRequestWorker *worker, QString StatusCode) {
   ui->rpsn_code->setText(StatusCode);
      QString msg;

    if (worker->error_type == QNetworkReply::NoError) {
        // communication was successful
        msg = "Success - Response: " + worker->response;
    }
    else {
        // an error occurred
        msg = "Error: " + worker->error_str;
    }


    QMessageBox::information(this, "", msg);


    //hopefully the user isnt fast enough to change the request type after sending out the request lol
    if(getRequestType() == "GET")
        parseJson(worker->response);
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
        url = url_str + "id=" + ui->rqst_uid->text() + "/Boundary/ver=" + ui->rqst_rid->text()+ "/";
        json = ui->rqst_body->toPlainText();
    }else{
        QMessageBox::information(this, "", "Not A Valid Request");
        return;
    }

    HttpRequestInput input(url, requestType);

    input.add_json(json);
    worker->execute(&input);

    m_rqst = request::BOUNDARY;
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
        url = url_str + "id=" + ui->rqst_uid->text() + "/Obstacles/obstacle_id=" + ui->rqst_oid->text() + "ver=" + ui->rqst_rid->text()+ "/";
        json = ui->rqst_body->toPlainText();
    }else if(requestType == "POST"){
        url = url_str + "id=" + ui->rqst_uid->text() + "/Obstacles/ver=" + ui->rqst_rid->text()+ "/";
        json = ui->rqst_body->toPlainText();
    }else{
        QMessageBox::information(this, "", "Not A Valid Request");
        return;
    }

    HttpRequestInput input(url, requestType);

    input.add_json(json);
    worker->execute(&input);

    m_rqst = request::OBSTACLES;
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
}

void MainWindow::on_but_robot_clicked()
{
    QString json;
    QString requestType = getRequestType();
    QString url;

    if(requestType == "GET" && ui->rqst_oid->text() == ""){
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
}
