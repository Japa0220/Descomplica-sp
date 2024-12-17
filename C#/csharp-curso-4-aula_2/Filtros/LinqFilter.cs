using ScreenSound_04.Modelos;
using System.Text.Json;
using ScreenSound_04.Filtros;

namespace ScreenSound_04.Filtros
{
    internal class LinqFilter
    {
        public static void FiltrarTodososGenerosMusicais(List<Musica> musicas)
        {
            var todosOsGenerosMusicais = musicas.Select(genero => genero.Genero).Distinct().ToList();
            foreach (var genero in todosOsGenerosMusicais)
            {
                Console.WriteLine($"-{genero}");
            }
        }
    }
}
