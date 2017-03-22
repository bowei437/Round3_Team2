#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QNetworkReply>
#include <QMessageBox>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    worker(new HttpRequestWorker(this))
{

    ui->setupUi(this);

    //connect request worker to parser handle_result
    connect(worker, SIGNAL(on_execution_finished(HttpRequestWorker*)), this, SLOT(handle_result(HttpRequestWorker*)));

    //set url
    url_str  = "http://ec2-54-200-185-55.us-west-2.compute.amazonaws.com:8081/v3/";
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



void MainWindow::POST_problem() {




    //input.add_var("key1", "value1");
    //input.add_var("key2", "value2");
    //worker->execute(&input);
}

void MainWindow::handle_result(HttpRequestWorker *worker) {
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
}
