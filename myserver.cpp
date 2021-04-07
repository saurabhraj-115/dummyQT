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

}

void MyServer::onReadyRead(){
    qDebug()<<"Ready read called";
    QByteArray ba;
	ba =socket->readAll();
    qDebug()<<ba;
}
