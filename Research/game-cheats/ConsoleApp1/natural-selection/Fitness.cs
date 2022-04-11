namespace ConsoleApp1;

public class Fitness
{
    public static double FitnessFunction(double[] x)
    {
        double sum = 0;
        for (int i = 0; i < x.Length; i++)
        {
            sum += x[i] * x[i];
        }
        return sum;
    }
}