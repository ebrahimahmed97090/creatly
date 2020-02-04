/*slider*/
$(document).ready(function () {
    $("#testimonial-slider").owlCarousel({
        items: 3,
        itemsDesktop: [15, 3],
        itemsDesktopSmall: [15, 2],
        itemsTablet: [15, 2],
        itemsMobile: [15, 1],
        pagination: true,
        autoPlay: true
    });
});