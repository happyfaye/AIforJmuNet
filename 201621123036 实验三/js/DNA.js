function DNA(text){
	this.goalText = text;
	this.DNA = [];
	this.fitness = 0;

	this.newChar = function(){
		return String.fromCharCode(random(36, 156));
	}

	this.generateDNA = function(){
		for(var i = 0; i < this.goalText.length; i++){
			this.DNA.push(this.newChar());
		}
	}

	this.calcFitness = function(){
		var score = 0;
		for(var i = 0; i < this.DNA.length; i++){
			if(this.goalText[i] == this.DNA[i]) score++;
		}
		this.fitness = (score / this.DNA.length).toFixed(4);
	}

	this.mutate = function(mutateRate){
		for(var i = 0; i < this.DNA.length; i++){
			var mutateIndex = Math.random();
			if(mutateIndex < mutateRate){
				this.DNA[i] = this.newChar();
			}
		}
	}

	this.crossover = function(DNA){
		var randStart = random(0, this.goalText.length / 2);
		var randEnd = random(0, this.goalText.length);
		while(randEnd <= randStart){
			randEnd = random(0, this.goalText.length);
		}

		for(var i = randStart; i < randEnd; i++){
			this.DNA[i] = DNA.DNA[i];
		}
	}
}