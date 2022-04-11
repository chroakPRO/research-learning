
create_gameboard = () => {
    let game = [];
    let max = 100;
    for(let i = 0; i < max; i++) {
        for(
        game.push([]);
        for(let j = 0; j < max; j++) {
            game[i].push(0);
        }
    }
    return game;
}


pos_taken = (xy, pos_list) => {
    let done = true;
    while (done) {
        if(pos_list.includes()){
            xy = [Math.floor(Math.random()*10), Math.floor(Math.random()*10)]
            console.log(1)
        } else  {
            done = false;
            return xy[0], xy[1]
            console.log(2)
        }


    }
}

//pos_taken([1,1], [[1,1]])
let gameb = create_gameboard();
console.log(gameb);


