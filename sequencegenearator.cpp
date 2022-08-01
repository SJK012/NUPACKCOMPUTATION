#include<bits/stdc++.h>

using namespace std;

vector<char> v;

void p(vector<char> &v,int &n, int a, char b )
{
 
	cout<<" "<<a+1<<b<<" - ";
     
        // if only genes required without numbering comment the above cout statement

 for(int i=0;i<n;i++)
{
    
    if(v[i]!=' ')
 {cout<<v[i];}

 

}

  }



int main()
{
cout<<"Enter the no of genes "<<endl;
int n;
cin>>n;

cout<<"Enter the sequence without spaces"<<endl;



for(int i=0;i<n;i++)
{
 char a;
 cin>>a;
 v.push_back(a);

}

cout<<""<<endl;
cout<<" Sequences "<<endl;
cout<<""<<endl;

for(int j=0;j<v.size();j++)
{

for(int i=0;i<1;i++)
{
    // for A
    if(v[j]=='A' || v[j]=='a'  )
   { v[j]=' ';
   p(v,n,j,'0');
   v[j]='A';
   cout<<endl;
   }

    if(v[j]=='A' || v[j]=='a')
   { v[j]='C';
   p(v,n,j,v[j]);
   v[j]='A';
   cout<<endl;
   }
    if(v[j]=='A' || v[j]=='a')
   { v[j]='G';
   p(v,n,j,v[j]);
   v[j]='A';
   cout<<endl;
   }
    if(v[j]=='A' || v[j]=='a')
   { v[j]='U';
   p(v,n,j,v[j]);
   v[j]='A';
   cout<<endl;
   }

  

// for G
    if(v[j]=='G' || v[j]=='g')
   { v[j]=' ';
   p(v,n,j,'0');
   v[j]='G';
   cout<<endl;
   }
    if(v[j]=='G' || v[j]=='g')
   { v[j]='A';
   p(v,n,j,v[j]);
   v[j]='G';
   cout<<endl;
   }
    if(v[j]=='G' || v[j]=='g')
   { v[j]='C';
   p(v,n,j,v[j]);
   v[j]='G';
   cout<<endl;
   }
    if(v[j]=='G' || v[j]=='g')
   { v[j]='U';
   p(v,n,j,v[j]);
   v[j]='G';
   cout<<endl;
   }
   

//for U
   if(v[j]=='U' || v[j]=='u' || v[j]=='T' || v[j]=='t')
   { v[j]=' ';
   p(v,n,j,'0');
   v[j]='U';
   cout<<endl;
   }
    if(v[j]=='U'  || v[j]=='u'|| v[j]=='T' || v[j]=='t')
   { v[j]='A';
   p(v,n,j,v[j]);
   v[j]='U';
   cout<<endl;
   }
    if(v[j]=='U'  || v[j]=='u'|| v[j]=='T' || v[j]=='t')
   { v[j]='C';
   p(v,n,j,v[j]);
   v[j]='U';
   cout<<endl;
   }
    if(v[j]=='U'  || v[j]=='u'|| v[j]=='T' || v[j]=='t')
   { v[j]='G';
   p(v,n,j,v[j]);
   v[j]='U';
   cout<<endl;
   }
   

//for C
      if(v[j]=='C'  || v[j]=='c')
   { v[j]=' ';
   p(v,n,j,'0');
   v[j]='C';
   cout<<endl;
   }
    if(v[j]=='C' || v[j]=='c')
   { v[j]='A';
   p(v,n,j,v[j]);
   v[j]='C';
   cout<<endl;
   }
    if(v[j]=='C' || v[j]=='c')
   { v[j]='G';
   p(v,n,j,v[j]);
   v[j]='C';
   cout<<endl;
   }
    if(v[j]=='C' || v[j]=='c')
   { v[j]='U';
   p(v,n,j,v[j]);
   v[j]='C';
   cout<<endl;
   }

}


}

system("pause");


    return 0;
}
