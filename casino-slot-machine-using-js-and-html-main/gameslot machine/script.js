let value1 = document.getElementById('value1')
let value2 = document.getElementById('value2')
let value3 = document.getElementById('value3')

let inSpeed = document.getElementById('inpSpeed')
let stopButton=document.getElementById('stopButton')
let spinButton=document.getElementById('spinButton')
let value=document.getElementsByClassName('value')

let values = [
    '😃', '😇:', '😊', '🤭', '😎', '😢', '😠'
]
function getRandomValue(){
    return values[Math.floor(Math.random() * 7)]
}

let animationId;

function updateAnimation(newSpeed){
    if(animationId) clearInterval(animationId)
    animationId = setInterval(() => {
        value1.innerText = getRandomValue()
        value2.innerText = getRandomValue()
        value3.innerText = getRandomValue()
    }, 1000 / newSpeed)

}
function check()
{
    if(value1 === value2 === value3)
    alert("winner")
    else
    alert("loser")
}
$(document).ready(function(){
   
    $("#stopButton").click(function(){
      clearInterval(animationId)
          $(".value").css("animation-play-state", "paused");
    });
    $("#spinButton").click(function(){
        $(".value").css("animation-play-state", "running");
    });
});

inSpeed.onchange = function(ev){
   // console.log('value changed', ev.target.value)
    document.documentElement.style.setProperty('--speed', ev.target.value)
    updateAnimation(ev.target.value)
}