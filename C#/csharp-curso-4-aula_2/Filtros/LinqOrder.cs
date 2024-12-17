using ScreenSound_04.Modelos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ScreenSound_04.Filtros
{
    internal class LinqOrder
    {
        public static void ExibirListadeArtistasOrdenados(List<Musica> musicas)
        {
            var ArtistasOrdenados = musicas.OrderBy(musica => musica.Artista).Select(musica => musica.Artista).Distinct().ToList();
        }
    }
}
