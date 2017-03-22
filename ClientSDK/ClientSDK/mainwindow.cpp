#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QNetworkReply>
#include <QMessageBox>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->but1, SIGNAL(clicked()), this, SLOT(POST_problem()));
}

MainWindow::~MainWindow() {
    delete ui;
}

/*void MainWindow::on_pushButton_clicked() {
    QString url_str = "http://ec2-54-200-185-55.us-west-2.compute.amazonaws.com:8081/v3/";

    HttpRequestInput input(url_str, "POST");

    HttpRequestWorker *worker = new HttpRequestWorker(this);
    connect(worker, SIGNAL(on_execution_finished(HttpRequestWorker*)), this, SLOT(handle_result(HttpRequestWorker*)));
    worker->execute(&input);
}*/

void MainWindow::POST_problem() {
    QString url_str = "http://ec2-54-200-185-55.us-west-2.compute.amazonaws.com:8081/v3/";

    HttpRequestInput input(url_str, "POST");

    //input.add_var("key1", "value1");
    //input.add_var("key2", "value2");

    HttpRequestWorker *worker = new HttpRequestWorker(this);
    connect(worker, SIGNAL(on_execution_finished(HttpRequestWorker*)), this, SLOT(handle_result(HttpRequestWorker*)));
    worker->execute(&input);
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

