/*
  Dado um array contendo 4 sub-arrays, cada qual com 4 valores inteiros; pede-se para retornar um array com os maiores inteiros de cada sub-array.

  Esse problema pode ser decomposto nas seguintes duas tarefas: encontrar o maior valor de cada um dos sub-arrays de inteiros, e o segundo, montar o array desejado.

  Inicialmente, criaremos uma função que, dado um array numérico, retorne o maior valor inteiro. Para isto, suporemos inicialmente que o primeiro elemento do array seja o maior valor e o armazenaremos numa variável "maiorInteiro". 
  
*/
function maiorInt(arr) {
  let maiorInteiro = arr[0];
/*  
  
  Em seguida, basta iterar sobre os demais elementos do array, checando se é o maior valor encontrado: se for, atualizaremos nossa variável 'maiorInteiro'. No fim, basta retorna o valor encontrado. 

*/
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > maiorInteiro) {
      maiorInteiro = arr[i];
    }
  }

  return maiorInteiro;
}
/*
  
  Podemos agora focar no problema de montar o array. Nós criaremos uma função e uma variável 'maioresValores' para servir armazenar o array desejado, que inicialmente é vazio.

*/
function largestOfFour(arr) {
  let maioresValores = [];
/*

  O problema indica que o argumento da função é um array de arrays. Desse modo, para encontrar os maiores valores, iteraremos sobre os elementos do array principal. Para cada um deles, identificaremos o maior valor com auxílio da função que criamos, maiorInt(arr), adicionando-o ao array 'maioresValores'.

*/
  for (let i=0; i < arr.length; i++) {
    maioresValores.push(maiorInt(arr[i]));
  }
/*
  
  Ao final, o array 'maioresValores' conterá os maiores valores de cada sub-array no array dado, na ordem em que constam, como nos foi pedido. Assim, foi criado um array consistindo dos maiores números de cada sub-array de um array dado. Basta-nos agora retorná-lo. 

*/
  return maioresValores;
}

largestOfFour([4, 5, 1, 3]);
