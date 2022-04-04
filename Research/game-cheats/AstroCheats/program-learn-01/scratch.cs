namespace program_learn_01;

public class scratch
{
    /*
     * Create a function that implements a selection sort algorithm from scratch.
     */
    
    public static void main(String[] args)
    {
        int[] arr = {5, 3, 6, 2, 10, 1};
        selectionSort(arr);
        for (int i = 0; i < arr.length; i++)
        {
            System.out.println(arr[i]);
        }
    }
    
    public void selectionSort(String[] arr)
    {
        for (int i = 0; i < arr.length; i++)
        {
            int min = i;
            for (int j = i + 1; j < arr.length; j++)
            {
                if (arr[j].compareTo(arr[min]) < 0)
                {
                    min = j;
                }
            }
            swap(arr, i, min);
        }
    }
    }