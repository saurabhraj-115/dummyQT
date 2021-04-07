#include "myserver.h"
#include <myserver.h>
#include <QTextStream>
#include <QIODevice>

MyServer::MyServer(QObject *parent) : QObject(parent)
{

    server = new QTcpServer(this);
    connect(server, SIGNAL(newConnection()), this, SLOT(newConnection() )  );
    
    if(!server->listen(QHostAddress::Any , 3232) ){
        qDebug()<<"Server could not start";
    }
    else{
        qDebug()<<"Server started";
    }
}

void MyServer::newConnection(){

    socket = server->nextPendingConnection();
    connect(socket, SIGNAL(readyRead() ) , this, SLOT(onReadyRead() ) );

    socket->write("hello client\r\n");
    socket->flush();

//    qDebug()<<server->listen(QHostAddress::Any,3232) ;
//    QTextStream ts( this );
//    QString str = ts.readLine();
//    qDebug()<<str;

    QByteArray totol_data, data_buffer;
    while(1) {
        data_buffer = socket->read(1024);
        qDebug()<<QString(data_buffer);
        if(data_buffer.isEmpty()) {
            break;
        }
        totol_data.append(data_buffer);
    }
    QString message_content(totol_data);
//    qDebug()<<totol_data;

//    socket->waitForBytesWritten(3000);
//    socket->close();



}

void MyServer::onReadyRead(){
    qDebug()<<"Ready read called";
}
