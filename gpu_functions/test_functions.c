#include <stdio.h>
#include "utilfuncs.h"
int main(int argc, char const *argv[]) {
  int board[8][8] = {
    {1,2,3,4,5,6,7,8},
    {9,10,11,12,13,14,15,16},
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0},
    {32,31,30,29,28,27,26,25},
    {24,23,22,20,21,19,18,17},
  };
  int newtester = testarrayer();
  for (size_t y = 0; y < 8; y++) {
    for (size_t x = 0; x < 8; x++) {
      printf("%d", newtester[y][x]);
      printf("%s", " ");
    }
    printf("%s", "\n");
  }
  return 0;
}

int testarrayer() {
  int b[8][8];
  return b;
}
