using GeneticSharp;

namespace GeneticSolution;

public class Chromosome : ChromosomeBase
{
    public readonly List<Box> _boxes = new();
    public readonly Container _container;
    public List<Box> _result = new();

    public Chromosome(List<Box> boxes, Container container) : base(10)
    {
        boxes.Shuffle();
        _boxes = boxes;
        _container = container;
        CreateGenes();
    }

    public override Gene GenerateGene(int geneIndex)
    {
        return new Gene(geneIndex);
    }

    public void SetResult(List<Box> boxes)
    {
        _result = boxes;
    }

    public override IChromosome CreateNew()
    {
        return new Chromosome(_boxes, _container);
    }
}