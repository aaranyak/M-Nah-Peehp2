#include <stdio.h>
#include "seek_codes.h"
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
  int *tiles = getTiles(2, board);
  int position;
  getPositionOfPiece(2, board, position);
  printf("%d\n", position[0]);
  return 0;
}
