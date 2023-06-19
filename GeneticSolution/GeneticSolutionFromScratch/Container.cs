namespace GeneticSolutionFromScratch;

public record Container(int width, int height, int depth)
{
    public int Volume => width * height * depth;
}