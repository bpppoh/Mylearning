import java.util.ArrayList;
import java.util.List;

public class User {
    public String FirstName ;
    public String Lastname ;
    public int BirthYear ;
    public double salary ;

    public User(String firstName, String lastname, int birthYear, double salary) {
        this.FirstName = firstName;
        this.Lastname = lastname;
        this.BirthYear = birthYear;
        this.salary = salary;
    }
    
    public User(String firstName , int birthYear) {
        this.FirstName = firstName;
        this.BirthYear = birthYear;
    }

    public static void main(String[] args) {
        List<User> users = new ArrayList<>();
        users.add(new User("Terrance","Johnson",2005,5000.0));
        users.add(new User("John","Smith",1966,15000.0));
        users.add(new User("Eva","Birch",2002,20000.0)) ;
        int currentYear = 2028 ;
        
        List<UserWithAge> fullNames = new ArrayList<>();
        for (User user : users) {
            if (user.BirthYear >= 1990){
                fullNames.add(new UserWithAge(user.FirstName , user.Lastname , user.salary , currentYear - user.BirthYear));
            }
        }
        for (UserWithAge newUser : fullNames) {
            System.out.println("fullname=" + newUser.fullname + " ,salary=" + newUser.salary + " ,age=" + newUser.age);
        }

        List<User> age1990 = new ArrayList<>();
        for (User user : users) {
            if (user.BirthYear >= 1990){
                age1990.add(new User(user.FirstName , user.BirthYear));
            }
        }
        for (User user1990 : age1990) {
            System.out.println("FirstName : " + user1990.FirstName + " , BirthYear: " + user1990.BirthYear);
        }
    }
}

class UserWithAge {
    public String fullname ;
    public String LastName ;
    public double salary ;
    public int age ;

    public UserWithAge(String fullname , String LastName , double salary , int age) {
        this.fullname = fullname;
        this.LastName = LastName;
        this.salary = salary;
        this.age = age;
    }
}
