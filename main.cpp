#include <QCoreApplication>
#include <myserver.h>
#include <QIODevice>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    MyServer mServer;

    return a.exec();
}
