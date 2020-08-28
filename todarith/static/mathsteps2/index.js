const ChangeTypes = require('./lib/ChangeTypes');
const factor = require('./lib/factor');
const simplifyExpression = require('./lib/simplifyExpression');
const solveEquation = require('./lib/solveEquation');

module.exports = {
  factor,
  simplifyExpression,
  solveEquation,
  ChangeTypes,
};

const mathsteps = require('mathsteps');

const steps = mathsteps.solveEquation(process.argv[2]);
var ans = "";
steps.forEach(step => {
    ans = step.newEquation.ascii();
});

//console.log(process.argv);
console.log(ans);
