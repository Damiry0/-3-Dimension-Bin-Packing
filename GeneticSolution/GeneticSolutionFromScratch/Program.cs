using System.Diagnostics;
using GeneticSolutionFromScratch;

var populationSize = 50; // Size of the population
var maxGenerations = 30; // Maximum number of generations
var random = new Random();

var boxes = new List<Box>();
for (var i = 0; i < 150; i++)
    boxes.Add(new Box(random.Next(1, 10), random.Next(1, 10), random.Next(1, 10), new Tuple<int, int, int>(0, 0, 0)));

var container = new Container(30, 30, 30);

var population = InitializePopulation(populationSize, boxes, container);


var stopwatch = new Stopwatch();
stopwatch.Start();


var latestFitness = 0.0;
var bestFitness = -1.0;
var bestResult = new List<Box>();


for (var generation = 1; generation <= maxGenerations; generation++)
{
    EvaluatePopulation(population);

    //Console.WriteLine("Generation: " + generation + " Fitness: " + population[0].Fitness);

    latestFitness = population[0].Fitness;

    if (latestFitness > bestFitness)
    {
        bestFitness = latestFitness;
        bestResult = population[0]._result;
        Console.WriteLine("New best solution found! Container is packed in {0}%.", bestFitness);
    }

    var newPopulation = new List<Individual>();

    while (newPopulation.Count < populationSize)
    {
        var parent1 = SelectParent(population, random);
        var parent2 = SelectParent(population, random);

        var child = Crossover(parent1, parent2, random, container);

        if (random.NextDouble() < 0.2)
            child = Mutate(child, random);

        newPopulation.Add(child);
    }

    population = newPopulation;
}

stopwatch.Stop();

Console.WriteLine($"Finished! Total elapsed time: {stopwatch.ElapsedMilliseconds}ms");
Console.WriteLine("Packed boxes:");
foreach (var box in bestResult) Console.WriteLine(box.ToString());

Console.WriteLine($"Container is packed in {latestFitness}%.");

Console.ReadLine();


static List<Individual> InitializePopulation(int populationSize, List<Box> boxes, Container container)
{
    var population = new List<Individual>();

    for (var i = 0; i < populationSize; i++)
    {
        var individual = new Individual(boxes, container);
        population.Add(individual);
    }

    return population;
}

static void EvaluatePopulation(List<Individual> population)
{
    foreach (var individual in population)
        individual.CalculateFitness();

    population.Sort((a, b) => b.CompareTo(a));
}

static Individual SelectParent(List<Individual> population, Random random)
{
    var totalFitness = population.Sum(i => i.Fitness);
    var randomValue = random.NextDouble() * totalFitness;

    foreach (var individual in population)
    {
        randomValue -= individual.Fitness;
        if (randomValue <= 0)
            return individual;
    }

    return population[^1];
}

static Individual Crossover(Individual parent1, Individual parent2, Random random, Container container)
{
    var crossoverPoint = random.Next(1, parent1._boxes.Count - 1);

    var child = new Individual(new List<Box>(parent1._boxes.Count), container);

    for (var i = 0; i < crossoverPoint; i++)
        child._boxes.Add(parent1._boxes[i]);

    for (var i = crossoverPoint; i < parent2._boxes.Count; i++)
        child._boxes.Add(parent1._boxes[i]);

    return child;
}

static Individual Mutate(Individual individual, Random random)
{
    var mutationPoint = random.Next(individual._boxes.Count);
    individual._boxes[mutationPoint] = new Box(random.Next(1, 10), random.Next(1, 10), random.Next(1, 10),
        new Tuple<int, int, int>(0, 0, 0));
    return individual;
}