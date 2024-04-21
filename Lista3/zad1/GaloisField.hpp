#ifndef GALOIS_FIELD_HPP
#define GALOIS_FIELD_HPP

#include <optional>

template <typename T, T order>
class GaloisField {
 public:
  static T convertToFieldElement(T abnormalNumber) {
    while (abnormalNumber < 0) {
      abnormalNumber += order;
    }

    return abnormalNumber % order;
  }

  static T add(T summand1, T summand2) { return (summand1 + summand2) % order; }

  static T subtract(T minuend, T subtrahend) {
    return (minuend - subtrahend + order) % order;
  }

  static T multiply(T faktor1, T faktor2) {
    return (faktor1 * faktor2) % order;
  }

  static T opposite(T number) { return (-number + order) % order; }

  static std::optional<T> inverse(T number) {
    T x, y;
    T d = extendedGcd(number, order, x, y);
    if (d == 1) {
      return {(x % order + order) % order};
    }

    return std::nullopt;
  }

  static std::optional<T> divide(T dividend, T divisor) {
    auto divisorInverse = inverse(divisor);

    if (divisorInverse) {
      return multiply(dividend, *divisorInverse);
    }

    return std::nullopt;
  }

  static T power(T base, T exponent) {
    T result{1};

    while (exponent > 0) {
      if (exponent % 2 == 1) {
        result *= base;
        result %= order;
      }

      exponent /= 2;
      base *= base;
      base %= order;
    }

    return result;
  }

 private:
  static T extendedGcd(T a, T b, T& x, T& y) {
    T x0{1}, x1{0}, y0{0}, y1{1};

    while (b != 0) {
      T q = a / b;
      T temp = b;
      b = a % b;
      a = temp;

      T nextX = x0 - q * x1;
      T nextY = y0 - q * y1;

      x0 = x1;
      y0 = y1;
      x1 = nextX;
      y1 = nextY;
    }

    x = x0;
    y = y0;

    return a;
  }
};

#endif  // GALOIS_FIELD_HPP