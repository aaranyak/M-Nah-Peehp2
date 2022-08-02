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
  int posY;
  int posX;
  getPositionOfPiece(piece, board, posY, posX);
  int unfilteredPattern[2][8] = {
    {}
  };
  tilesY = (int*) malloc(8 * sizeof(int)); // Allocates the memory for storing the tiles on Y axis.
  tilesX = (int*) malloc(8 * sizeof(int)); // Allocates the memory for storing the tiles on X axis.
  int simpleBoard;
  teamifyBoard(board, simpleBoard);
  int retSize = 0;


}
