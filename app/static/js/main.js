

/*==========================
    TOGGLE PROFILE TAB
==========================*/

// Toggle profile tab hidden div
$('#profile').click( () => {
    $('.paper-profile').fadeToggle('fast');
});



/*==========================
    FADE AND SLIDE ANIMATION
==========================*/

if (window.location.href.endsWith('leaderboard') || window.location.href.endsWith('game') ) {
    let margin = 100;
    let opacity = 0;
    
    function fadeSlideIn() {
        margin -= 2.5;
        opacity += 0.025;
        element.style.marginTop = margin + 'px';
        element.style.opacity = opacity;
        
        if (opacity >= 1) {
            clearInterval(animation)
        }
    }
    
    const element = document.querySelector('.fade-slide-in');
    const animation = setInterval(fadeSlideIn, 10);
}



/*==========================
    CURRENT GAME TIME TICK
==========================*/

if (window.location.href.endsWith('game')) {
    const currentTime = document.querySelector('#current-time');
    setInterval( () => {
        let seconds = parseInt(currentTime.innerText) + 1;
        currentTime.innerHTML = seconds;
    }, 1000);
}
