using System.Net.Mail;
using Randomn
namespace ConsoleApp1;

public class Prey
{
    protected int x;
    protected int y;
    protected int fitness;
    protected int days_survived;
    private int enemy_close;
    protected PreyGenes genes;
    protected int NUMGENES;
    protected List<int> pos = new List<int>();
    
    
    
    public Prey(List<int> pos)
    {
        this.x = x;
        this.y = y;
        this.fitness = 0;
        this.days_survived = 0;
        this.enemy_close = 0;
        this.genes = new PreyGenes();
        this.NUMGENES = 0;
        this.pos = pos;
        
    }