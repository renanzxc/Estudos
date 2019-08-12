package collectionsframework;

public class Conta implements Comparable<Conta>{
    public int numero;
    public double saldo;
    public String nome;

    Conta(int numero, double saldo, String nome){
        this.numero = numero;
        this.saldo = saldo;
        this.nome = nome;
    }
    
    public int getNumero() {
        return numero;
    }

    public double getSaldo() {
        return saldo;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "Conta{" + "numero=" + numero + ", saldo=" + saldo + ", nome=" + nome + '}';
    }       
    
    @Override
    public int compareTo(Conta c1){
        if(saldo == c1.getSaldo()){
            return 0;
        }else if(saldo < c1.getSaldo()){
            return -1;
        }else{
            return 1;
        }
    }
}
