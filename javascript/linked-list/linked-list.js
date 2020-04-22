//
// This is only a SKELETON file for the 'Linked List' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

class Node {
  previous;
  value;
  next;

  constructor(val, previousNode = null, nextNode = null) {
    this.value = val;
    this.previous = previousNode;
    this.next = nextNode;
  }
}

export class LinkedList {
  first;
  last;

  push(value) {
    const newNode = new Node(value, this.last);
    this.last.next = newNode;
    this.last = newNode;
  }

  pop() {
    const last = this.last;
    if (this.last && this.last.previous) {
      this.last.previous.next = null;
      this.last = this.last.previous;
    }
    return last;
  }

  shift() {
    const first = this.first;
    if (this.first && this.first.next) {
      this.first.next.previous = null;
      this.first = this.first.next;
    }
    return first;
  }

  unshift() {
    throw new Error("Remove this statement and implement this function");
  }

  delete() {
    throw new Error("Remove this statement and implement this function");
  }

  count() {
    throw new Error("Remove this statement and implement this function");
  }
}
