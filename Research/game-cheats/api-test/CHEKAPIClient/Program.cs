using System;

namespace MalShare.NET
{
    class Program
    {
        public static void Main(string[] args)
        {
            MSClient client = new MSClient("fee963fbeef39a63af94d268550a87abfe29366507d6f7a53aaa37c7afe9871c");

            Console.WriteLine(client.GetHashList());

        }
    }
}