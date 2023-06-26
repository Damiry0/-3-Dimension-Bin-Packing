namespace GeneticSolution;

public class Box
{
    public Box(int width, int height, int length, Tuple<int, int, int> coordinates)
    {
        Width = width;
        Height = height;
        Length = length;
        Coordinates = coordinates;
    }

    public int Width { get; }
    public int Height { get; }
    public int Length { get; }

    public int Volume => Width * Height * Length;

    public Tuple<int, int, int> Coordinates { get; set; }

    public Box Rotate(Rotations rotation)
    {
        return rotation switch
        {
            Rotations.LWH => new Box(Length, Width, Height, Coordinates),
            Rotations.WLH => new Box(Width, Length, Height, Coordinates),
            Rotations.LHW => new Box(Length, Height, Width, Coordinates),
            Rotations.HLW => new Box(Height, Length, Width, Coordinates),
            Rotations.HWL => new Box(Height, Width, Length, Coordinates),
            Rotations.WHL => new Box(Width, Height, Length, Coordinates),
            _ => throw new IndexOutOfRangeException()
        };
    }

    public override string ToString()
    {
        return
            $"Coordinates: {Coordinates.Item1} {Coordinates.Item2} {Coordinates.Item3}, W: {Height} L: {Length} H: {Height}";
    }
}