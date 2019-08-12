package collectionsframework;
import java.util.*;

public class CollectionsFramework {
    public static void main(String[] args) {
        Conta c1 = new Conta(123, 789, "Joao");
        Conta c2 = new Conta(345, 345, "Antonio");
        Conta c3 = new Conta(567, 567, "Maria");
        Conta c4 = new Conta(789, 123, "Paulo");
        
        Map<String, Conta> contas = new HashMap();
        contas.put(c1.nome,c1);
        contas.put(c2.nome,c2);
        contas.put(c3.nome,c3);
        contas.put(c4.nome,c4);
        
        for(String nome : contas.keySet()){
            System.out.println(nome + "," + contas.get(nome));
        }
    }    
}
