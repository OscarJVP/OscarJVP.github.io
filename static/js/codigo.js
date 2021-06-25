let con = document.getElementById("canvas1");
let can = con.getContext("2d");
let c = 0;

function cambiarBoton(){
	if(document.getElementById("botonFav").innerHTML == "Agregar a favoritos")
	{
		document.getElementById("botonFav").innerHTML = "Quitar de favoritos";
	}else{
		document.getElementById("botonFav").innerHTML = "Agregar a favoritos";
	}
}

function animacion(){
	can.clearRect(0,0,100,50);
	can.fillStyle = "#803945";
	can.fillRect(0,0,100,50);

	can.beginPath();

	can.moveTo(50,10);
	can.lineTo(55,18.34);
	can.lineTo(63.33,20);
	can.lineTo(56.66,28.34);
	can.lineTo(58.33,36.67);
	can.lineTo(50,32.5);
	can.lineTo(41.67,36.67);
	can.lineTo(43.34,28.34);
	can.lineTo(36.67,20);
	can.lineTo(45,18.34);
	can.lineTo(50,10);

	if(c == 0){
		can.strokeStyle = "#FFFFA7";
	}else{
		if(c == 1){
			can.fillStyle = "#FFFFA7";
		}else{
			if(c == 2){
				can.strokeStyle = "#FFFF7E";
				can.fillStyle = "#FFFF7E";
			}else{
				if(c == 3){
					can.strokeStyle = "#FFFF56";
					can.fillStyle = "#FFFF56";
				}else{
					can.strokeStyle = "yellow";
					can.fillStyle = "yellow";
				}
			}
		}
	}

	can.fill();
	can.stroke();

	if(c == 4){
		c = 0;
	}else{
		c += 1;
	}

	var ciclo = setTimeout(animacion,1000);
}

function navidad(){
	var son = document.getElementById("sonidoNavidad");

	if(son.paused == true){
		son.play();
	}else{
		son.pause();
	}
}

function anioNuevo(){
	var son = document.getElementById("sonidoAnio");

	if(son.paused == true){
		son.play();
	}else{
		son.pause();
	}
}

function fiestasPatrias(){
	var son = document.getElementById("sonidoFiestas");

	if(son.paused == true){
		son.play();
	}else{
		son.pause();
	}
}

// Para revisar inicio de sesión
