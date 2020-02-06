#include <stdio.h>
#include <stdlib.h>
using namespace std;
 
int N;
 
typedef struct BiTree
{
    int Data;
    struct BiTree* left, *right;
}BiTree;

BiTree* CreatTree(int data1[], int data2[], int start, int ends, int &ind)
{
 
    int mid = data1[ind];
    int i;
    for(i = ends; i >= start; i--)
    {
        if(mid == data2[i])
            break;
    }
    BiTree *root = (BiTree*)malloc(sizeof(BiTree));
    root->Data = mid, root->right = NULL, root->left = NULL; 
    if(i + 1 <= ends)
    {
        root->right = CreatTree(data1, data2, i + 1, ends, --ind);
    }
    if(i - 1 >= start)
    {
        root->left = CreatTree(data1, data2, start, i - 1, --ind);
    }
    return root;
}
 
void Preorder(BiTree* key)
{
    if(key)
    {
        printf(" %d", key->Data);
        Preorder(key->left);
        Preorder(key->right);
    }
}
 
int main()
{
    scanf("%d", &N);
    int K1[100], K2[100];// K1 hou xu   K2 zheng xu
    int i;
    for(i = 0; i < N; i++)
    {
        int n;
        scanf("%d", &n);
        K1[i] = n;
    }
    for(i = 0; i < N; i++)
    {
        int n;
        scanf("%d", &n);
        K2[i] = n;
    }
    BiTree *One;
    int k = N - 1;
    One = CreatTree(K1, K2, 0, N - 1, k);//建立二叉树
    printf("Preorder:");
    Preorder(One);//遍历二叉树
    printf("\n");
    return 0;
}