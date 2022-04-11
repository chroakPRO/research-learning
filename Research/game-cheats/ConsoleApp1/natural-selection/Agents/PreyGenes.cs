namespace ConsoleApp1;

public class PreyGenes : Prey
{
    public int health;
    public int attack;
    public int speed;
    public int weight;

    public PreyGenes(int health, int weight, int attack, int speed)
    {
        this.health = health;
        this.weight = weight;
        this.attack = attack;
        this.speed = speed;
    }
}