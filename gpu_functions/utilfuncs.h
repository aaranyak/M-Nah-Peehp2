#include <stdio.h>

int getPieceById(int id) {
  if (id == 1 || id == 8 || id == 24 || id == 17) {
    // If piece is a rook.
    return 1;
  }
  else if (id == 2 || id == 7 || id == 23 || id == 18) {
    // If piece is a knight.
    return 2;
  }
}
