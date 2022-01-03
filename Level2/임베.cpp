void sub(){
    int *pi = new int;
    *pi = 69;
    delete pi;

    pi = new int;
    *pi = 99;
    delete pi;
}


