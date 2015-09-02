//problem: user interaction doesnt provide desired results
//solution: add interactivity so the user can manage daily task
var taskInput = document.getElementById("new-task");
var addButton = document.getElementsByTagName("button")[0]; //first button on the page
var incompleteTasksHolder = document.getElementById("incomplete-tasks");
var completedTasksHolder = document.getElementById("completed-tasks");

//New Task List Item
var createNewTaskElement = function(taskString) {
  //create list item 
  var listItem = document.createElement("li");
  //input checkbox
  var checkBox = document.createElement("input"); //checkbox
  //label
  var label = document.createElement("label");
  //input text
  var editInput = document.createElement("input");
  // creat button.edit
  var editButton = document.createElement("button");
  //create button.delete
  var deleteButton = document.createElement("button");
  //each elements needs modfying
  checkBox.type = "checkbox";
  editInput.type = "text";

  editButton.innerText = "Edit";
  editButton.className = "edit";
  deleteButton.innerText = "Delete";
  deleteButton.className = "delete";

  label.innerText = taskString;


  //each elements needs appending
  listItem.appendChild(checkBox);
  listItem.appendChild(label);
  listItem.appendChild(editInput);
  listItem.appendChild(editButton);
  listItem.appendChild(deleteButton);
  return listItem
}

//Add a new task
var addTask = function() {
    console.log("Add task..");
    //create a new list item with the text from the #new-task
    var listItem = createNewTaskElement(taskInput.value)
      //Append listItem to incompletetaskholder
    incompleteTasksHolder.appendChild(listItem)
    bindTaskEvents(listItem, taskCompleted);
    
    taskInput.value = " ";
  }


  //Edit an existing task
var editTask = function() {
  console.log("Edit task..");
  var listItem = this.parentNode;

  var editInput = listItem.querySelector("input[type=text]");
  var label = listItem.querySelector("label");
  var containsClass = listItem.classList.contains("editMode")
  //if the class of the parent is .editmode
  if(containsClass) {
  //switch from .editmode
  //label text become input's value
  label.innerText = editInput.value;
  } else {
    editInput.value = label.innerText;
  //switch to .editmode
  // input value becomes the label's test
}
listItem.classList.toggle("editMode");
  //toggle .editMode on listItem
}



//Delete task
var deleteTask = function() {
  console.log("delete task..");
  var listItem = this.parentNode;
  var ul = listItem.parentNode;
  ul.removeChild(listItem);
  //remove the parent list item from the ul

}

//Mark task as complete
var taskCompleted = function() {
  console.log("task complete..");
  //append the task list item to the #completed-tasks
  var listItem = this.parentNode;
  completedTasksHolder.appendChild(listItem);
  bindTaskEvents(listItem, taskIncomplete);
}

var taskIncomplete = function() {
  console.log("task incomplete..");
  var listItem = this.parentNode;
  incompleteTasksHolder.appendChild(listItem);
  //append the task list item to the #incompleted-tasks
  bindTaskEvents(listItem, taskCompleted);
}

var bindTaskEvents = function(taskListItem, checkBoxEventHandler) {
  console.log("Bind list item events");
  //select listitems children
  var checkBox = taskListItem.querySelector("input[type=checkbox]");
  var editButton = taskListItem.querySelector("button.edit");
  var deleteButton = taskListItem.querySelector("button.delete");
  //bind editTask to edit button
  editButton.onclick = editTask;
  // bind deleteTask to the to delete button
  deleteButton.onclick = deleteTask;
  // bind checkBoxEventHandler to the checkbox
  checkBox.onchange = checkBoxEventHandler;
}

//set the click handler to the add task function 
addButton.addEventListener("click", addTask);


//cycle over the incompleteTasksHolder ul items
for (var i = 0; i < incompleteTasksHolder.children.length; i++) {
  //bind events to list items children (taskCompleted)
  bindTaskEvents(incompleteTasksHolder.children[i], taskCompleted);
}



//cycle over the completeTasksHolder ul items
for (var i = 0; i < completedTasksHolder.children.length; i++) {
  //bind events to list items children (taskCompleted)
  bindTaskEvents(completedTasksHolder.children[i], taskIncomplete);

}