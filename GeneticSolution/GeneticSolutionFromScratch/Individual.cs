namespace GeneticSolutionFromScratch;

public class Individual
{
    private static readonly Random random = new();

    public Individual(int geneLength)
    {
        Gene = GenerateRandomGene(geneLength);
    }

    public string Gene { get; private set; }
    public double Fitness { get; private set; }

    public void CalculateFitness(string targetGene)
    {
        var matchingGenes = Gene.Zip(targetGene, (a, b) => a == b ? 1 : 0).Sum();
        Fitness = (double)matchingGenes / targetGene.Length;
    }

    public Individual Crossover(Individual partner)
    {
        var crossoverPoint = random.Next(0, Gene.Length);
        var childGene = Gene.Substring(0, crossoverPoint) + partner.Gene.Substring(crossoverPoint);
        return new Individual(childGene.Length) { Gene = childGene };
    }

    public void Mutate(double mutationRate)
    {
        var geneArray = Gene.ToCharArray();
        for (var i = 0; i < geneArray.Length; i++)
            if (random.NextDouble() < mutationRate)
                geneArray[i] = geneArray[i] == '0' ? '1' : '0';
        Gene = new string(geneArray);
    }

    private string GenerateRandomGene(int geneLength)
    {
        var geneArray = new char[geneLength];
        for (var i = 0; i < geneLength; i++) geneArray[i] = random.Next(2) == 0 ? '0' : '1';
        return new string(geneArray);
    }
}