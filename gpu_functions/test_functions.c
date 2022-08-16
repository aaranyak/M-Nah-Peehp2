#include <stdio.h>
#include "seek_codes.h"
int main(int argc, char const *argv[]) {
  /*
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
  */
  int board[8][8] = {
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,2,0,0,0},
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0},
  };
  int* rookTiles;
  rookTiles = getTiles(2, board);
  // if ((int)sizeof(rookTiles) / (int)sizeof(int) > 1) {
  //   for (size_t i = 0; i < (int)sizeof(rookTiles) / (int)sizeof(int); i+= 1) {
  //     printf("%d ", rookTiles[i]);
  //     printf("%d\n", rookTiles[i + 1]);
  //   }
  // }
  return 0;
}
