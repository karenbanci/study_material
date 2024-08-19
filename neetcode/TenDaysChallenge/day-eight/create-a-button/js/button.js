const clickMeButton = document.createElement("Button");

clickMeButton.id = "btn";
clickMeButton.innerHTML = 0;

document.body.appendChild(clickMeButton);

// clickMeButton.onclick = function () {
//   this.innerHTML = "you clicked";
// };
let sum = 0;
clickMeButton.addEventListener("click", function () {
  sum++;
  this.innerHTML = sum;
});
