$(document).ready(function(){

	/*  CHANGES Background images of SECTION TAG  */
	
	var bagks = ['url(/static/p1.jpg)','url(/static/p2.jpg)','url(/static/p3.jpg)'];
	var ind = 0;
	$('.openw1').css('animation-duration','3s');
	$('#b2').on('click',function(){
		ind++;
		if (ind>2){
			ind=0;
			$('section').animate({opacity: 0}, 'slow', function() {
        		$(this).css({'background-image': bagks[ind]}).animate({opacity: 1});
    });
		}else{
			$('section').animate({opacity: 0}, 'slow', function() {
        		$(this).css({'background-image': bagks[ind]}).animate({opacity: 1});
    });
		}
	});
	$('#b1').on('click',function(){
		ind--;
		if (ind<=0){
			ind=2;
			$('section').animate({opacity: 0}, 'slow', function() {
        		$(this).css({'background-image': bagks[ind]}).animate({opacity: 1});
    });
		}else{
			$('section').animate({opacity: 0}, 'slow', function() {
        		$(this).css({'background-image': bagks[ind]}).animate({opacity: 1});
    });
		}
	});


	$('#c1').on('click',function(){
		$('#c1p').toggle(1000);
	});

	$('#cwd').on('click',function(){
		$('#cwdp').fadeToggle('slow');
	});
	$('#hf').on('click',function(){
		$('#hfp').fadeToggle('slow');
	});
	$('#df').on('click',function(){
		$('#dfp').fadeToggle('slow');
	});

	

	$('.openw1').on('click',function(){
		$('.openw1').toggleClass('open-pause');
		
	});


	


});