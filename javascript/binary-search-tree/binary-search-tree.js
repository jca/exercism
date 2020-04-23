export class BinarySearchTree {

  constructor(value) {
    this.value = value;
    this.branches = {};
  }

  get data() {
    return this.value;
  }

  get right() {
    return this.branches.right || null
  }

  get left() {
    return this.branches.left || null
  }

  insert(value) {
    const side = value <= this.value ? 'left' : 'right'

    if (this.branches[side]) {
      this.branches[side].insert(value)
    }  else {
      this.branches[side] = new BinarySearchTree(value)
    }
  }

  each(callback) {
    this.branches.left && this.branches.left.each(callback)
    callback(this.value)
    this.branches.right && this.branches.right.each(callback)
  }
}
