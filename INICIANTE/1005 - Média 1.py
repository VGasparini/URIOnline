# Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
# Nome: Média 1
# Nível: 1
# Categoria: INICIANTE
# URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class Main{
  public static void main(String arg[]) throws IOException{
    Scanner teclado = new Scanner( System.in);
    teclado.useLocale(Locale.US);
    double valor1 = teclado.nextFloat();
    double valor2 = teclado.nextFloat();
    System.out.println(String.format("MEDIA = %.5f", ((valor1*.35)+(valor2*.75))/1.1));
  }
}

