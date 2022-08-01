#include "utilfuncs.h"

void getTiles(int piece, int board[8][8], int *tilesY, int *tilesX) {
  // Returns the available squares that a piece can move to.
  pType = getPieceById(piece);
  if (ptype == 2) {
    // If piece is a knight.
    getKnightTiles(piece, board, tilesY, tilesX);
  }
}

void getKnightTiles(int piece, int board[8][8], int *tilesY, int *tilesX) {
  // Returns the available squares that a knight can move to.
  tilesX = malloc(sizeof(), )
}
