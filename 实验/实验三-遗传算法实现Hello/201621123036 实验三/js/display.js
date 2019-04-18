function Drawer(targetText, bestFit, mutateRate, maxPop){
	this.canvas = document.getElementById('canvas');
	this.context = canvas.getContext('2d');
	this.color = "#333333";
	this.bgColor = '#F2F2F2'
	this.screenWidth = document.documentElement.clientWidth;
	this.screenHeight = document.documentElement.clientHeight;

	this.targetText = targetText;
	this.generation = 0;
	this.bestFit = bestFit || '-';
	this.mutateRate = mutateRate || 0.01;
	this.maxPop = maxPop || 200;

	this.setCanvas = function(bgColor){
		this.canvas.width = this.screenWidth;
		this.canvas.height = this.screenHeight;
		this.canvas.style.backgroundColor = bgColor;
	}

	this.drawBasic = function(fontStyle, text, left, top){
		this.context.font = fontStyle;
		this.context.fillStyle = this.targetText == this.bestFit ? 'red' : this.color;
		this.context.fillText(text, left, top);
	}

	this.drawBestFitness = function(text){
		this.drawBasic("42px Sarif", text, 20, this.screenHeight / 5);
	}

	this.drawGeneration = function(text){
		this.drawBasic("18px Sarif", text, 20, this.screenHeight / 5 + 50);
	}

	this.drawTargetText = function(text){
		this.drawBasic("18px Sarif", text, 20, this.screenHeight / 5 + 80);
	}

	this.drawTargetTextLength = function(text){
		this.drawBasic("18px Sarif", text, 20, this.screenHeight / 5 + 110);
	}

	this.drawMutateRate = function(text){
		this.drawBasic("18px Sarif", text, 20, this.screenHeight / 5 + 140);
	}

	this.drawMaxPop = function(text){
		this.drawBasic("18px Sarif", text, 20, this.screenHeight / 5 + 170);
	}

	this.drawPopListItem = function(id, text, fitness){
		this.context.font = "14px Sarif";
		this.context.fillStyle = '#888';
		this.context.fillText(id, this.screenWidth * 1 / 2, this.screenHeight / 5 + 50 + id * 20);
		this.context.fillText(fitness, this.screenWidth * 1 / 2 + 40, this.screenHeight / 5 + 50 + id * 20);
		this.context.fillText(text, this.screenWidth * 1 / 2 + 100, this.screenHeight / 5 + 50 + id * 20);
	}

	this.draweInfo = function(){
		this.context.clearRect(0, 0, this.screenWidth, this.screenHeight);
		this.drawBestFitness(this.bestFit);
		this.drawTargetText('Target Text: ' + this.targetText);
		this.drawTargetTextLength('Target Text Length: ' + this.targetText.length);
		this.drawGeneration('Current Generation: ' + this.generation);
		this.drawMutateRate('Mutate Rate: ' + this.mutateRate);
		this.drawMaxPop('Max Population: ' + this.maxPop);
	}

	this.updateData = function(bestFit, generation){
		this.bestFit = bestFit;
		this.generation = generation;

		this.draweInfo();
	}

	this.setCanvas(this.bgColor);
	this.draweInfo();
}

// var drawer = new Drawer();

// drawer.setCanvas('#F2F2F2');
// drawer.drawBestFitness(drawer.text);
// drawer.drawGeneration('Current Generation: ' + drawer.generation);
// drawer.drawMutateRate('Mutate Rate: ' + drawer.mutateRate);
// drawer.drawMaxPop('Max Population: ' + drawer.maxPop);
// drawer.drawPopList(0, "To be or not to be, that is a question.", 1);
// drawer.drawPopList(1, "To be or not to be, that is a question.", 1);