package editora;

public class Autor {
   public String nome;
   public String email;
   public String cpf;
   
   public void setAtributos(String nome, String email, String cpf){
       this.nome = nome;
       this.email = email;
       this.cpf = cpf;
   }
   
   public void imprimeAtributos(){
        System.out.println(this.nome);
        System.out.println(this.email);
        System.out.println(this.cpf);
    }
}
