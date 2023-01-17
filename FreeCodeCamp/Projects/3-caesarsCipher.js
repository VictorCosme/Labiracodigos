/* 
Recebe um caractere e uma string. Retorna uma lista contendo no índice:
	0. Um bool conf. o char pertença ou não a string;
	1. Somente se pertence, o índice do char na str 
*/
function pertence(c, str) {
	for (let i = 0; i < str.length; i++) {
    	if (c == str[i]) {
    		return [true, i];
    	}
  	}

	return [false];
}


/*
Recebe uma string criptografada. Retorna uma string descriptografada a partir do deslocamento de cada caractere de 13 posições à esquerda.
*/
function rot13(str) {
  const A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const B = 'NOPQRSTUVWXYZABCDEFGHIJKLM';

  let mes = "";

  for (let i = 0; i < str.length; i++) {
    let c = pertence(str[i], A);
    
    if (c[0]) {
      mes += B[c[1]]

    } else {
      mes += str[i];
    }
  }

  return mes;
}


