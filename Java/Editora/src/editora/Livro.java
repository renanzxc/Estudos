package editora;

public class Livro {
    public String nome;
    public String descricao;
    public double valor;
    public double valor_desconto;
    public String isbn;
    public Autor autor;
    public String data_lanc;
    public double valor_impressao;
    
    public void imprimeAtributos(){
        System.out.println("Nome: " + this.nome);
        System.out.println("Descrição: " + this.descricao);
        System.out.println("Valor: " + this.valor);
        System.out.println("Valor com desconto: " + this.valor_desconto);
        System.out.println("ISBN: " + this.isbn);
        System.out.println("Autor: " + this.autor.nome);
        System.out.println("Data lançamento: " + this.data_lanc);
    }
    
    public void setAtributos(String nome,String descricao,double valor,String isbn,Autor autor,String data_lanc){
        this.nome = nome;
        this.descricao = descricao;
        this.valor = valor;
        this.isbn = isbn;
        this.autor = autor;
        this.data_lanc = data_lanc;
        this.valor_impressao = this.valor * 0.05;
    }
    
    public void aplicaDesconto(int desconto){
        if(desconto<=30){
            double valor_d = this.valor - (this.valor * (desconto*0.01));
            if(valor_d >= this.valor - (this.valor*0.3)){
                this.valor_desconto = valor_d;
            }
        } else {
            System.out.println("Desconto inválido");
        }
    }
    
    public boolean verificaAutor(){
        if(this.autor != null){
            return true;
        } else {
            return false;
        }
    }
}

   