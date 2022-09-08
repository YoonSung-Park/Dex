#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  int fopn, sopn;
  bool endf = false;
  while (!endf) {
    cin >> fopn >> sopn;
    cout << fopn + sopn << "\n" << flush;
    if (fopn == 0 || sopn == 0) {
      endf = true;
    }
  }
  return 0;
}