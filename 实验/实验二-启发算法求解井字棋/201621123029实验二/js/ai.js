function AIAction() {
    let emptyCell = getEmptyCell(game.chessPane.checkMap);
    // let down = mind.random(emptyCell);
    // paneDiv[down].click();
    let down = mind.master();
    setTimeout(() => {
        game.ui.paneDiv[down].click();
    },AI.thinkDelay);
}

function getEmptyCell(checkMap) {
    let emptyCell = [];
    for (let i = 0; i < checkMap.length; i++) {
        if (checkMap[i]) continue;
        emptyCell.push(i);
    }
    return emptyCell;
}

let mind = {
    random(emptyCell) {
        let index = Math.floor(Math.random() * emptyCell.length);
        return emptyCell[index];
    },
    master() {
        let res = AI.minmax(game.chessPane.checkMap);
        res.sort((a, b) => {
            // if (a.score < 0 && b.score < 0) return b.score - a.score;
            return a.score - b.score
        });
        console.log('ai got', res);
        return res[0].pos;
    }
}
let AI = {
    state: {
        hand: null
    },
    thinkDelay: 0,
    _hold: null,
    set hold(val) {
        this.state.hand = val;
        this._hold = val;
        console.log('机器人持子', val);
    },
    get hold() {
        return this._hold;
    },
    toggleHand() {
        return Game.prototype.toggleHand.call(this);
    },
    putChess(pane, index, hand) {
        pane[index] = hand.chess;
    },
    minmax(pane) {
        pane = pane.slice();
        let moveStep = [];
        let emptys = getEmptyCell(pane);
        for (let each of emptys) {
            let score = this.action(each, pane, this.hold);
            moveStep.push({ score, pos: each });
        }
        return moveStep;
    },
    action(pos, pane, hand, step = 1) {
        pane = pane.slice();
        let res = 0;//AI无所事事/为后面计划惩罚值
        let env = {};
        env.checkWin = Game.prototype.checkWin.bind(env);
        env.chessPane = Object.assign({}, game.chessPane);
        env.chessPane.checkMap = pane;
        env.state = Object.assign({}, game.state);
        env.state.hand = hand;
        this.putChess(pane, pos, hand);
        let winner = Game.prototype.judgeWin.call(env, pos);
        let emptys = getEmptyCell(pane);
        // if (step === 2 && pane[6] === 'clear')
        //     console.log(step, pos, hand, pane, winner);
        if (winner) {
            if (winner === this.hold) return -1 * (10 / step) ** (emptys.length + 1);//AI攻击性
            else if (winner === handDraw) return 0;
            else return (10 / step) ** (emptys.length + 1);//AI防御性
        }
        for (let each of emptys) {
            res += this.action(each, pane, getAnotherHand(hand), step + 1);
        }
        return res;
    }
}
function getAnotherHand(hand) {
    if (hand === handA) return handB;
    else return handA;
}