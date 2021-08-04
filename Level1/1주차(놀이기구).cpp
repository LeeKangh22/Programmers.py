#include<iostream>
using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1; //long long 자료형이 아닌 int 사용 시 자릿수에 의한 에러 발생
    long long total = 0;

    for(int i = 0; i < count; i++){
        total += (i + 1) * price;
    }
    answer = money - total;
    if(answer < 0)
        answer = -(answer);
    else
        answer = 0;

    return answer;
}