#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    priority_queue<int> pq;
    queue< pair<int, int> > Q;

    for (int i = 0; i < priorities.size(); i++) {
        pq.push(priorities[i]);
        Q.push(make_pair(priorities[i], i));
    }

    while (!Q.empty()) {
        int value = Q.front().first;
        int index = Q.front().second;
        Q.pop();

        if (pq.top() == value) {
            pq.pop();
            answer += 1;
            if (index == location) 
                break;
        }
        else 
            Q.push(make_pair(value, index));
    }
    return answer;
}