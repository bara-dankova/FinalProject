let daysItem = document.querySelector("#days");
let hoursItem = document.querySelector("#hours");
let secsItem = document.querySelector("#mins");
let minsItem = document.querySelector("#secs");

let countDown = () => {
    let futureDate = new Date("18 May 2021");
    let currentDate= new Date();
    let myDate = futureDate - currentDate;

    let days = Math.floor(myDate/ 1000 / 60 / 60 / 24);
    let hours = Math.floor(myDate/ 1000 / 60 / 60) % 24;
    let mins = Math.floor(myDate/ 1000 / 60) % 60;
    let secs = Math.floor(myDate/ 1000) % 60;

    daysItem.innerHTML = days;
    hoursItem.innerHTML = hours;
    secsItem.innerHTML = mins;
    minsItem.innerHTML = secs;
}

countDown()

setInterval(countDown, 1000)