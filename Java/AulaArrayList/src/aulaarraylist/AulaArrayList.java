package aulaarraylist;
import java.util.*;

public class AulaArrayList {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Joao",10,"111.111.111-1");
        Pessoa p2 = new Pessoa("Paulo",11,"111.111.111-1");
        Pessoa p3 = new Pessoa("Gabriel",15,"111.111.111-1");
        Pessoa p4 = new Pessoa("Antonio",15,"111.111.111-1");
        Pessoa p5 = new Pessoa("Rafael",14,"111.111.111-1");
        
        List<Pessoa> pessoas = new ArrayList();
        pessoas.add(p1);
        pessoas.add(p2);
        pessoas.add(p3);
        pessoas.add(p4);
        pessoas.add(p5);
        
        //pessoas.forEach((pessoa) -> {
        //    System.out.println(pessoa);
        //});
        for(Pessoa pessoa : pessoas){
            System.out.println("Nome: " + pessoa.getNome());
            System.out.println("Idade: " + pessoa.getIdade());
            System.out.println("Cpf: " + pessoa.getCpf());

        }
        
        for(Pessoa pessoa : pessoas){
            System.out.println(pessoa);
        }
        
        System.out.println("Tamanho Array: " + pessoas.size());
        pessoas.remove(2);
        System.out.println("Tamanho Array: " + pessoas.size());
        System.out.println(pessoas.get(pessoas.size()-1));
        
        Collections.sort(pessoas);
   
        for(Pessoa pessoa : pessoas){
            System.out.println("Nome: " + pessoa.getNome());
            System.out.println("Idade: " + pessoa.getIdade());
            System.out.println("Cpf: " + pessoa.getCpf());

        }
        
    }
    
}
