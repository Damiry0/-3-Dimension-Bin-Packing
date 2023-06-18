using System.Diagnostics;
using GeneticSharp;
using GeneticSolution;

// Console.WriteLine("Hybrid Genetic Algorithm");
// Console.WriteLine("========================");
// Console.WriteLine("Number of generated boxes:");
// var numberOfBoxes = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Dimensions of Container:");
// var x = Convert.ToInt32(Console.ReadLine());
// var y = Convert.ToInt32(Console.ReadLine());
// var z = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Number of population:");
// var minPopulation = Convert.ToInt32(Console.ReadLine());
// var maxPopulation = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Number of generations:");
// var generations = Convert.ToInt32(Console.ReadLine());


var selection = new EliteSelection();
var crossover = new OrderedCrossover();
var mutation = new ReverseSequenceMutation();
var fitness = new Fitness();

var random = new Random();

var boxes = new List<Box>();
for (var i = 0; i < 150; i++)
    boxes.Add(new Box(random.Next(1, 10), random.Next(1, 10), random.Next(1, 10), new Tuple<int, int, int>(0, 0, 0)));

var container = new Container(30, 30, 30, new Tuple<int, int, int>(0, 0, 0));

var chromosome = new Chromosome(boxes, container);
var population = new Population(50, 100, chromosome);

var ga = new GeneticAlgorithm(population, fitness, selection, crossover, mutation)
{
    Termination = new GenerationNumberTermination(50)
};


var latestFitness = 0.0;
var latestResult = new List<Box>();


var stopwatch = new Stopwatch();
stopwatch.Start();

ga.GenerationRan += (sender, e) =>
{
    var bestChromosome = ga.BestChromosome as Chromosome;
    var bestFitness = bestChromosome.Fitness.Value;
    if (bestFitness != latestFitness)
    {
        latestFitness = bestFitness;
        latestResult = bestChromosome._result;
        Console.WriteLine("New best solution found! Container is packed in {0}%.", ga.BestChromosome.Fitness);
    }
};

ga.Start();

stopwatch.Stop();
var elapsed_time = stopwatch.ElapsedMilliseconds;

Console.WriteLine($"Finished! Total elapsed time: {elapsed_time}ms");
Console.WriteLine("Packed boxes:");
foreach (var box in latestResult) Console.WriteLine(box.ToString());

Console.WriteLine($"Container is packed in {latestFitness}%.");