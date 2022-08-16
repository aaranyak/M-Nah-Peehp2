#include "utilfuncs.h"
#include <stdlib.h>
int *getKnightTiles(int piece, int board[8][8]) {
  int *retTiles = malloc(32 * 8); // Allocate memory for the tiles.
  int position[2];
  getPositionOfPiece(piece, board, position);
  int posY = position[0];
  int posX = position[1];
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
  int retSize = 0;
  int simpleBoard[8][8];
  teamifyBoard(board, simpleBoard);
  for (int baseIndex = 0; baseIndex < 8; baseIndex++) { // Loop through every tile in the pattern
    int y = unfilteredPattern[baseIndex][0];
    int x = unfilteredPattern[baseIndex][1];
    if ((y >= 0 && y < 8) && (x >= 0 & x < 8)) { // If the tile exists on a board.
      if (simpleBoard[y][x] != 0) { // If square is not blocked by own piece.
        retTiles[retSize * 2] = y;
        retTiles[(retSize * 2) + 1] = x;
        retSize++;
      }
    }
  }
  printf("%d\n", retSize);
  if (retSize == 0) {
    retTiles = realloc(retTiles, sizeof(int));
  }
  else {
    retTiles = realloc(retTiles, sizeof(int) * retSize * 2);
  }
  return retTiles;
}

int *getTiles(int piece, int board[8][8]) {
  // Returns the available squares that a piece can move to.
  int pType = getPieceById(piece);
  if (pType == 2) {
    // If piece is a knight.
    return getKnightTiles(piece, board);
  }
  if (pType == 6) {
    // If piece is a pawn

  }
}
