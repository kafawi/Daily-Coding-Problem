#include "xor_linked_list.h"

#include <iostream>
#include <cassert> // for simple assertion tests()
#include <string>

#define BOOST_TEST_MODULE xor_linked_list_test
#include <boost/test/included/unit_test.hpp>


BOOST_AUTO_TEST_CASE( add_size_increasing_test ) {
  XorLinkedList<int> list;
  std::cout << "fresh initialize list:\n" << list << std::endl;
  BOOST_CHECK_EQUAL( list.size(), 0);
  list.add(1);
  std::cout << "after adding one element:\n" << list << std::endl;
  BOOST_CHECK_EQUAL(list.size(), 1);
  list.add(2);
  list.add(3);
  list.add(123);
  std::cout << "after adding three more elements:\n" << list << std::endl;
  BOOST_CHECK_EQUAL(list.size(), 4);
}


BOOST_AUTO_TEST_CASE( add_and_get_test ) {
  XorLinkedList<std::string> list;
  std::cout << "fresh initialize list:\n" << list << std::endl;
  list.add("a");
  std::cout << "after add(\"a\"):\n" << list << std::endl;
  BOOST_CHECK_EQUAL(list.get(0), "a");
  list.add("b");
  std::cout << "after add(\"b\"):\n" << list << std::endl;
  BOOST_CHECK_EQUAL(list.get(1), "b");
  list.add("c");
  std::cout << "after add(\"c\"):\n" << list << std::endl;
  BOOST_CHECK_EQUAL(list.get(2), "c");

  BOOST_CHECK_EXCEPTION(
    list.get(-1), 
    std::out_of_range, 
    [](const std::out_of_range& ex) {
      BOOST_CHECK_EQUAL(ex.what(), std::string("Index is out of range [0, 3[. - got: -1"));
      return true;
    }
  );

  BOOST_CHECK_EXCEPTION(
    list.get(3), 
    std::out_of_range,
    [](const std::out_of_range& ex) {
      BOOST_CHECK_EQUAL(ex.what(), std::string("Index is out of range [0, 3[. - got: 3"));
      return true;
    }
  );
}

struct A{
  int val_ {0};
  A(int val): val_(val) {}
  friend std::ostream& operator<<(std::ostream& out, const A& r){
    return out<< "A:" << r.val_;
  }
  friend bool operator==(const A& a, const A& b){
    return a.val_ == b.val_;
  }
};

BOOST_AUTO_TEST_CASE( referenced_typed_test ) {
  A a = *(new A(10));
  A b = *(new A(20));

  XorLinkedList<A&> list;
  list.add(a);
  BOOST_CHECK_EQUAL(list.get(0), a);
  list.add(b);
  BOOST_CHECK_EQUAL(list.get(1), b);
  std::cout << "liste with refences as element:\n" << list << std::endl;
  // are the elements also the same (same memory address)
  BOOST_CHECK_EQUAL(&(list.get(0)), &a);
  BOOST_CHECK_EQUAL(&(list.get(1)), &b);
}
