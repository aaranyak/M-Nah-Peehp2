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
  int posY;
  int posX;
  int position[2];
  posY = position[0];
  posX = position[1];
  getPositionOfPiece(11, board, position);
  printf("%d\n", posY);
  printf("%d\n", posX);
  return 0;
}