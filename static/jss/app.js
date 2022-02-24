let text = [" БУХГАЛТЕРСКИЕ УСЛУГИ В ТАШКЕНТЕ"];
let i = 0;
let speed = 100;
let speedLast = 1000;

let typingTextIndex = 0;

function type() {
  document.getElementById("hero").innerHTML += text[typingTextIndex].charAt(i);
  i++;
  setTimeout(
    () => {
      if (i >= text[typingTextIndex].length) {
        erease();
      } else {
        type();
      }
    },
    i == text[typingTextIndex].length ? speedLast : speed
  );
}
type();

function erease() {
  document.getElementById("hero").innerHTML = document
    .getElementById("hero")
    .innerHTML.substr(0, document.getElementById("hero").innerHTML.length - 1);
  i--;
  setTimeout(() => {
    if (i <= 0) {
      if (typingTextIndex >= text.length - 1) {
        typingTextIndex = 0;
      } else {
        typingTextIndex++;
      }
      type();
    } else {
      erease();
    }
  }, speed);
}

// CODS FOR WHY__US
const ANIMATEDCLASSNAME = "animated";
const ELEMENTS = document.querySelectorAll(".HOVER");
const ELEMENTS_SPAN = [];

ELEMENTS.forEach((element, index) => {
  let addAnimation = false;
  // Elements that contain the "FLASH" class, add a listener to remove
  // animation-class when the animation ends
  if (element.classList[1] == "FLASH") {
    element.addEventListener("animationend", (e) => {
      element.classList.remove(ANIMATEDCLASSNAME);
    });
    addAnimation = true;
  }

  // If The span element for this element does not exist in the array, add it.
  if (!ELEMENTS_SPAN[index])
    ELEMENTS_SPAN[index] = element.querySelector("span");

  element.addEventListener("mouseover", (e) => {
    ELEMENTS_SPAN[index].style.left = e.pageX - element.offsetLeft + "px";
    ELEMENTS_SPAN[index].style.top = e.pageY - element.offsetTop + "px";

    // Add an animation-class to animate via CSS.
    if (addAnimation) element.classList.add(ANIMATEDCLASSNAME);
  });

  element.addEventListener("mouseout", (e) => {
    ELEMENTS_SPAN[index].style.left = e.pageX - element.offsetLeft + "px";
    ELEMENTS_SPAN[index].style.top = e.pageY - element.offsetTop + "px";
  });
});

AOS.init();

// CODS FOR MORE DIV TEXT
function More1() {
  document.getElementById("more1").classList.toggle("showdiv");
}

// CODS FOR SCROLL
let myVar = setInterval(myscroll, 10);
function myscroll() {
  let y = window.scrollY;
  if (y > 0) {
    document.getElementById("shadow__scroll").style.boxShadow =
      "1px 1px 1px rgba(0, 0, 0, 0.1)";
    document.getElementById("navbar__scrol").style.padding = "5px 0px";
    document.getElementById("menu__scroll").style.padding = "10px 0px";
  }
  if (y === 0) {
    document.getElementById("shadow__scroll").style.boxShadow =
      "0px 0px 0px white";
    document.getElementById("navbar__scrol").style.padding = "20px 0px";
    document.getElementById("menu__scroll").style.padding = "15px 0px";
  }
}

function myFunction(x) {
  if (x.matches) {
    // If media query matches
    document.getElementById("truemenu").style.transform =
      "translate3d(0px, 32px, 0px)";
  }
}

var x = window.matchMedia("(max-width: 420px)");
myFunction(x);
x.addListener(myFunction);

// CODS FOR PRICE BTN

function myModal() {
  let myrResulr = document.getElementById("exampleModal1");
  if (myrResulr.style.display === "block") {
    document.getElementById("dc_1").classList.add("myactive");
    document.getElementById("slide_down").classList.add("myactive");
    document.getElementById("dc_s1").classList.add("myactive_s");
  } else {
    document.getElementById("dc_1").classList.remove("myactive");
    document.getElementById("slide_down").classList.remove("myactive");
    document.getElementById("dc_s1").classList.remove("myactive_s");
    
  }
}
let myremv = setInterval(myModal, 20);

function myModal2() {
  
  let myrResulr2 = document.getElementById("exampleModal2");
  if (myrResulr2.style.display === "block") {
    document.getElementById("dc_2").classList.add("myactive");
    document.getElementById("slide_down2").classList.add("myactive");
    document.getElementById("dc_s2").classList.add("myactive_s");
  } else {
    document.getElementById("dc_2").classList.remove("myactive");
    document.getElementById("slide_down2").classList.remove("myactive");
    document.getElementById("dc_s2").classList.remove("myactive_s");
  }
}
let myremv2 = setInterval(myModal2, 20);

function myModal3() {
  let myrResulr3 = document.getElementById("exampleModal3");
  if (myrResulr3.style.display === "block") {
    document.getElementById("dc_3").classList.add("myactive");
    document.getElementById("slide_down3").classList.add("myactive");
    document.getElementById("dc_s3").classList.add("myactive_s");
  } else {
    document.getElementById("dc_3").classList.remove("myactive");
    document.getElementById("slide_down3").classList.remove("myactive");
    document.getElementById("dc_s3").classList.remove("myactive_s");
  }
}
let myremv3 = setInterval(myModal3, 20);

function myModal4() {
  let myrResulr4 = document.getElementById("exampleModal4");
  if (myrResulr4.style.display === "block") {
    document.getElementById("dc_4").classList.add("myactive");
    document.getElementById("slide_down4").classList.add("myactive");
    document.getElementById("dc_s4").classList.add("myactive_s");
  } else {
    document.getElementById("dc_4").classList.remove("myactive");
    document.getElementById("slide_down4").classList.remove("myactive");
    document.getElementById("dc_s4").classList.remove("myactive_s");
  }
}
let myremv4 = setInterval(myModal4, 20);






