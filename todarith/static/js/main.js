function removeSkill(skillId, probId) {
  $.getJSON($SCRIPT_ROOT + '/db/_remove_skill', {
    skillId: skillId,
    probId: probId,
  }, function(data) {
  });
  skillListItem= document.getElementById("sortSkill_" + skillId.toString())
  skillListItem.parentNode.removeChild(skillListItem);
  console.log("Skill Removed");
}

function addSkill() {
  console.log(selectedSkillId + " added");
  if (curProbId != undefined ) {
    probId = curProbId;
  } else {
    console.log("no skill selected")
  }
  $.getJSON($SCRIPT_ROOT + '/db/_add_skill', {
    probId: probId,
    skillId: selectedSkillId,
  }, function(data) {
    displaySkill(data.name, data.id);
  });
}

function createSkill() {
  $.getJSON($SCRIPT_ROOT + '/db/_create_skill', {
    skillName: document.querySelector('#sort_addSkillQuery').value,
  }, function(data) {
    selectedSkillId = data.id;
    addSkill()
  });
}
