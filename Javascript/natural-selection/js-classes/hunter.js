class Hunter {
    constructor(name) {
        this.name = name;
        this.x = 0;
        this.y = 0;
        this.fitness = 0;
        this.genes = Genes(random(0, 1), random(0, 1), random(0, 1), random(0,1))
        this.kills = 0;
        this.pos = []
    }

    upgrade() {
        this.fitness += 1;
    }

    set_pos(x, y) {
        this.x = x;
        this.y = y;
    }

    get_pos() {
        return [this.x, this.y];
    }

}