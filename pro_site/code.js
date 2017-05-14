$(document).ready(function(){
	$("carusel-slider").flickity({
		cellSelector: '.carusel-cell',
		imagesLoaded: true,
		freeScroll: true,
		wrapAround: true,
		autoPlay: 1500,
		groupCells: true

	});
});