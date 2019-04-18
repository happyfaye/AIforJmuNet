var targetText = "Hello,201621123036
var generation = 0;
var mutateRate = 0.01;
var maxPop = 300;
var maxGeneration = 10000;
var sleepTime = 50;
var bestFitness = "";
var bestFitRate = 0;

function start(){

	var populations = new Populations(targetText, mutateRate, maxPop, maxGeneration);
	// calc fitness.
	populations.calcFitness();
	// sort by fitness.
	populations.sortByFitness();
	bestFitness = arrToString(populations.bestFit);
	bestFitRate = populations.bestFitRate;

	var drawer = new Drawer(targetText, bestFitness, mutateRate, maxPop);

	function drawPopList(){
		for(var i = 0; i < 22; i++){
			var itemText = arrToString(populations.popList[i].DNA);
			drawer.drawPopListItem(i, itemText, populations.popList[i].fitness);
		}
	}

	drawPopList();

	var interval = this.setInterval(function(){
		if(bestFitRate == 1 || generation > maxGeneration)
		{
			clearInterval(interval);
			generation = 0;
			return;
		}
		// crossover 
		populations.crossover();
		// mutate
		populations.mutate();
		// calc fitness.
		populations.calcFitness();
		// sort by fitness.
		populations.sortByFitness();
		// update bestFitness.
		bestFitness = arrToString(populations.bestFit);
		bestFitRate = populations.bestFitRate;
		// update generation.
		generation++;
		// update the canvas.
		drawer.updateData(bestFitness, generation);
		drawPopList();
	}, sleepTime);
}

start();