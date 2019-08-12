package editora;

public class Main {
    public static void main(String [] args){
        Livro l1 = new Livro();
        Autor joao = new Autor();
        joao.setAtributos("João", "joao@gmail.com", "111.111.111-22");
        l1.setAtributos("Joãozinho adventures","As aventuras de Joãozinho",100,"123",joao,"12/12/12");
        l1.imprimeAtributos();
        l1.aplicaDesconto(30);
        System.out.println("Valor com descontro: " + l1.valor_desconto);
        System.out.println("Autor: " + l1.verificaAutor());
        System.out.println("Valor impressao: " + l1.valor_impressao);
    }
}
