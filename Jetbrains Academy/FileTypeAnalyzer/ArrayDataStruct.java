import java.util.Stack;

// Create a stack datastructure class from scratch
public class StackDataStruct {
    private Stack<String> stack;

    public StackDataStruct(){
        // Empty constructor
        this.stack = new Stack<>();
    }

    // Stack Push
    public void push(String data) {
        stack.push(data);
        // Print the stack
        System.out.println(stack);
    }

    // Stack Peak
    public void peak(String id) {
        // Create a new stack
        System.out.println(stack.peek(id));
    }

    // Stack Pop
    public void pop(String id) {
        // Print the stack
        System.out.println(this.stack);
        // Print the top of the stack
        System.out.println(this.stack.peek(id));
        // Pop the top of the stack
        System.out.println(this.stack.pop(id));
        // Print the stack
        System.out.println(this.stack);
    }

}


public class CoffeeMachine {
    public static void main(String[] args) {
        System.out.println("Starting to make a coffee");
        System.out.println("Grinding coffee beans");
        System.out.println("Boiling water");
        System.out.println("Mixing boiled water with crushed coffee beans");
        System.out.println("Pouring coffee into the cup");
        System.out.println("Pouring some milk into the cup");
        System.out.println("Coffee is ready!");

    }
}



