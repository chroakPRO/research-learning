//you learn nothing from copy and pasting, write it on your own and follow the tut!
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace program_learn_01
{
    class Program
    {
        public static int Base = 0x004E4DBC;
        public static int Health = 0xF4;


        static void Main(string[] args)
        {
            VAMemory vam = new VAMemory("esportal-client");

            int LocalPlayer = vam.ReadInt32((IntPtr)Base);
            vam.

            while(true)
            {
                int address = LocalPlayer + Health;
                vam.WriteInt32((IntPtr)address, 9999);


                Thread.Sleep(100);


            }



        }
    }

    class SHA256Gen
    {
        public static string GetSHA256(string str)
        {
            SHA256 sha256 = SHA256Managed.Create();
            ASCIIEncoding encoding = new ASCIIEncoding();
            byte[] stream = null;
            StringBuilder sb = new StringBuilder();
            stream = sha256.ComputeHash(encoding.GetBytes(str));
            for (int i = 0; i < stream.Length; i++) sb.AppendFormat("{0:x2}", stream[i]);
            return sb.ToString();
        }
        
        public static string GenerateSHA256String(int length)
        {
            const string valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
            StringBuilder res = new StringBuilder();
            Random rnd = new Random();
            while (0 < length--)
            {
                res.Append(valid[rnd.Next(valid.Length)]);
            }
            return res.ToString();
        }
        
        public void GenerateJTWToken()
        {
            string token = GenerateSHA256String(32);
            string tokenHash = GetSHA256(token);
            Console.WriteLine("JTW Token: " + token);
            Console.WriteLine("JTW Token Hash: " + tokenHash);
            Console.ReadKey();
        }
    }
    
    void GenerateJSONWEBToken()
    {
        string token = GenerateSHA256String(32);
        string tokenHash = GetSHA256(token);
        Console.WriteLine("JSON Web Token: " + token);
        Console.WriteLine("JSON Web Token Hash: " + tokenHash);
        Console.ReadKey();
    }
}