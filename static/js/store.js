function navbarToggler() {
	var x = document.getElementById('myNavbar')
	if (x.className === 'navbar'){
		x.className += ' responsive';

	}
	else {
		x.className = 'navbar'
	}
}


// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myScroll()};

function myScroll() {
  // var navbar = document.getElementById("myTopnav");
  var mybutton = document.getElementById("myBtn");
  var progress_bar = document.getElementById("progress-bar");
  var sticky = progress_bar.offsetTop;
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;


  document.getElementById("myBar").style.width = scrolled + "%";
  if (window.pageYOffset >= sticky) {
    // navbar.classList.add("sticky")
    progress_bar.classList.add("sticky")
  } else {
    // navbar.classList.remove("sticky");
    progress_bar.classList.remove("sticky");
  }

  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }

  console.log(scrolled)

}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 


