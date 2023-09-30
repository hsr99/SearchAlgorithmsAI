#include <stdio.h>
#include <stdlib.h>
// maximum size of the graph
#define MAX_SIZE 100
// graph node
typedef struct Node {
    int data;
    int visited;
    struct Node* next;
} Node;
//graph
typedef struct Graph {
    int num_nodes;
    Node* nodes[MAX_SIZE];
} Graph;
//create a new node
Node* create_node(int data) {
    Node* new_node = (Node*) malloc(sizeof(Node));
    new_node->data = data;
    new_node->visited = 0;
    new_node->next = NULL;
    return new_node;
}
// add an edge between two nodes
void add_edge(Graph* graph, int src, int dest) {
    Node* new_node = create_node(dest);
    new_node->next = graph->nodes[src];
    graph->nodes[src] = new_node;
}
void dfs(Graph* graph, int node) {
    if (graph->nodes[node] == NULL) {
        return;
    }
    Node* temp = graph->nodes[node];
    printf("%d ", node);
    temp->visited = 1;
    while (temp != NULL) {
        int n = temp->data;
        if (graph->nodes[n]->visited == 0) {
            dfs(graph, n);
        }
        temp = temp->next;
    }
}
int main() {
    Graph* graph = (Graph*) malloc(sizeof(Graph));
    graph->num_nodes = 0;
    add_edge(graph, 0, 1);
    add_edge(graph, 0,3);

    dfs(graph,0);
}