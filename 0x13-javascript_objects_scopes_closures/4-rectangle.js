#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // create an empty object if w or h is invalid
      return;
    }
    this.width = w;
    this.height = h;
  }

  print() {
    if (!this.width || !this.height) {
      return;
    }
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate() {
    if (!this.width || !this.height) {
      return;
    }
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    if (!this.width || !this.height) {
      return;
    }
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
