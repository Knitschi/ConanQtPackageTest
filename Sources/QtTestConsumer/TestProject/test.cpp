#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>

#include <iostream>

int main(int argc, char** argv)
{
    QApplication app(argc, argv);
    QMainWindow window;
    window.show();

    app.processEvents();

    std::cout << "The Qt TestConsumer worked!\n";
}