#include <iostream>
#include <iomanip>
#include <valarray>

#define set << setprecision(18)
using namespace std;

class Complex {
private:
    long double real, imag;
    valarray<long double>  number;
public:
    // Constructors
    Complex(long double a, long double b) {
        real = a; imag = b;
        valarray<long double>  number = {real, imag};
    }

    Complex() {
        real = 0.0L; imag = 0.0L;
        valarray<long double>  number = {real, imag};
    };

    // Operations on complex numbers
    Complex operator+ (const Complex& c1) {
        Complex c2;
        c2.real = this->real + c1.real;
        c2.imag = this->imag + c1.imag;
        return c2;
    }

    Complex operator- (const Complex& c1) {
        Complex c2;
        c2.real = this->real - c1.real;
        c2.imag = this->imag - c1.imag;
        return c2;
    }

    Complex operator* (const Complex& c1) {
        Complex c2;
        c2.real = (this->real * c1.real) - (this->imag * c1.imag);
        c2.imag = (this->imag * c1.real) + (this->real * c1.imag);
        return c2;
    }

    // Print the complex number
    friend ostream& operator<< (ostream& os, const Complex& c) {
        os << "(" << c.real << ", " << c.imag << ")";
        return os;
    }


};

class Polynomial {
    valarray<valarray<long double>> coeffs;
    // Constructor for Real Polynomials
    Polynomial(valarray<long double> input) {
        coeffs.resize(input.size());
        for (int i = 0; i < input.size(); i++) {
            coeffs[i] = valarray<long double> {input[i], 0.0L};
        }
    }
    // Constructor for Complex Polynomials
    Polynomial(valarray<valarray<long double>> input) {
        coeffs.resize(input.size());
        coeffs = input;
    }
    // Empty Constructor
    Polynomial() {
        coeffs.resize(1); coeffs[0] = valarray<long double> {0.0L, 0.0L};
    }
    void print_polynomial(Polynomial p) {
        cout << "{ ";
        for (int i = 0; i < p.coeffs.size() - 1; i++) {
            cout << "(" << p.coeffs[i][0] << ", " << p.coeffs[i][1] << "), ";
        }
    }
};

int main() {
    Complex num1 = Complex(2, 3);
    Complex num2 = Complex(4, 5);
    cout set << num1 * num2 << endl;
    cout << num1 << endl;
    cout << num2 << endl;
}


