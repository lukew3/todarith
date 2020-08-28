var curProbId = document.getElementById("hiddenId").innerHTML;

console.log(curProbId);
//console.log({{ problem.id }});
//var curProbId = {{ problem.id }};//some problem here
var selectedSkillId = 0;

function displaySkill(name, id) {
  var temp = document.querySelector('template').content;
  var li = temp.querySelector('li');
  var text_to_change = li.childNodes[0];
  text_to_change.nodeValue = name;
  li.id = "sortSkill_" + id;
  if (li.childNodes[1] != undefined) {
    li.removeChild(li.childNodes[1])
  }
  var a = document.createElement("a");
  curProbIdString = "'" + curProbId.toString() + "'";
  a.innerHTML = '<a style="color: blue" href="#" onclick="removeSkill(' + id.toString() + ', ' + curProbIdString + ')"> remove</a>';
  li.appendChild(a);
  document.querySelector('#skillsList').appendChild(document.importNode(temp, true));
}

$(function() {
  $('button#btn_flag').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/db/_flag_problem', {
      //nada
    }, function(data) {
      //nope
    });
    return false;
  });
});

$(function() {
  $('button#btn_next').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/db/sort/_next_problem', {
      //zip
    }, function(data) {
      console.log(data)
       document.getElementById("sort_problem").innerHTML = data.problem;
       document.getElementById("sort_answer").innerHTML = data.answer;
       curProbId = data.id;

       //Clear skills and add new ones
       document.getElementById("skillsList").innerHTML = "";
       skills = data.skills
       console.log(skills)
       console.log(data.skills[0].skillName)
       skillsLen = Object.keys(data.skills).length
       for (i = 0; i < skillsLen; i++) {
         displaySkill(data.skills[i].skillName, data.skills[i].skillId);
       }
    });
    return false;
  });
});


function queryEdited() {
  const queryBox = document.querySelector('#sort_addSkillQuery');
  query = queryBox.value
  $.getJSON($SCRIPT_ROOT + '/db/_get_skill_query', {
    query: query,
  }, function(data) {
    queryResults = data.returnSkills;
      document.getElementById('sort_queryResult').innerHTML = (queryResults[0].name)
      selectedSkillId = queryResults[0].id;
  });
}
