package aulaarraylist;

public class Pessoa implements Comparable<Pessoa>{
    public String nome;
    public int idade;
    public String cpf;
    
    Pessoa(String nome, int idade, String cpf){
        this.nome = nome;
        this.idade = idade;
        this.cpf = cpf;
    }

    @Override
    public String toString() {
        return "Pessoa{" + "nome=" + nome + ", idade=" + idade + ", cpf=" + cpf + '}';
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public String getCpf() {
        return cpf;
    }
    
    @Override
    public int compareTo(Pessoa p1){
        if(idade == p1.getIdade()){
            return 0;
        }else if(idade < p1.getIdade()){
            return -1;
        }else{
            return 1;
        }
    }
}

