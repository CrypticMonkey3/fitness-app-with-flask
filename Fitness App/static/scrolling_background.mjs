$(function() {
    var x = 0;
    var y = 0;
    setInterval(function(){
        x += 1;
        y += 1;
        $('#left').css('background-position', x + 'px ' + y + 'px');
        $('#right').css('background-position', x + 'px ' + y + 'px');
    }, 55);
})