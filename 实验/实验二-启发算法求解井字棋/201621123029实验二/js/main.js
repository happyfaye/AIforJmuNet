class Game {
    constructor() {
        this.state = {
            hand: handA,
            put: null,
            win: null
        }
        this.chessPane = {
            width: 3,
            height: 3,
            range: null,
            checkMap: null,
            emptyCells: []
        }
        this.ui = new UI(this);
    }
    startUp() {
        this.chessPane.range = this.chessPane.width * this.chessPane.height;
        this.chessPane.checkMap = new Array(this.chessPane.range);
        for (let i = 0; i < this.chessPane.range; i++) this.chessPane.emptyCells.push(i);
        let pane = document.getElementsByClassName('pane');
        this.ui.initPane(pane[0]);
        switch (settings.mode.value) {
            case 'vs': {
                handA.player = 'player A';
                handB.player = 'player B';
                break;
            }
            case 'vscom': {
                handA.player = 'human';
                handB.player = 'robot';
                AI.hold = handB;
                break;
            }
            case 'com': {
                handA.player = 'robot';
                handB.player = 'robot';
                AI.hold = handA;
                AI.thinkDelay = 2000;
                AIAction();
                break;
            }
        };
    }
    initCheck(check, index) {
        check.onclick = (e) => {
            if (this.chessPane.checkMap[index]) {
                console.log('位置', index, '已经有落子，请重新下子');
                return;
            }
            this.chessPane.checkMap[index] = this.state.hand.chess;
            delete this.chessPane.emptyCells[index];
            // console.log('you click', index, this.chessPane.checkMap, this.chessPane.emptyCells);
            this.ui.putChess(check);
            this.state.put = index;
            this.state.win = this.judgeWin(index);
            if (this.state.win) {
                console.log('Game End', this.state.win);
                this.end();
                return;
            }
            this.toggleHand();
            if (this.state.hand.player === 'robot')
                AIAction();
        }
    }
    judgeWin(index) {
        // let col = Math.floor(index / this.chessPane.width);
        // let row = index % this.chessPane.width;
        // console.log('判断', this.state.hand.chess, '胜利，棋盘', this.chessPane.checkMap, '落子', index);
        let res = false;
        let arg2 = [
            [i => i % this.chessPane.width, 1],
            [i => Math.floor(i / this.chessPane.width), this.chessPane.width],
            [i => i % this.chessPane.width, this.chessPane.width + 1],
            [i => i % this.chessPane.width, this.chessPane.width - 1]
        ]
        for (let arg of arg2) {
            res = this.checkWin(index, ...arg);
            if (res) return res;
        }
        if (getEmptyCell(this.chessPane.checkMap).length === 0) {
            return handDraw;
        }
    }
    checkWin(index, calc, step) {
        let start = calc(index);
        while (start > -1 && (this.chessPane.checkMap[index - step] === this.state.hand.chess)) {
            index -= step;
            let nstart = calc(index);
            //将检查位置限制在落点前后一列，这样不会出现5,2 => 3,0 => 7,1的情况
            if (Math.abs(nstart - start) === 1) start = nstart;
            else return;
        }
        let score = 0;
        let scoreSet = [];
        // console.log('start', index, start);
        while (start < this.chessPane.width && (this.chessPane.checkMap[index] === this.state.hand.chess)) {
            scoreSet.push(index);
            score++;
            index += step;
            let nstart = calc(index);
            //同上
            if (Math.abs(nstart - start) === 1) start = nstart;
            else break;
            // console.log('then', index, start, score);
        }
        if (score === 3) {
            // console.log('Win route', scoreSet);
            return this.state.hand;
        }
    }
    toggleHand() {
        if (this.state.hand === handA) {
            this.state.hand = handB;
        } else {
            this.state.hand = handA;
        }
    }
    end() {
        if (this.state.win === handDraw)
            console.log('Nobody Win');
        else console.log(this.state.win.player, 'Win');
    }
}

let handA = {
    chess: 'panorama_fish_eye',
    player: 'human'
};
let handB = {
    chess: 'clear',
    player: 'robot'
};
let handDraw = {}
let settings = document.forms['settings'];
let startBtn = document.getElementById('start-btn');

let game = null;
function GameStart() {
    if (game) {
        for (let div of game.ui.paneDiv)
            game.ui.checkerboardDiv.removeChild(div);
        AI.thinkDelay = 0;
    }
    game = new Game();
    game.startUp();
    startBtn.innerText = '重新开始';
}