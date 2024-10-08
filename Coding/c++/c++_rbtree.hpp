/*
C++ RBTree
@author Dunhe
*/

#ifndef _RED_BLACK_TREE_HPP_
#define _RED_BLACK_TREE_HPP_

#include <iomanip>
#include <iostream>
using namespace std;

enum RBTColor{RED, BLACK};

template <class T>
class RBTNode {
    public:
        RBTColor color;
        T key;
        RBTNode *left;
        RBTNode *right;
        RBTNode *parent;

        RBTNode(T value, RBTColor c, RBT Node *p, RBTNode *l, RBTNode *r):
            key(value), color(c), parent(), left(l), right(r) {}
};

template<class T>
class RBTree {
private:
    RBTNode<T> *mRoot;

public:
    RBTree();
    ~RBTree();

    void preOrder(); // pre order of red black tree
    void inOrder(); // in order of red black tree
    void postOrder(); // post Order of red black tree

    RBTNode<T>* search(T key); // non iterative search for key
    RBTNode<T>* iterativeSearch(T key); // iterative search for key

    T minimum(); // find minimum
    T maximum(); // find maximum

    void insert(T key); // insert key
    void remove(T key); // remove key
    void destroy(); // destroy red black tree
    void print(); // print red black tree

private:
    void preOrder(RBTNode<T>* tree) const;
    void inOrder(RBTNode<T>* tree) const;
    void postOrder(RBTNode<T>* tree) const;

    RBTNode<T>* search(RBTNode<T>* x, T key) const;
    RBTNode<T>* iterativeSearch(RBTNode<T>* x, T key) const;

    RBTNode<T>* minimum(RBTNode<T>* tree);
    RBTNode<T>* maximum(RBTNode<T>* tree);

    RBTNode<T>* successor(RBTNode<T> *x);
    RBTNode<T>* predecessor(RBTNode<T> *x);

    void leftRotate(RBTNode<T>* &root, RBTNode<T>* x);
    void rightRotate(RBTNode<T>* &root, RBTNode<T>* y);
    void insert(RBTNode<T>* &root, RBTNode<T>* node);
    void insertFixUp(RBTNode<T>* &root, RBTNode<T>* node);
    void remove(RBTNode<T>* &root, RBTNode<T>* node);
    void removeFixUp(RBTNode<T>* &root, RBTNode<T> *node, RBTNode<T> *parent);
    void destroy(RBTNode<T>* &tree);
    void print(RBTNode<T>* tree, T key, int direction);

#define rb_parent(r)   ((r)->parent)
#define rb_color(r) ((r)->color)
#define rb_is_red(r)   ((r)->color==RED)
#define rb_is_black(r)  ((r)->color==BLACK)
#define rb_set_black(r)  do { (r)->color = BLACK; } while (0)
#define rb_set_red(r)  do { (r)->color = RED; } while (0)
#define rb_set_parent(r,p)  do { (r)->parent = (p); } while (0)
#define rb_set_color(r,c)  do { (r)->color = (c); } while (0)
};


/* Constructor function*/
template <class T>
RBTree<T>::RBTree():mRooot(NULL) {
    //TODO fill in constructor function
}

/* Destructor function */
template <class T>
RBTree<T>::~RBTree() {
    // TODO fill in destructor function
}

/* pre order rbtree */
template <class T>
void RBTree<T>::preOrder(RBTNode<T>* tree) const {
    // TODO fill in pre order function
    // 1. cout each key in pre order
    // 2. Finish pre order algorithm
}

template <class T>
void RBTree<T>::preOrder() {
    preOrder(mRoot);
}

/* in order rbtree */
template <class T>
void RBTree<T>::inOrder(RBTNode<T>* tree) const {
    // TODO fill in in order function
    // 1. cout each key in in order
    // 2. Finish in order algorithm
}

template<class T>
void RBTree<T>::inOrder() {
    inOrder(mRoot);
}

/* post order rbtree*/
template <class T>
void RBTree<T>::postOrder(RBTNode<T> *tree) const {
    // TODO fill in post order function
    // 1. cout each key in post order
    // 2. finish post order algorithm
}

template <class T>
void RBTree<T>::postOrder() {
    postOrder(mRoot);
}

/* search for key in rbtree */
template <class T>
RBTNode<T>* RBTree<T>::search(RBTNode<T>* x, T key) const {
    // TODO fill in search function
    // 1. check if current rbtnode is null or equals key
    // 2. rbtree has attribute left child key less than current node
    // 3. rbtree has attribute
    // 4. write function in recursive way
}


template <class T>
RBTNode<T>* RBTree<T>::iterativeSearch(RBTNode<T>* x, T key) const {
    // TODO fill in iterative search function
    // 1. do not recursively call iterativesearch
}

template <class T>
RBTNode<T>* RBTree<T>::iterativeSearch(T key) {
    iterativeSearch(mRoot, key);
}

/* minimum of rbtree node */
template <class T>
RBTNode<T>* RBTree<T>::minimum(RBTNode<T>* tree) {
    // TODO fill in minimum function
    // find the minimum of rbtree
    // 1. notice that do not use extra space
}

template <class T>
T RBTree<T>::minimum() {
    RBTNode<T> *p = minimum(mRoot);
    if (p != NULL)
        return p->key;
    return (T)NULL;
}

/* maximum of rbtree node */
template <class T>
RBTNode<T>* RBTree<T>::maximum(RBTNode<T>* tree) {
    // TODO fill in maximum function
    // find the maximum of rbtree
    // 1. notice that do not use extra space
}

/* successor of rbtree node */
template <class T>
RBTNode<T>* RBTree<T>::successor(RBTNode<T> *x) {
    // If exist right child, then the successor should be
    // "the smallest key node of the subtree of the right child"


    // If do not exist right child:
    //      1. if current node x is a left child, 
    //          then its successor should be its parent node
    //      2. if current node x is a right child,
    //          then find the lowest parrent node which has left child


}


/* predecessor of rbtree node */
template <class T>
RBTNode<T>* RBTree<T>::predecessor(RBTNode<T> *x) {
    // if node x has left child, then the predecessor of node x should be
    // the maximum key node of subtree of left child of node x

    // if node x has no left child:
    //      1. if current node x is a right child,
    //          then its predecessor should be its parent node
    //      2. if current node x is a left child
    //          then find the lowest parrent node which has a right child 
}

/*
leftRotate function
*      px                              px
*     /                               /
*    x                               y
*   /  \    --(left rotate)-->      / \
*  lx   y                          x  ry
*     /   \                       /  \
*    ly   ry                     lx  ly
*/
template <class T>
void RBTree<T>::leftRotate(RBTNode<T>* &root, RBTNode<T> *x) {
    // TODO fill in the left rotate function according to the diagram
    // 
}

/*
rightRotate function

*            py                               py
*           /                                /
*          y                                x
*         /  \   --(right rotate)-->       /  \
*        x   ry                           lx   y
*       / \                                   / \
*      lx  rx                                rx  ry

 */
template <class T>
void RBTree<T>::rightRotate(RBTNode<T>* &root, RBTNode<T>* y) {
    // TODO
}

/* insertFixUp function */
template <class T>
void RBTree<T>::insertFixUp(RBTNode<T>* &root, RBTNode<T>* node) {
    // TODO
}

/* insert function */
template <class T>
void RBTree<T>::insert(RBTNode<T>* &root, RBTNode<T>* node) {
    // TODO
}

/* removeFixUp function */
template <class T>
void RBTree<T>::removeFixUp(RBTNode<T>* &root, RBTNode<T> *node, RBTNode<T> *parent) {
    
}

/* remove function */
template <class T>
void RBTree<T>::remove(RBTNode<T>* &root, RBTNode<T> *node) {
    RBTNode<T> *child, *parent;
    RBTColor color;

}

# endif