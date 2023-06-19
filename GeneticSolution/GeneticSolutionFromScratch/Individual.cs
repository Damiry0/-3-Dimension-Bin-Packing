using GeneticSolutionFromScratch;

public class Individual : IComparable<Individual>
{
    public readonly List<Box> _boxes = new();
    public readonly Container _container;
    public List<Box> _result = new();

    public Individual(List<Box> boxes, Container container)
    {
        boxes.Shuffle();
        _boxes = boxes;
        _container = container;
    }

    public double Fitness { get; private set; }

    public int CompareTo(Individual other)
    {
        // Compare individuals based on their fitness (lower fitness is better)
        return Fitness.CompareTo(other.Fitness);
    }

    public void SetResult(List<Box> boxes)
    {
        _result = boxes;
    }

    public void CalculateFitness()
    {
        var fitness = new Fitness().Evaluate(this);
        Fitness = fitness;
    }
}