#pragma once

#ifndef XOR_LINKED_LIST_H_
#define XOR_LINKED_LIST_H_

#include <iostream>
#include <stdexcept>      // std::out_of_range


template <typename T>
class XorLinkedList{
  private:
    struct Node{
        friend class XorLinkedList;
        T value_;
        void* both_ {nullptr}; 
        
        Node(T value):value_(value){};
        inline friend std::ostream& operator<<(std::ostream& out, const Node& r)
        {
          return out<< "[" << r.value_ << " , " << r.both_ << "]";
        }
    };
  private:
    Node* head_ {nullptr};
    Node* tail_ {nullptr};
    int size_{0};
  public:
    ~XorLinkedList();
    void add(T element);
    T get(int index);
    int size(){return size_;}

    template <typename U>
    friend std::ostream& operator<<(std::ostream& out, const XorLinkedList<U>& l);
};

// -------------------------------- implementation in the header, -> linker problems otherwise
template<typename T>
void 
XorLinkedList<T>::add(T element)
{
  Node* node = new Node(element);
  if (size_ < 1){
    head_ = node;
  } else {
    Node* prev = tail_;
    prev->both_ = (Node*)((long)(prev->both_) ^ (long)node);
    node->both_ = prev;  
  }
  tail_ = node;
  size_++;
  return;
}

template <typename T>
T 
XorLinkedList<T>::get(int index)
{
  if (0 > index || size_ -1 < index) {
        throw std::out_of_range("Index is out of range [0, " + std::to_string(size_) + "[. - got: " + std::to_string(index));
  }
  Node* node = head_;
  Node* prev = nullptr;
  for (int i = 0; i<index; i++){
    Node* next = (Node*)((long)(node->both_) ^ (long)prev);
    prev = node;
    node = next;
  }
  return node->value_;
}

template <typename T>
std::ostream& 
operator<<(std::ostream& out, const XorLinkedList<T>& l)
{
  using Node = struct XorLinkedList<T>::Node;
  out << "[" << std::endl;
  Node* node = l.head_;
  Node* prev = nullptr;
  while (node != nullptr){
    out << "\t" << *node << std::endl;
    Node* next = (Node*)((long)(node->both_) ^ (long)prev);
    prev = node;
    node = next;
  }
  out << "]";
  return out;
}

template <typename T>
XorLinkedList<T>::~XorLinkedList(void){
  Node* node = head_;
  Node* prev = nullptr;
  while (node != nullptr){
    Node* delNode = node;
    Node* next = (Node*)((long)(node->both_) ^ (long)prev);
    prev = node;
    node = next;
    delete delNode; 
  }
}

#endif  // XOR_LINKED_LIST_H_