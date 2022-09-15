#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


void func(const double& x, const double& par_a, const double& par_b);
void get_value(const double& par_a, const double& par_b, const double& lhs_edge, const double& rhs_edge, const int& steps);

int main() {
    int steps;
    double par_a, par_b, lhs_edge, rhs_edge;
  //  add some input
    vector<double> y(steps);
    y = get_value(par_a, par_b, lhs_edge, rhs_edge, steps);
  //  add some visualisation

    return 0;
}

void func(const double& phi, const double& par_a, double& x, double& y) {
  //  Ro = a * cos(3 * phi)
  //  x = Ro * cos(phi)
  //  y = Ro * sin(phi)
    return ;
}

void get_value(const double& par_a, const double& lhs_edge, const double& rhs_edge, const int& steps) {
    double phi = lhs_edge, step_size = (rhs_edge - lhs_edge) / steps;
    vector<double> y(steps);
    vector<double> x(steps);

    for (size_t i = 0; i < steps; ++i) {
        func(phi, par_a, x[i], y[i]);
        phi += step_size;
    }

    return y;
}
