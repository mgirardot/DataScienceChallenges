## DataScience Challenge 5
# _ Quel langage parlent les protéines ? _

Un article récent dans [xkcd what-if](https://web.archive.org/web/20161205231341/http://what-if.xkcd.com/153/) pose une question amusante à propos du plus long mot anglais qu'on peut constituer avec l'alphabet des abreviations des 20 acides aminés qui constituent les protéines. Cela m'a inspiré une question encore plus amusante: **Quel langage parlent les protéines de notre corps ?**

Les séquences des protéines humaines sont connues et disponibles sur [uniprot](http://www.uniprot.org/proteomes/UP000005640). Elles sont encodé grâce a un alphabet de 20 lettres qui est:

|Nom    | lettre|
|:------|------:|
| Alanine | A   |
| Arginine | R   |
| Asparagine | N   |
| Acide Aspartique | D   |
| Cysteine | C   |
| Acide Glutamique | E   |
| Glutamine | Q   |
| Glycine | G   |
| Histidine | H   |
| Isoleucine | I   |
| Leucine | L   |
| Lysine | K   |
| Methionine | M   |
| Phenylalanine | F   |
| Proline | P   |
| Serine | S   |
| Threonine | T   |
| Tryptophane | W   |
| Tyrosine | Y   |
| Valine | V   |

Voici, par exemple, la séquence d'une protéine connue, l'insuline, dans laquelle on peut identifier le mot `VEAL` (veau en anglais) ou `GIVE` (donner en anglais).

>sp|P01308|INS_HUMAN Insulin OS=Homo sapiens GN=INS PE=1 SV=1
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHL**VEAL**YLVCGERGFFYTPKTRREAED
LQVGQVELGGGPGAGSLQPLALEGSLQKR**GIVE**QCCTSICSLYQLENYCN

Le challenge va donc consister à identifier dans le protéome le nombre maximum de mots des différentes langues internationnales. Pour générer les dictionnaires des différentes langues, vous pouvez utiliser les livres du domaine public hébergé sur [project Guntenberg](https://www.gutenberg.org/catalog/).


      . .
       \|    o
        o__ /
       /   O
    .-o    | 
     .'`.  o

