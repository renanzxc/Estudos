package collectionsframework;
import java.util.*;

public class TestaConjuntoContas {
    public static void main(String[] args) {
        Conta c1 = new Conta(123, 789, "Maria");
        Conta c2 = new Conta(345, 345, "Antonio");
        Conta c3 = new Conta(123, 789, "Maria");
        Conta c4 = new Conta(789, 123, "Paulo");
        
        Set<Conta> contas = new HashSet();
        contas.add(c1);
        contas.add(c2);
        contas.add(c3);
        contas.add(c4);
        
        for(Conta conta : contas){
            System.out.println(conta);
        }        
    } 
}
