function findLongestWordLength(str) {
/*
  Dada uma sentença, pede-se para encontrar a quantidade de caracteres da maior palavra. 

  Uma possível abordagem para o problema consiste em: encontrar as palavras da sentença, verificar qual delas é a maior e, enfim, retornar seu comprimento. Mas, antes de tudo, convém resaltar que o problemas não é suficentemente claro quanto ao que se deve considerar como "palavra". Tomemos, por definição, que 'palavra' seja qualquer sequência de caracteres limitada por um espaço em branco. Assim, as palavras da string "olá mundo" seria "mundo" e "olá". No entanto, há um problema com sinais de pontuação: se a string fosse "olá, mundo!", pela definição, as palavras seriam "mundo!" e "olá,".

  Mas, para este desafio, a definição nos basta. E, desse modo, podemos facilmente criar a lista desejada através do método .split(). 

*/
  let palavras = str.split(' ');
/*

  Com a lista em mãos, podemos encontrar a palavra mais longa comparando os tamanhos das palavras. Iterando sobre cada item da lista, verificamos se esta é a palavra mais longa já encontrada. Usaremos para isto uma variável auxiliar que armazene o valor do comprimento da palavra mais longa e chamá-la-emos 'lengthLongestWord'. É óbvio que na primeira iteração, não teremos nenhuma palavra armazenada: por esta razão é que convém inicializá-la com valor 0. 

*/
  let lengthLongestWord = 0;
/*

  Em seguida, para cada palavra p na lista de palavras, verificaremos se seu comprimento é maior que o da palavra que já encontramos. Somente se for, atualizaremos o valor da variável.
 
*/
  for (let p = 0; p < palavras.length; p++) {
    if (palavras[p].length > lengthLongestWord) {
      lengthLongestWord = palavras[p].length;
    }
  }
/*

  Desse modo, ao fim do loop teremos armazenado o valor da maior palavra da sentença, bastando-nos apenas retorná-lo.
*/
  return lengthLongestWord;
}


console.log(findLongestWordLength("The quick brown jumped over the lazy dog"))