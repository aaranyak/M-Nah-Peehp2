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

bool getPieceColour(int id) {
  // Returns the pieces colour
  if (id >= 17) {
    return false;
  } else {
    return true;
  }
}
