// All-pairs BFS for the finite bases of the exact-diameter working theorem.
// Adjacency is checked with edge sets, degrees, and connectivity, independently
// of the Python prefix-reversal adjacency implementation.
// Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;
int n;
vector<vector<int>> host, paths;
void dfs(vector<int>& p, uint64_t seen) {
    if(int(p.size())==n) { if(p.front()<p.back()) paths.push_back(p); return; }
    for(int v:host[p.back()]) if(!(seen>>v&1)) {
        p.push_back(v); dfs(p,seen|(1ULL<<v)); p.pop_back();
    }
}
int main(int argc,char**argv) {
    int limit=argc>1?stoi(argv[1]):15;
    assert(3<=limit && limit<=20);
    ofstream out(argc>2?argv[2]:"FINITE_BASES_CPP.jsonl");
    for(n=3;n<=limit;n++) {
        host.assign(n,{}); paths.clear();
        for(int i=0;i<n;i++) for(int j=n-1;j>=0;j--)
            if(0<abs(i-j) && abs(i-j)<=2) host[i].push_back(j);
        for(int s=n-1;s>=0;s--) { vector<int> p{s}; dfs(p,1ULL<<s); }
        vector<pair<int,int>> edges;
        vector<vector<int>> ei(n,vector<int>(n,-1));
        for(int a=0;a<n;a++) for(int b=a+1;b<n;b++) if(b-a<=2) {
            ei[a][b]=ei[b][a]=edges.size(); edges.emplace_back(a,b);
        }
        int M=paths.size(), E=edges.size();
        assert(E<64);
        vector<uint64_t> masks(M);
        unordered_map<uint64_t,int> index;
        for(int i=0;i<M;i++) {
            uint64_t mask=0;
            for(int j=0;j<n-1;j++) mask|=1ULL<<ei[paths[i][j]][paths[i][j+1]];
            masks[i]=mask; assert(index.emplace(mask,i).second);
        }
        vector<vector<int>> graph(M);
        for(int i=0;i<M;i++) {
            uint64_t mask=masks[i];
            for(int u:{paths[i].front(),paths[i].back()}) for(int v:host[u]) {
                int add=ei[u][v]; if(mask>>add&1) continue;
                for(int cut=0;cut<E;cut++) {
                    auto [a,b]=edges[cut];
                    if((a!=v && b!=v) || !(mask>>cut&1)) continue;
                    uint64_t changed=(mask^(1ULL<<cut))|(1ULL<<add);
                    vector<vector<int>> adjacency(n);
                    for(int k=0;k<E;k++) if(changed>>k&1) {
                        auto [x,y]=edges[k]; adjacency[x].push_back(y); adjacency[y].push_back(x);
                    }
                    bool bad=false;
                    for(auto &q:adjacency) if(q.size()>2) bad=true;
                    if(bad) continue;
                    vector<int> q{0}; uint64_t seen=1;
                    for(int j=0;j<int(q.size());j++) for(int w:adjacency[q[j]])
                        if(!(seen>>w&1)) { seen|=1ULL<<w; q.push_back(w); }
                    if(int(q.size())!=n) continue;
                    graph[i].push_back(index.at(changed));
                }
            }
            sort(graph[i].begin(),graph[i].end());
            graph[i].erase(unique(graph[i].begin(),graph[i].end()),graph[i].end());
        }
        long long arcs=0;
        for(int u=0;u<M;u++) for(int v:graph[u]) {
            assert(binary_search(graph[v].begin(),graph[v].end(),u)); arcs++;
        }
        vector<int> distance(M), queue(M);
        map<int,int> spectrum; int diameter=0;
        for(int root=0;root<M;root++) {
            fill(distance.begin(),distance.end(),-1);
            distance[root]=0; queue[0]=root; int front=0,back=1,ecc=0;
            while(front<back) { int u=queue[front++]; for(int v:graph[u]) if(distance[v]<0) {
                distance[v]=distance[u]+1; ecc=max(ecc,distance[v]); queue[back++]=v;
            }}
            assert(back==M); spectrum[ecc]++; diameter=max(diameter,ecc);
        }
        out<<"{\"n\":"<<n<<",\"vertices\":"<<M<<",\"edges\":"<<arcs/2
           <<",\"diameter\":"<<diameter<<",\"eccentricity_histogram\":{";
        bool first=true; for(auto [ecc,count]:spectrum) {
            if(!first) out<<','; first=false; out<<'\"'<<ecc<<"\":"<<count;
        }
        out<<"},\"all_pairs\":true,\"edge_set_adjacency\":true}\n"; out.flush();
        cout<<"n="<<n<<" vertices="<<M<<" diameter="<<diameter<<" PASS\n";
    }
}
