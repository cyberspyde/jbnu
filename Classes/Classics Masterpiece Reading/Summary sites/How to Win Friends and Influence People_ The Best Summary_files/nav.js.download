(function($) {
	$("a#toggle").on('click', function(e) {
		$('body').toggleClass('js-open');
		$('nav').toggleClass('js-open');
		e.preventDefault();
	});

	$(".nav-background").on('click', function() {
		$('body, nav').removeClass('js-open');
	});



// Offset for Wordpress Anchor Links
// https://jsfiddle.net/ju5xLgkq/
// The function actually applying the offset
function offsetAnchor() {
	if (location.hash.length !== 0) {
		window.scrollTo(window.scrollX, window.scrollY - 90);
	}
}

	// Captures click events of all a elements with href starting with #
	$(document).on('click', 'a[href^="#"]', function(event) {
	  // Click events are captured before hashchanges. Timeout
	  // causes offsetAnchor to be called after the page jump.
	  window.setTimeout(function() {
	  	offsetAnchor();
	  }, 0);
	});

	// Set the offset when entering page with hash present in the url
	window.setTimeout(offsetAnchor, 0);



})(jQuery);