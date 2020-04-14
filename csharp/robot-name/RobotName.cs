using System;
using System.Collections.Generic;

public class Robot
{
    // Set of already assigned names
    private static HashSet<string> _names = new HashSet<string>();
    private static Random _rnd = new Random();

    public Robot()
    {
        this.Name = _GetUniqueName();
    }

    public string Name {get; set;}

    public void Reset()
    {
        _names.Remove(this.Name);
        this.Name = _GetUniqueName();
    }

    private static string _GetUniqueName()
    {
        String name = ChooseName();
        while(false == _names.Add(name)) {
            name = ChooseName();
        }
        return name;
    }

    protected static string ChooseName()
    {
        return string.Format("{0}{1}{2:000}",
            (char)_rnd.Next('A', 'Z'),
            (char)_rnd.Next('A', 'Z'),
            _rnd.Next(0, 999)
        );
    }
}