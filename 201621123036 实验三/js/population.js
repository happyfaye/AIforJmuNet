function Populations(text, mutateRate, maxPop, maxGeneration){
	this.text = text;
	this.bestFit = "";
	this.bestFitRate = 0;
	this.mutateRate = mutateRate || 0.01;
	this.maxPop = maxPop || 200;
	this.maxGeneration = maxGeneration || 10000;
	this.popList = [];
	this.usefulLine = this.maxPop / 10;

	this.generate = function(){
		for(var i = 0; i < maxPop; i++){
			var newDNA = new DNA(this.text);
			newDNA.generateDNA();
			this.popList.push(newDNA);
		}
	}

	this.calcFitness = function(){
		for(var i = 0; i < this.popList.length; i++){
			this.popList[i].calcFitness();
		}
	}

	this.sortByFitness = function(){
		for(var i = 0; i < maxPop - 1; i++){
			for(var j = 0; j < maxPop - i -1; j++){
				if(this.popList[j].fitness < this.popList[j + 1].fitness){
					var temp = this.popList[j];
					this.popList[j] = this.popList[j + 1];
					this.popList[j + 1] = temp;
				}
			}
		}
		this.bestFit = this.popList[0].DNA;
		this.bestFitRate = this.popList[0].fitness;
	}

	// this.getUserfulLine = function(){
	// 	for(var i = 0; i < this.maxPop / 2; i++){
	// 		if(this.popList[i].fitness == 0){
	// 			this.getUserfulLine = i;
	// 			return i;
	// 		}
	// 	}
	// 	return maxPop / 2;
	// }

	this.mutate = function(){
		for(var i = 0; i < maxPop; i++){
			this.popList[i].mutate(this.mutateRate);
		}
	}

	this.crossover = function(){
		// update the usefulLine;
		// this.usefulLine = this.getUserfulLine();
		// console.log(this.usefulLine);

		for(var i = this.usefulLine; i < this.maxPop; i++){
			var randDNA = random(0, this.usefulLine);
			this.popList[i].crossover(this.popList[randDNA]);
		}
	}

	this.generate();
}

