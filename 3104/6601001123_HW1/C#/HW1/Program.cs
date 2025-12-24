using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
namespace ConsoleApplication3
{
    class Program
    {
        public class User
        {
            public string FirstName { get; set; }
            public string LastName { get; set; }
            public int BirthYear { get; set; }
            public double salary { get;set; }
        }
        static void Main(string[] args)
        {
               var users = new List<User>()
                    {
                        new User()
                        {
                            FirstName = "Terrance",
                            LastName = "Johnson",
                            BirthYear = 2005,
                            salary= 5000.0
                        },
                        new User()
                        {
                            FirstName = "John",
                            LastName = "Smith",
                            BirthYear = 1966,
                            salary= 15000.0
                            
                        },
                        new User()
                        {
                            FirstName = "Eva",
                            LastName = "Birch",
                            BirthYear = 2002,
                            salary= 20000.0
                        }
                    };
            int currentYear = 2028;
            //Get the full combined name for people born in 1990 or later
            var fullNames = from x in users
                            where x.BirthYear >= 1990
                           select new { fullname=x.FirstName, 
                                        x.LastName ,x.salary, 
                                        age = currentYear-x.BirthYear  };
            foreach (var item in fullNames)
            {
                System.Console.WriteLine("fullname={0} ,salary={1},age={2}", 
                          item.fullname,item.salary, item.age);
            }
            var age1990 = from x in users
                            where x.BirthYear >= 1990
                            select new { x.FirstName, x.BirthYear };
            foreach (var item in age1990)
            {
                System.Console.WriteLine("FirstName : {0} , BirthYear: {1}", item.FirstName, item.BirthYear);
            }
            return;
        }
    }
}
