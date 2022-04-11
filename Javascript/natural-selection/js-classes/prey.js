class Prey {
    constructor(name) {
        this.name = name;
        this.x = 0;
        this.y = 0;
        this.fitness = 0;
        this.days_survived = 0;
        this.enemy_close = 0;
        this.isAlive = true;
        this.genes = new Genes(Math.floor(Math.random() * 10), Math.random() * 10, Math.random() * 10, Math.random() * 10);
        self.NUM_GENES = 0;
        self.pos = [];
    }

    update() {
        this.days_survived++;
        this.fitness = this.days_survived + this.enemy_close;
        this.genes.update();
    }


    /** set pos function
     * @param {int} x
     * @param {int} y
     */
    set_pos(x, y) {
        this.x = x;
        this.y = y;
    }
    // TODO: add a function to check if prey is close to enemy
    // * if prey is close to enemy, enemy_close = 1
    // * if prey is not close to enemy, enemy_close = 0

    /**
     * @returns {fitness} fitness
     */
    calc_fitness() {
        this.fitness = ((this.days_survived / 0, 45) * (this.genes[0] / 0.09) * (this.enemy_close / 0.02));
        return this.fitness;
    }

    /** mutation function
     * @param {list} xx_genes
     * @param {list} yy_genes
     *
     * @returns {list{list}} [child01[], child02[]]
     *
     */
    mutation(xx_genes, xy_genes) {
        let child01 = [];
        let child02 = [];

        let gen_len = xx_genes.length;
        let crossover_point = Math.floor(Math.random() * gen_len.length);
        for(let i = 0; i < gen_len; i++) {
            if (i < crossover_point) {
                child01.push(xx_genes[i]);
                child02.push(xy_genes[i]);
            } else {
                child01.push(xy_genes[i]);
                child02.push(xx_genes[i]);
            }
        }
        return [child01, child02];
    }

    /** Set random genes function
     * @returns {int} 0 ? 1
     */
    setRandomGenes() {
        this.genes = [];
        try {
            for (let i = 0; i < self.NUM_GENES; i++) {
                this.genes.push(Math.random() * 10);
            }
            return 1;
        }
        catch (err) {
            console.log(err);
            return 0;
        }
    }
}
