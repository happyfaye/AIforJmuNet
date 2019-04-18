function random(start, end){
	return parseInt(Math.random() * (end - start) + start);
}

function arrToString(arr){
	return arr.toString().replace(/,/g, "");
}

document.getElementById('submit').onclick = function(){
	targetText = document.getElementById('text').value;
	document.getElementById('set').style.left = -485 + 'px';
	start();
}

document.getElementById('hide').onclick = function(){
	document.getElementById('set').style.left = -485 + 'px';
}

document.getElementById('show').onclick = function(){
	document.getElementById('set').style.left = 0;
}