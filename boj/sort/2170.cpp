#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    int n, i, start, end, ans=0;
    pair<int, int> lines[1000000];

    scanf("%d", &n);
    for(i=0; i<n; i++) scanf("%d%d", &lines[i].first, &lines[i].second);
    sort(lines, lines+n);

    for(i=0; i<n; i++){
        start = lines[i].first;
        end = lines[i].second;

        while(i<n-1 && end > lines[i+1].first) end = max(end, lines[++i].second);
        ans += end-start;
    }

    printf("%d", ans);
}