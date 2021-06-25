let canvas = document.getElementById("canvas1");
let context = canvas.getContext("2d");
 
function pixeles(){
	var imageObj = new Image();
    	imageObj.src = 'static/images/iconoHome.PNG';
 
    	imageObj.onload = function () {
        context.drawImage(imageObj, 0, 0 );

	context.getImageData( 0, 0, 150, 150 );
	}
}