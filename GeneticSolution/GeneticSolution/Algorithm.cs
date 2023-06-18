using GeneticSharp;

namespace GeneticSolution;

public enum Rotations
{
    LWH = 0,
    WLH = 1,
    LHW = 2,
    HLW = 3,
    HWL = 4,
    WHL = 5
}

public class Fitness : IFitness
{
    public double Evaluate(IChromosome chromosome)
    {
        var values = chromosome as Chromosome;
        var results = new List<Box>();

        var boxes = values._boxes;
        var container = values._container;

        var dblf = new List<DBLF>();
        dblf.Add(new DBLF(new Point(0, 0, 0), new Point(container.width, container.height, container.depth)));

        var spaceUsed = 0;
        //var sortedBoxes = boxes.OrderBy(x => x.Length).ThenBy(x => x.Height).ThenBy(x => x.Width).ToList();

        foreach (var box in boxes)
        foreach (Rotations roration in Enum.GetValues(typeof(Rotations)))
        {
            dblf = dblf.OrderBy(x => x.PossiblePosition.X).ThenBy(x => x.PossiblePosition.Z)
                .ThenBy(x => x.PossiblePosition.Y).ToList();
            foreach (var dblfSolution in dblf)
            {
                var rotatedBox = box.Rotate(roration);
                if (dblfSolution.PossiblePosition.Volume >= rotatedBox.Volume &&
                    dblfSolution.PossiblePosition.X >= rotatedBox.Length &&
                    dblfSolution.PossiblePosition.Y >= rotatedBox.Width &&
                    dblfSolution.PossiblePosition.Z >= rotatedBox.Height)
                {
                    rotatedBox.Coordinates =
                        new Tuple<int, int, int>(dblfSolution.CurrentPosition.X, dblfSolution.CurrentPosition.Y,
                            dblfSolution.CurrentPosition.Z);
                    results.Add(rotatedBox);
                    spaceUsed += rotatedBox.Volume;

                    var firstPossibleSolution = new DBLF(
                        new Point(dblfSolution.CurrentPosition.X, dblfSolution.CurrentPosition.Y,
                            dblfSolution.CurrentPosition.Z + rotatedBox.Height),
                        new Point(rotatedBox.Length, rotatedBox.Width,
                            dblfSolution.PossiblePosition.Z - rotatedBox.Height));
                    var secondPossibleSolution = new DBLF(
                        new Point(dblfSolution.CurrentPosition.X, dblfSolution.CurrentPosition.Y + rotatedBox.Width,
                            dblfSolution.CurrentPosition.Z),
                        new Point(rotatedBox.Length, dblfSolution.PossiblePosition.Y - rotatedBox.Width,
                            dblfSolution.PossiblePosition.Z));
                    var thirdPossibleSolution = new DBLF(
                        new Point(dblfSolution.CurrentPosition.X + rotatedBox.Length, dblfSolution.CurrentPosition.Y,
                            dblfSolution.CurrentPosition.Z),
                        new Point(dblfSolution.PossiblePosition.X - rotatedBox.Length, dblfSolution.PossiblePosition.Y,
                            dblfSolution.PossiblePosition.Z));
                    dblf.Add(firstPossibleSolution);
                    dblf.Add(secondPossibleSolution);
                    dblf.Add(thirdPossibleSolution);
                    dblf.Remove(dblfSolution);
                    break;
                }
            }
        }

        values.SetResult(results);

        return spaceUsed / (double)container.Volume * 100;
    }
}

public class DBLF
{
    public DBLF(Point currentPosition, Point possiblePosition)
    {
        CurrentPosition = currentPosition;
        PossiblePosition = possiblePosition;
    }

    public Point CurrentPosition { get; set; }
    public Point PossiblePosition { get; set; }
}

public class Point
{
    public Point(int x, int y, int z)
    {
        X = x;
        Y = y;
        Z = z;
    }

    public int X { get; set; }
    public int Y { get; set; }
    public int Z { get; set; }

    public int Volume => X * Y * Z;
}