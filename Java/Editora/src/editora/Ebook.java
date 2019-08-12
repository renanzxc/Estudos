package editora;

public class Ebook extends Livro {
    public String formato;
    public String drm;
    
    Ebook(){
        this.valor_impressao = 0;
    }
    @Override
    public void aplicaDesconto(int desconto){
        if(desconto<=15){
            this.valor_desconto = this.valor - (this.valor * (desconto*0.01));
        } else {
            System.out.println("Desconto inválido");
        }
    }
}