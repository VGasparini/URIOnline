// Autor: [loopTree] VGasparini 🎈<gasparini.vinicius@hotmail.com>
// Nome: Libertadores
// Nível: 1
// Categoria: AD-HOC
// URL: https://www.urionlinejudge.com.br/judge/pt/problems/view/1536


#include<stdio.h>
#include<stdlib.h>


int main()
{
           int tc,t1,t2,tmp1,tmp2;
           int team1,team2;

           scanf("%d",&tc);

           while(tc--){

           team1=0;
           team2=0;

                      scanf("%d",&t1);  // home
                      getchar();
                      getchar();
                      getchar();
                      scanf("%d",&t2); //  away


                      scanf("%d",&tmp2); // home
                      getchar();
                      getchar();
                      getchar();
                      scanf("%d",&tmp1); // away

                      team1=t1+tmp1;
                      team2=t2+tmp2;

                      if(team1>team2)
                                 printf("Time 1\n");
                       else if(team1==team2 && tmp1>t2)
                                   printf("Time 1\n");
                       else if(team1==team2 && t1==tmp2 && t2==tmp1)
                                 printf("Penaltis\n");
                        else
                       printf("Time 2\n");


                             //printf("%d %d",team2,team1);

           }

           return 0;
}

