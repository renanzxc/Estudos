package collectionsframework;
import java.util.*;


public class TestaComparacao {
    public static void main(String[] args) {
        Conta c1 = new Conta(123, 789, "Joao");
        Conta c2 = new Conta(345, 345, "Antonio");
        Conta c3 = new Conta(567, 567, "Maria");
        Conta c4 = new Conta(789, 123, "Paulo");
        
        List<Conta> contas = new ArrayList();
        contas.add(c1);
        contas.add(c2);
        contas.add(c3);
        contas.add(c4);
        
        for(Conta conta : contas){
            System.out.println(conta);
        }
        
        Collections.sort(contas);
        System.out.println("-----------");

        for(Conta conta : contas){
            System.out.println(conta);
        }
    }  
}
