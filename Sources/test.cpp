#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>

#include <iostream>

int main(int argc, char** argv)
{
    try
    {
        QApplication app(argc, argv);
        QMainWindow window;
        window.show();

        app.processEvents();

        std::cout << "The Qt TestConsumer worked!\n";
        return 0;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    catch(...)
    {
        std::cerr << "Unknown exception!") << '\n';
    }

    return 1;
}