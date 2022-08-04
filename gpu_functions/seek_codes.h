#include "utilfuncs.h"
#include <stdlib.h>
int *getKnightTiles(int piece, int board[8][8]) {
  int *retTiles = malloc(8 * sizeof(int)); // Allocate memory for the tiles.
  int posX;
  int posY;
  getPositionOfPiece(piece, board, posX, posY);
  int unfilteredPattern[8][2] = {
    {posY + 1, posX + 2},
    {posY + 2, posX + 1},
    {posY - 1, posX - 2},
    {posY - 2, posX - 1},
    {posY + 1, posX - 2},
    {posY - 2, posX + 1},
    {posY - 1, posX + 2},
    {posY + 2, posX - 1},
  }; // Pattern that the knight movement followes.
  for (int baseIndex = 0; baseIndex < 8; baseIndex++) { // Loop through every tile in the pattern
    int y = unfilteredPattern[baseIndex][0];
    int x = unfilteredPattern[baseIndex][1];
    if ((y >= 0 && y < 8) && (x >= 0 & x < 8)) { // If the tile exists on a board.
      if (!())
    }
  }
}

int *getTiles(int piece, int board[8][8]) {
  // Returns the available squares that a piece can move to.
  int pType = getPieceById(piece);
  if (pType == 2) {
    // If piece is a knight.
    return getKnightTiles(piece, board);
  }
}
