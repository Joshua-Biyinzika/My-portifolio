

// selecting elements from the dom

var closeBtn = document.getElementById('close');

var openBtn = document.getElementById('open');


// adding event listeners

closeBtn.addEventListener('click', closeNav);

openBtn.addEventListener('click', openNav);


//event listener functions

function closeNav(){
    document.getElementById('mySidenav').style.width = '0'
}

function openNav(){
    document.getElementById('mySidenav').style.width = '250px'
}
































