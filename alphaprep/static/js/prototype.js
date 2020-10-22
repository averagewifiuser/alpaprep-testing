$(function() {
    menu = $("section nav ul");

    $("#openup").on("click", function(e) {
        e.preventDefault();
        menu.slideToggle();
        setTimeout()
    });

    $(window).resize(function() {
        var w = $(this).width();
        if (w > 480 && menu.is(":hidden")) {
            menu.removeAttr("style");
        }
    });

    $(".logoName").on("click", function(e) {
        var w = $(window).width();
        if (w < 480) {
            menu.slideToggle();
        }
    });
    $(".open-menu").height($(window).height());

});