// Initial variables connected to the DOM
const container = document.querySelector('div#container');
const body = container.querySelector('div#body');
const drop_btn = container.querySelector('button#drop-btn');
var drop_icon = drop_btn.querySelector('i');
const drop_cnt = container.querySelector('div#drop-cnt');
var nav_linq = drop_cnt.querySelectorAll('a#drop-linq');

//SCRIPT TO CAUSE A DROPDOWN ON SCREENS LESS THAN 500PX
body.addEventListener('click', closeNav)
drop_btn.addEventListener("click", slideDownNav);

function slideDownNav() {
    if (!drop_cnt.classList.contains('max-sm:mt-10')) {
        drop_cnt.classList.add('max-sm:mt-10');
        drop_btn.classList.add('bg-black-300');
        drop_icon.classList.replace("fa-ellipsis-h", "fa-times")
        body.classList.add('opacity-25');

        for (i=0; i<nav_linq.length; i++) {
            nav_linq[i].addEventListener('click', closeNav);
        };
    }
    else {
        drop_cnt.classList.remove('max-sm:mt-10');
        drop_btn.classList.remove('bg-black-300');
        body.classList.remove('opacity-25');
        drop_icon.classList.replace("fa-times", "fa-ellipsis-h")
    };
}

function closeNav() {
    drop_cnt.classList.remove('max-sm:mt-10');
    drop_btn.classList.remove('bg-black-300');
    body.classList.remove('opacity-25');
    drop_icon.classList.replace("fa-times", "fa-ellipsis-h");
}

// SCRIPT TO CHANGE BACKGROUND COLOR OF NAVIGATION LINKS
// WHEN CLICKED
for (i=0; i<nav_linq.length; i++) {
    nav_linq[i].addEventListener('click', NavCol);
}

function NavCol(evt) {
    for (i=0; i<nav_linq.length; i++) {
        nav_linq[i].classList.remove("bg-black-300");
    };
    evt.currentTarget.classList.add("bg-black-300");
}











