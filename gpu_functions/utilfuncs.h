#include <stdio.h>

int getPieceById(int id) {
  // Takes the piece id and returns the piece type.
  if (id == 1 || id == 8 || id == 24 || id == 17) {
    // If piece is a rook.
    return 1;
  }
  else if (id == 2 || id == 7 || id == 23 || id == 18) {
    // If piece is a knight.
    return 2;
  }
  else if (id == 3 || id == 6 || id == 22 || id == 19) {
    // If piece is a bishop.
    return 3;
  }
  else if (id == 4 || id == 20) {
    // If piece is a king.
    return 4;
  }
  else if (id == 5 || id == 21) {
    // If piece is a queen.
    return 5;
  }
  else if ((id >= 9 && id <= 16) || (id <= 32 && id >= 25)) {
    // If piece is a pawn.
    return 6;
  }
  else {
    return 0;
  }
}

int getPieceColour(int id) {
  // Returns the pieces colour
  if (id >= 17) {
    // Piece is black.
    return 0;
  } else {
    // Piece is white.
    return 1;
  }
}

void simplifyBoard(int board[8][8], int newBoard[8][8]) {
  // Returns a simplified version of the board with only piece types.
  for (size_t y = 0; y < 8; y++) {
    for (size_t x = 0; x < 8; x++) {
      int piece = board[y][x];
      int pieceColour = getPieceColour(piece);
      int pieceType = getPieceById(piece);
      if (pieceColour) {
        newBoard[y][x] = pieceType;
      }
      else {
        newBoard[y][x] = pieceType + 6;
      }
    }
  }
}

void teamifyBoard(int board[8][8], int newBoard[8][8]) {
  // Returns a simplified version of the board with only piece colours.
  for (size_t y = 0; y < 8; y++) {
    for (size_t x = 0; x < 8; x++) {
      int piece = board[y][x];
      int pieceColour = getPieceColour(piece);
      if (piece == 0) {
        newBoard[y][x] = 3;
      }
      else if (pieceColour){
        newBoard[y][x] = 0;
      }
      else {
        newBoard[y][x] = 1;
      }
    }
  }
}

void getPositionOfPiece(int piece, int board[8][8] int posy, int posx) {
  // Returns the x and y position of the piece on the board.
  for (size_t y = 0; y < 8; y++) {
    for (size_t x = 0; x < 8; x++) {
      if (board[y][x] == piece) {
        posx = x;
        posy = y;
      }
    }
  }
}

void drawSimpleBoard(int board[8][8]) {
  for (size_t y = 0; y < 8; y++) {
    for (size_t x = 0; x < 8; x++) {
      printf("%d", board[y][x]);
      printf("%s", " ");
    }
    printf("%s", "\n");
  }
}
