using System;

public static class TwoFer
{
    public static string Speak(String name = null) =>
        $"One for {Default(name)}, one for me.";

    private static string Default(String name = null) =>
        string.IsNullOrEmpty(name) ? "you" : name;

}
