// Independent-language BFS check of the rooted-distance formula.
// All rights reserved. No exact arbitrary-pair diameter is computed here.
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
int n;
vector<string> paths;
vector<vector<int>> host;
string canon(string p) { if(p.front()>p.back()) reverse(p.begin(),p.end()); return p; }
void dfs(string &p,uint64_t used) {
    if(int(p.size())==n) { if(p.front()<p.back()) paths.push_back(p); return; }
    for(int v:host[(unsigned char)p.back()]) if(!(used>>v&1)) {
        p.push_back(char(v)); dfs(p,used|(1ULL<<v)); p.pop_back();
    }
}
vector<int> curl(int a) {
    if(a==0) return {0};
    vector<int> p;
    for(int x=a;x>=0;x-=2) p.push_back(x);
    for(int x=(a%2==0?1:0);x<=a+1;x+=2) p.push_back(x);
    return p;
}
int formula(const string &p, bool &corner) {
    int a=(unsigned char)p.front(), b=(unsigned char)p.back();
    int low=a==0?0:a+1, high=b==n-1?n-1:b-1;
    vector<int> swaps;
    for(int t=0;t<n-1;t++) {
        int i=(unsigned char)p[t+1];
        if(int((unsigned char)p[t])==i+1 && low+1<=i && i<=high-2) swaps.push_back(i);
    }
    sort(swaps.begin(),swaps.end());
    for(int j=1;j<int(swaps.size());j++) assert(swaps[j]-swaps[j-1]>=3);
    vector<int> mid;
    for(int i=low;i<=high;i++) mid.push_back(i);
    for(int i:swaps) swap(mid[i-low],mid[i+1-low]);
    auto left=curl(a), right=curl(n-1-b);
    for(int &x:right) x=n-1-x;
    reverse(right.begin(),right.end());
    vector<int> rebuilt(left.begin(),left.end()-1);
    rebuilt.insert(rebuilt.end(),mid.begin(),mid.end());
    rebuilt.insert(rebuilt.end(),right.begin()+1,right.end());
    assert(int(rebuilt.size())==n);
    for(int i=0;i<n;i++) assert(rebuilt[i]==int((unsigned char)p[i]));
    int k=swaps.size(), answer=1000000;
    int dl=k && a==0 && swaps.front()==1;
    int dr=k && b==n-1 && swaps.back()==n-3;
    for(int j=0;j<=k;j++) {
        int lc=j==0?a:2*(swaps[j-1]+1)-a-2*j+dl;
        int rc=j==k?n-1-b:b+n-1-2*swaps[j]-2*(k-j)+dr;
        answer=min(answer,lc+rc);
    }
    corner=a==0 && b==n-1;
    return answer;
}
int main(int argc,char **argv) {
    int limit=argc>1?stoi(argv[1]):32;
    assert(3<=limit && limit<=40);
    ofstream out(argc>2?argv[2]:"ROOT_BFS_CPP.jsonl");
    for(n=3;n<=limit;n++) {
        auto start=chrono::steady_clock::now();
        paths.clear(); host.assign(n,{});
        for(int i=0;i<n;i++) for(int j=0;j<n;j++)
            if(0<abs(i-j) && abs(i-j)<=2) host[i].push_back(j);
        for(int s=0;s<n;s++) { string p(1,char(s)); dfs(p,1ULL<<s); }
        unordered_map<string,int> index;
        index.reserve(paths.size()*2);
        for(int i=0;i<int(paths.size());i++) index.emplace(paths[i],i);
        string identity; for(int i=0;i<n;i++) identity.push_back(char(i));
        int root=index.at(identity), m=paths.size();
        vector<int> dist(m,-1), queue(m); queue[0]=root; dist[root]=0;
        int front=0,back=1; long long arcs=0;
        while(front<back) {
            int u=queue[front++]; string p=paths[u]; vector<int> nbr;
            for(int end=0;end<2;end++,reverse(p.begin(),p.end()))
                for(int k=2;k<n;k++) if(abs(int((unsigned char)p[0])-int((unsigned char)p[k]))<=2) {
                    string q=p; reverse(q.begin(),q.begin()+k); nbr.push_back(index.at(canon(q)));
                }
            sort(nbr.begin(),nbr.end()); nbr.erase(unique(nbr.begin(),nbr.end()),nbr.end());
            arcs+=nbr.size();
            for(int v:nbr) if(dist[v]<0) { dist[v]=dist[u]+1; queue[back++]=v; }
        }
        assert(back==m);
        int ecc=0, corner_max=0;
        for(int i=0;i<m;i++) {
            bool corner=false; int f=formula(paths[i],corner);
            if(f!=dist[i]) { cerr<<"FAIL n="<<n<<" state="<<i<<" bfs="<<dist[i]<<" formula="<<f<<endl; return 1; }
            ecc=max(ecc,dist[i]); if(corner) corner_max=max(corner_max,dist[i]);
        }
        double sec=chrono::duration<double>(chrono::steady_clock::now()-start).count();
        out<<"{\"n\":"<<n<<",\"vertices\":"<<m<<",\"edges\":"<<arcs/2
           <<",\"root_eccentricity\":"<<ecc<<",\"corner_max\":"<<corner_max
           <<",\"all_states_match\":true,\"seconds\":"<<sec<<"}\n"; out.flush();
        cout<<"n="<<n<<" vertices="<<m<<" root_eccentricity="<<ecc<<" PASS seconds="<<sec<<endl;
    }
}
