import java.util.ArrayList;

public class L16A1 {
    public static void main(String[] args) {
        ArrayList<Double> list = new ArrayList<>();
        Rectangle obj1 = new Rectangle(10, 5);
        Circle obj2 = new Circle(10);
        Circle obj3 = new Circle(5);

        list.add(obj1.getArea());
        list.add(obj2.getArea());
        list.add(obj3.getArea());

        double totalArea = 0;
        for(int i = 0; i < list.size(); i++){
            totalArea += list.get(i);
        }
        
        System.out.println("Total Area of all shapes: " + totalArea);
    }
}

interface Shape{
    public double getArea();
}

class Rectangle implements Shape{
    private double length;
    private double width;

    public Rectangle(double length, double width){
        this.length = length;
        this.width = width;
    }

    public double getArea(){
        return (length * width);
    }
}

class Circle implements Shape{
    private double radius;
    
    public Circle(double radius){
        this.radius = radius;
    }

    public double getArea(){
        return (Math.PI * radius * radius);
    }
}

