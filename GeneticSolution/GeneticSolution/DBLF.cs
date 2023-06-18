namespace GeneticSolution;

public class DBLF
{
    public DBLF(Point currentPosition, Point possiblePosition)
    {
        CurrentPosition = currentPosition;
        PossiblePosition = possiblePosition;
    }

    public Point CurrentPosition { get; }
    public Point PossiblePosition { get; }
}