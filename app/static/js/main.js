
/*======================================

    For this project JavaScript has only been used to
    enhance the look and feel of some elements, such
    as fading or sliding an element for a visual effect.

    As this single JS file will be used over all html pages
    it was necessary to enclose function in if statements
    with a condition based on url to ensure that the
    no errors would appear on pages not containing
    the particualr element selected. 

======================================*/



/*======================================
*   TOGGLE USER PROFILE TAB - ON / OFF
*======================================*/

$('#profile').click( () => {
    $('.paper-profile').fadeToggle('fast');
});



/*======================================
*   ANIMATION TO CREATE A SLIDE IN / UP EFFECT
*======================================*/

if (window.location.href.endsWith('leaderboard') || window.location.href.endsWith('game')) {
    
    // select elements and setInterval of 10ms
    const element = document.querySelector('.fade-slide-in');
    const animation = setInterval(fadeSlideIn, 10);

    // assign initial values
    let margin = 100;
    let opacity = 0;
    
    // animation function
    function fadeSlideIn() {

        // adjust style values
        margin -= 5;
        opacity += 0.050;
        element.style.marginTop = margin + 'px';
        element.style.opacity = opacity;
        
        // stop the animation when opacity is complete
        if (opacity >= 1) {
            clearInterval(animation)
        };
    };
};



/*======================================
*  AUTOFOCUS INPUT & TIMER FUNCTION - GAME.HTML
*======================================*/

if (window.location.href.endsWith('game')) {

    // automatically focus the input on page load
    const input = document.querySelector('#input').focus();
  
    // select time element
    const currentTime = document.querySelector('#current-time');

    // increase timer by 1s each interval of 1s
    setInterval( () => {
        let seconds = parseInt(currentTime.innerText) + 1;
        currentTime.innerHTML = seconds;
    }, 1000);
};
