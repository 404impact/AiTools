//js codes for current condition when user hovers the text

//Unlimited power
function hovertrigger() {
    var power = document.getElementById("hov");
    // power.style.color = "#ecf0f1";
    power.innerHTML = "Ugh I don't want to watch 3 hrs long video!";
    power.style.textDecoration = "underline"
}

function hoverouttrigger() {

    var p = document.getElementById("hov");
    p.innerHTML = "YouTube Video Summariser";
    // p.style.color = "#ecf0f1"
    p.style.textDecoration = "none"
}

//Best Anime to watch
function animehoverin() {
    var anime = document.getElementById("best-anime");
    // anime.style.color = "#ecf0f1";
    anime.innerHTML = "Do I really need to read those long paras?";
    anime.style.textDecoration = "underline"
}

function animehoverout() {
    var anime = document.getElementById("best-anime");
    anime.innerHTML = "AI Webpage Summariser";
    // anime.style.color = "#ecf0f1"
    anime.style.textDecoration = "none"
}
//Facebook

function fb() {
    var fb = document.getElementById("fb");
    fb.innerHTML = "Notes making was never this easy";
    // fb.style.color = "#ecf0f1"
    fb.style.textDecoration = "underline";
    // fb.style.textAlign = "center";
}

function fbout() {
    var fb = document.getElementById("fb");
    fb.innerHTML = "AI Based Journal Application"
    // fb.style.color = "#ecf0f1"
    fb.style.textDecoration = "none"
}

// AI Based Weather

function win(){
    var weather = document.getElementById("weather");
    weather.innerHTML = "Can I go out for a walk right now?"
    // weather.style.color = "#ecf0f1"
    weather.style.textDecoration = "underline"
}

function wout(){
    var weather = document.getElementById("weather");
    weather.innerHTML = "AI Based Weather Application"
    // weather.style.color = "#ecf0f1"
    weather.style.textDecoration = "none"
}


// food scanner

function scannerin(){
    var scanner = document.getElementById("scanner");
    scanner.innerHTML = "Is this food healthy really for me?"
    // scanner.style.color = "#ecf0f1"
    scanner.style.textDecoration = "underline"
}

function scannerout(){
    var scanner = document.getElementById("scanner");
    scanner.innerHTML = "Barcode based AI FoodScanner"
    // scanner.style.color = "#ecf0f1"
    scanner.style.textDecoration = "none"
}
