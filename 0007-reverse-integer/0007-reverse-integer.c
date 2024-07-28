

int reverse(int n){
    int a,c;
    int b;
    a=0;
    c=0;
    b=0;
    while(n!=0){
        
        a = n%10;
        
        if (b < INT_MIN/10 || b > INT_MAX/10){
            return 0;
        }
     
        b = b*10 + a;
        n = n/10;
    }
    
    return b;
}