#include <iostream>
#include <string>
#include <iomanip>
#include <cmath> // For abs function

using namespace std;
#define E 0.01

double func(double x)
{
    return x * x - 2;
}

void bisection(double a, double b)
{
    int count = 1;
    if (func(a) * func(b) >= 0)
    {
        cout << "You have not assumed the right a and b\n";
        return;
    }

    double c;
    while ((b - a) >= E)
    {
        c = (a + b) / 2;

        // Print current iteration and the midpoint
        cout << "Iteration " << setw(2) << count << ": c = " << setw(10) << c << ", f(c) = " << setw(10) << func(c) << endl;

        if (func(c) == 0.0)
            break;

        if (func(c) * func(a) < 0)
            b = c;
        else
            a = c;
        
        count++;
    }
    cout << "The value of root is: " << c << endl;
}

int main()
{
    double a, b;
    char response;

    do {
        cout << "Enter first guess: ";
        cin >> a;
        cout << "You entered: " << a << endl;
        cout << "Enter second guess: ";
        cin >> b;
        cout << "You entered: " << b << endl;

        bisection(a, b);

        cout << "Do you want to try again? (y/n): ";
        cin >> response;
    } while (response == 'y');

    return 0;
}


