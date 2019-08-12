package tratandoexcecoes;

import java.util.InputMismatchException;
import java.util.Scanner;


public class TratandoExcecoes {
    public static void main(String[] args) {
        try{
            Scanner scan = new Scanner(System.in);
            int x,y,resultado;
            System.out.print("Insira o primeiro número: ");
            x = scan.nextInt();

            System.out.print("Insira o segundo número: ");
            y = scan.nextInt();
            resultado = x/y;
            System.out.println("Resultado: " + resultado);
        }
        catch(ArithmeticException ae){
            System.out.println("Não é possível dividir por zero");
        }
        catch(InputMismatchException ime){
            System.out.println("Digite somente números");
        }
        
    }
    
}
