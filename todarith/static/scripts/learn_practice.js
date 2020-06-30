

var answerSpan = document.getElementById('answer');
var answerMathField = MQ.MathField(answerSpan, {
  handlers: {
    edit: function() {
      enteredAnswer = answerMathField.latex(); // Get entered math in LaTeX format
    }
  }
});

var problems
var selectedCategory = 1;
var selectedDifficulty = 1;
var selectedTime = 1;
var problemIndex = 0;
var score = 0;
var ansCount = 0;
var streak = 0;
var time = 0;
prob = document.getElementById('practiceProblem');

$( window ).on( "load", function() {
  $.getJSON($SCRIPT_ROOT + '/learn/practice/_get_problems', {
    category: selectedCategory,
    difficulty: selectedDifficulty,
    time: selectedTime
  }, function(data) {
    problems = data.problems;
    console.log(problems)
    //$("#practiceProblem").text("$$"+ problems[problemIndex]["problem"] + "$$");
    katex.render((problems[problemIndex]["problem"]), prob, {
      throwOnError: false
    });
  });
  return false;
});

function checkAnswer() {
  if (enteredAnswer==problems[problemIndex]["answer"]) {
    score++;
    streak++;
    problemIndex++;
  } else {
    streak = 0;
    problemIndex++;
  }
  ansCount++;
  updateProbStats();
}
function updateProbStats() {
  katex.render((problems[problemIndex]["problem"]), prob, {
    throwOnError: false
  });
  answerMathField.select();
  answerMathField.write("");
  document.getElementById('streakValue').innerHTML = streak;
  document.getElementById('scoreValue').innerHTML = (score+"/"+ansCount);
}

/*
var enteredAnswer;
$(function() {
  $('button#btn_submit').bind('click', function() {
    console.log("activated")
    $.getJSON($SCRIPT_ROOT + '/learn/practice/_get_answer_input', {
      answer: enteredAnswer
    }, function(data) {
      $("#answer").text(data.answer);
    });
    return false;
  });
});
*/
