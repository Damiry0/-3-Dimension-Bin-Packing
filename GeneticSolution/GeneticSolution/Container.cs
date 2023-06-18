namespace GeneticSolution;

public record Container(int width, int height, int depth, Tuple<int, int, int> coordinates,
    Tuple<int, int, int>? potentialCoordinates = null)
{
    public int Volume => width * height * depth;
}