const navSlide = () => {
	const hamburger = document.querySelector('.hamburger');
	const nav = document.querySelector('nav ul');
	const navlinks = document.querySelectorAll('nav ul li');

	hamburger.addEventListener('click', () => {
		nav.classList.toggle('nav-active');
		hamburger.classList.toggle('toggle');
	});


	$(window).on("scroll",function(){
      if($(window).scrollTop()){
        $('nav').addClass('black');
        $('.logo').addClass('black');
      }
      else{
        $('nav').removeClass('black');
        $('.logo').removeClass('black');
      }
    });
}

navSlide();