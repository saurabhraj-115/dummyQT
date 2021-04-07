#ifndef MYSERVER_H
#define MYSERVER_H

#include <QObject>
#include <QDebug>
#include <QTcpServer>
#include <QTcpSocket>
#include <QAbstractSocket>
#include <QIODevice>

class MyServer : public QObject
{
    Q_OBJECT
public:
    explicit MyServer(QObject *parent = 0);

signals:
  void readyRead();


public slots:
    void newConnection();
    void onReadyRead();



private:
    QTcpServer *server;
    QAbstractSocket *socket;

};

#endif // MYSERVER_H
