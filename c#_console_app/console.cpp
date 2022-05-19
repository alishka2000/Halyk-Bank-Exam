using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace CalculatorApp {
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;
            int num1;
            int num2;
            string operand;
            ConsoleKeyInfo status;
            float answer;

            while (true)
            {
                Console.Write("Введите первое число: ");
                num1 = Convert.ToInt32(Console.ReadLine());
                Console.Write("Введите второе число: ");
                num2 = Convert.ToInt32(Console.ReadLine());
                Console.Write("Выберите операцию (+, -, /, *): ");
                operand = Console.ReadLine();

                switch (operand)
                {
                    case "-":
                        answer = num1 - num2;
                        break;
                    case "+":
                        answer = num1 + num2;
                        break;
                    case "/":
                        answer = num1 / num2;
                        break;
                    case "*":
                        answer = num1 * num2;
                        break;
                    default:
                        answer = 0;
                        break;
                }

                Console.WriteLine(num1.ToString() + " " + operand + " " + num2.ToString() + " = " + answer.ToString());
                Console.WriteLine("\n\n Хотите закончить?(Y/n)");
                status = Console.ReadKey();
                if(status.Key==ConsoleKey.Y)
                {
                    break;
                }
                else
                {
                    continue;
                }
                Console.Clear();
            }
        }
    }
}