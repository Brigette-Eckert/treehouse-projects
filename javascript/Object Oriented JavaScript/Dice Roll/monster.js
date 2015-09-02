function Monster(name) {
  this.name = name;
  this.health = 100;

}

Monster.prototype.takeDamage = function takeDamage () {
    this.health--;
}