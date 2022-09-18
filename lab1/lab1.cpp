#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


void func(const double& par_a, double& x, double& y);
void get_value(const double& par_a, const double& lhs_edge, const double& rhs_edge, const int& steps, vector<double>& y, vector<double>& x);
void show_plot(const vector<double>& y, const vector<double>& x);

int main() {
    int steps;
    double par_a, par_b, lhs_edge, rhs_edge;
  //  add some input
    vector<double> y(steps);
    vector<double> x(steps);
    get_value(par_a, lhs_edge, rhs_edge, steps, y, x);
  //  add some visualisation
    show_plot(y, x);
    return 0;
}

void func(const double& phi, const double& par_a, double& x, double& y) {
  //  Ro = a * cos(3 * phi)
  //  Ro ^ 2 = x^2 + y^2 && Ro *  a * cos(3 * phi) = x
  //  x ^
  //  x = Ro * cos(phi)
  //  y = Ro * sin(phi)
    double Ro = par_a * cos(3 * phi); // check insides of cos
    x = Ro * cos(3 * phi);
    y = Ro * sin(3 * phi);

}

void get_value(const double& par_a, const double& lhs_edge, const double& rhs_edge, const int& steps, vector<double>& y, vector<double>& x) {
    double phi = lhs_edge, step_size = (rhs_edge - lhs_edge) / steps;
    vector<double> y(steps);
    vector<double> x(steps);

    for (size_t i = 0; i < steps; ++i) {
        func(phi, par_a, &(x[i]), &(y[i]));  //  not sure about ampersands
        phi += step_size;
    }
}
void show_plot(const vector<double>& y, const vector<double>& x) {
  //  TODO
}
