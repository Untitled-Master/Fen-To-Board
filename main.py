from fentoboardimage import fenToImage, loadPiecesFolder
board = fenToImage(
    fen="8/8/8/8/8/5p2/5P2/8 w - - 0 1", #add any fen here
    squarelength=200,
    pieceSet=loadPiecesFolder("pieces"),
    darkColor="#79a65d",
    lightColor="#daf2cb"
)
image_path = 'chess_board.png'  # Path to save the image temporarily
board.save(image_path)
