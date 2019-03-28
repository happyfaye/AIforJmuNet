class UI {
    constructor(game){
        this.game = game;
        this.paneDiv = [];
    }
    initPane(pane) {
        this.checkerboardDiv = pane;
        for (let i = 0; i < 9; i++) {
            let check = document.createElement('div');
            check.classList.add('check');
            let placeholder = document.createElement('label');
            placeholder.classList.add('placeholder');
            placeholder.innerText = i;
            this.game.initCheck(check, i);
            check.appendChild(placeholder);
            pane.appendChild(check);
            this.paneDiv.push(check);
        }
    }
    putChess(check) {
        let chess = document.createElement('i');
        check.classList.add('chessman');
        chess.classList.add('material-icons');
        chess.innerText = this.game.state.hand.chess;
        check.appendChild(chess);
    }
}