

/*==========================
    TOGGLE PROFILE TAB
==========================*/

// Toggle profile tab hidden div
$('#profile').click( (event) => {
    $('.paper-profile').fadeToggle('fast');
});



/*==========================
    FADE AND SLIDE ANIMATION
==========================*/

if (window.location.href.endsWith('leaderboard') || window.location.href.endsWith('game') ) {
    let margin = 100;
    let opacity = 0;
    
    function fadeSlideIn() {
        margin -= 5;
        opacity += 0.050;
        element.style.marginTop = margin + 'px';
        element.style.opacity = opacity;
        
        if (opacity >= 1) {
            clearInterval(animation)
        }
    }
    
    const element = document.querySelector('.fade-slide-in');
    const animation = setInterval(fadeSlideIn, 10);
}
