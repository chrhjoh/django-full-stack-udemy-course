var playerOne = prompt("Player One: Enter Your Name, you will be Blue");
var playerOneColor = 'rgb(86, 151, 255)';

var playerTwo = prompt("Player Two: Enter Your Name, you will be Red");
var playerTwoColor = 'rgb(237, 45, 73)';

var game_on = true;
var table = $('table tr');




function getColor(row, col){
    return table.eq(row).find("td").eq(col).find("button").css("background-color")
}

function changeColor(row, col, color){
    return table.eq(row).find("td").eq(col).find("button").css("background-color", color)
}


function findAvailSpace(col){
    for (let row = 5 ; row >= 0; row--) {
        var color = getColor(row, col)
        if (color === "rgb(128, 128, 128)"){
            return row
        }
    }
}

function gameOver(){
    $('h3').fadeOut("fast")
    $('h2').fadeOut("fast")
    $('h1').text(currentName + " has won! Refresh your browser to play again!")
    game_on = false
}

function colorMatchCheck(one,two,three,four){
    return (one===two && one===three && one===four && one !== 'rgb(128, 128, 128)' && one !== undefined);
  }

function horizontalWinCheck() {
    for (var row = 0; row < 6; row++) {
      for (var col = 0; col < 4; col++) {
        if (colorMatchCheck(getColor(row,col), getColor(row,col+1) ,getColor(row,col+2), getColor(row,col+3))) {
          console.log('horiz');
          return true;
        }else {
          return false;
        }
      }
    }
  }

function verticalWinCheck(row, col){
    if (currentColor === getColor(row+1, col) && currentColor === getColor(row+2, col) && currentColor === getColor(row+3, col)){
        return true
    }
    else{
        return false
    }

}

function diagonalWinCheck() {
    for (var col = 0; col < 5; col++) {
      for (var row = 0; row < 7; row++) {
        if (colorMatchCheck(getColor(row,col), getColor(row+1,col+1) ,getColor(row+2,col+2), getColor(row+3,col+3))) {
          console.log('diag');
          return true;
        }else if (colorMatchCheck(getColor(row,col), getColor(row-1,col+1) ,getColor(row-2,col+2), getColor(row-3,col+3))) {
          console.log('diag');
          return true;
        }else {
          return false;
        }
      }
    }
  }


function playerChange(){
    currentPlayer = currentPlayer * -1

    if (currentPlayer === 1) {
        currentName = playerOne
        currentColor = playerOneColor
        $('h3').text(currentName+": it is your turn, please pick a column to drop your blue chip.");
    }
    else{
        currentName = playerTwo
        currentColor = playerTwoColor
        $('h3').text(currentName+": it is your turn, please pick a column to drop your red chip.");
    }
}

currentPlayer = 1
currentName = playerOne
currentColor = playerOneColor
$('h3').text(currentName+": it is your turn, please pick a column to drop your blue chip.");

$(".board button").on('click', function(){

    var col = $(this).closest("td").index()

    var row = findAvailSpace(col)
    changeColor(row, col, currentColor)

    if(game_on && (verticalWinCheck(row, col) || horizontalWinCheck(row, col) ||  diagonalWinCheck(row, col))){
        gameOver()
        
    }
    playerChange()
})


