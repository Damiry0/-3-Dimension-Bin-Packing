namespace GeneticSolutionFromScratch;

public class GeneticAlgorithm
{
    private readonly int geneLength;
    private readonly double mutationRate;
    private readonly int populationSize;
    private readonly Random random;
    private readonly string targetGene;
    private List<Individual> population;

    public GeneticAlgorithm(string targetGene, double mutationRate, int populationSize, int geneLength)
    {
        this.targetGene = targetGene;
        this.mutationRate = mutationRate;
        this.populationSize = populationSize;
        this.geneLength = geneLength;
    }

    public void Run(int maxGenerations)
    {
        InitializePopulation();

        var generation = 0;
        while (generation < maxGenerations && !HasFoundTargetGene())
        {
            NextGeneration();
            generation++;
        }

        Console.WriteLine("Algorithm complete.");
        Console.WriteLine("Target gene: " + targetGene);
        Console.WriteLine("Generation: " + generation);
        Console.WriteLine("Best gene found: " + GetBestIndividual().Gene);
    }

    private void InitializePopulation()
    {
        population = new List<Individual>();
        for (var i = 0; i < populationSize; i++) population.Add(new Individual(geneLength));
    }

    private bool HasFoundTargetGene()
    {
        return population.Any(individual => individual.Gene == targetGene);
    }

    private void NextGeneration()
    {
        List<Individual> newPopulation = new();

        while (newPopulation.Count < populationSize)
        {
            var parent1 = SelectParent();
            var parent2 = SelectParent();

            var child = parent1.Crossover(parent2);
            child.Mutate(mutationRate);

            newPopulation.Add(child);
        }

        population = newPopulation;
        CalculateFitness();
    }

    private Individual SelectParent()
    {
        return population[random.Next(populationSize)];
    }

    private void CalculateFitness()
    {
        foreach (var individual in population) individual.CalculateFitness(targetGene);
    }

    private Individual GetBestIndividual()
    {
        return population.OrderByDescending(individual => individual.Fitness).First();
    }
}