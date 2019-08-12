package selectionsort;

public class SelectionSort {
    public static void main(String[] args) {
        int i,n=5,min,j,x,cont=0;
        int[] lista = new int[5];
        lista[0]=1;
        lista[1]=2;
        lista[2]=20;
        lista[3]=4;
        lista[4]=5;

            for(i=0;i<n-1;i++){
                min = i;
                for(j=i+1;j<n;j++){
                    cont++;
                    if(lista[j]<lista[min]){
                        min = j;
                    }
                }
                x = lista[min];
                lista[min]= lista[i];
                lista[i]= x;
            }        
        
        for(i=0; i<n;i++){
            System.out.print(" "+lista[i]);
        }
        System.out.println("\nComparações: "+cont);

    }
    
}
