var restart = document.querySelector("#restart")
var board = document.querySelectorAll("td")


function clearBoard(){
    for (let i = 0; i < board.length; i++) {
        const position = board[i];
        position.textContent = ""
        
    } 
    };



restart.addEventListener("click", clearBoard)

function changeField(){
    if (this.textContent == ""){
        this.textContent = "X"
    }
    else if (this.textContent == "X"){
        this.textContent = "O"
    }
    else{
        this.textContent = ""
    }
}
for (let i = 0; i < board.length; i++) {
    const pos = board[i];
    pos.addEventListener("click", changeField)
}