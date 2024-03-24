import java.util.*;
class CardsGame
{
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of games to be played today:");
        int no=sc.nextInt();
        System.out.println("Enter the number of players:");
        int n=sc.nextInt();
        n=n+1;
        System.out.println("Enter the name of players:");
        int i;
        String name[]=new String[n];
        int pts[]=new int[n];
        int d[]=new int[n];
        int f[]=new int[n];
        int p[]=new int[n];
        for(i=0;i<n;i++)
        {
            name[i]=sc.nextLine();//to enter the player names
        }
        System.out.println("Please enter all wins with the digit zero.");
        int e=1;
        for(i=e;i<n;i++)//loop to know the person to distribute the cards next
        {
            System.out.println(name[i]+" should distribute the cards.");
            break;
        }
        int j,a=0,b=0,c=0;
        for(j=0;j<no;j++)
        {
            e++;
            System.out.println("Enter the points of:-");
            for(i=1;i<n;i++)
            {
                System.out.print(name[i]+":");
                pts[i]=sc.nextInt();
                if((pts[i]>80)||(pts[i]<0))//for score range
                System.out.println("Error! Range of score is between 0 to 80.");
                else
                {
                    if(pts[i]==0)//for win
                    {
                        d[i]=d[i]+1;
                        a++;b++;
                    }
                    else if(pts[i]==80)//for full
                    {
                        f[i]=f[i]+1;
                        p[i]=p[i]+pts[i];//storing points in p
                    }
                    else//for other points
                    {
                        p[i]=p[i]+pts[i];//storing points in p
                    }
                }
            }
            if(a>=2)
            {
                System.out.println("Error! More than 1 zero!");
                c=1;
                break;
            }
            else if(a<1)
            {
                System.out.println("Error! Less than 1 zero.");
                c=1;
                break;
            }
            else
            {
                System.out.println("Name\tPoints\tDs\t80s");
                for(i=0;i<n;i++)
                {
                    System.out.println(name[i]+"\t"+p[i]+"\t"+d[i]+"\t"+f[i]);
                }
                c=0;
            }
            if(c==1)
            break;
            a=0;c=0;
            if(e==4)
            {
                e=1;
            }
            for(i=e;i<n;i++)
            {
                System.out.println(name[i]+" should distribute the cards.");
                break;
            }    
        }
        int small,pos,tmp;String small1,tmp1;
        for(i=0;i<n;i++)
        {
            small=p[i];
            small1=name[i];
            pos=i;
            for(j=i+1;j<n;j++)
            {
                if(small>p[j])
                {
                    small=p[j];
                    small1=name[j];
                    pos=j;
                }
            }
            tmp=p[i];
            p[i]=p[pos];
            p[pos]=tmp;
            tmp1=name[i];
            name[i]=name[pos];
            name[pos]=tmp1;
        }
        System.out.println("The Winning Order:");
        for(i=0;i<n;i++)
        {
            System.out.println(name[i]);
        }
        System.out.println("Game Over!!!");
        System.out.println("Congratulations!!!");
        for(i=1;i<n;i++)
        {
            System.out.println("The Winner is:"+name[i]);
            break;
        }
    }
}