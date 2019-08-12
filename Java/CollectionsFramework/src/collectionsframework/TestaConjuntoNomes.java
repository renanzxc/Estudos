package collectionsframework;
import java.util.*;

public class TestaConjuntoNomes {
    public static void main(String[] args) {
        
        Set<String> nomes = new HashSet();
        
        nomes.add("Maria");
        nomes.add("Joao");
        nomes.add("Maria");
        nomes.add("Paulo");
        
        for(String nome : nomes){
            System.out.println(nome);
        }
    } 
}
