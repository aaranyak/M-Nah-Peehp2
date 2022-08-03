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
  int posY; // Declare variable for Y Position.
  int posX; // Declare variable for X Position.
  int position[2]; // Declare position var.
  posY = position[0]; // Y position of piece.
  posX = position[1]; // X Position of piece.
  getPositionOfPiece(piece, board, position); // Calculate piece positions.
  int unfilteredPattern[2][8] = {
    {posY + 1, posX + 2},
    {posY + 2, posX + 1},
    {posY - 1, posX - 2},
    {posY - 2, posX - 1},
    {posY + 1, posX - 2},
    {posY - 2, posX + 1},
    {posY - 1, posX + 2},
    {posY + 2, posX - 1},
  }; // Pattern that the knight movement followes.
  tilesY = (int*) malloc(8 * sizeof(int)); // Allocates the memory for storing the tiles on Y axis.
  tilesX = (int*) malloc(8 * sizeof(int)); // Allocates the memory for storing the tiles on X axis.
  int simpleBoard; // Declare variable for simple board.
  teamifyBoard(board, simpleBoard); // Calculate simple board.
  int retSize = 0; // Size of the pointer.
  for (size_t patIn = 0; patIn < 8; patIn++) {
    int y = unfilteredPattern[0][patIn];
    int x = unfilteredPattern[1][patIn];
    // If the square exists.
    if ((posX < 8 && posX >= 0) && (posY < 8 && posY >= 0)) {
      // If the square is not blocked by a friendly piece.
      if (!(simpleboard[y][x] == 1)) {
        tilesY[retSize] = y; // Add the tile to the memory pointer for Y axis.
        tilesX[retSize] = x; // Add the tile to the memory pointer for X axis.
        retSize++; // Increment the index value.
      }
    }
  }
  tilesY = (int*) realloc(tilesY, sizeof(int) * retSize); // Free the unused memory.
  tilesX = (int*) realloc(tilesY, sizeof(int) * retSize); // Free the unused memory.
}
