function pertence(elemento, str) {
  for (let i = 0; i < str.length; i++) {
    if (elemento == str[i]) {
      return true                                            
    }
  }                                                          
                                                             
  return false                                               
}


function prepara(str) {
	const ALPHANUMERIC = 'abcdefghijklmnopqrstuvwxyz1234567890';
	str = str.toLowerCase();
	let res = "";

	for (let i = 0; i < str.length; i++) {                     
		if (pertence(str[i], ALPHANUMERIC)) {                    
        	res += str[i];                                       
    	}                                                        
 	}
                                                         
	return res                                                 
} 


function palindrome(str) {
	str = prepara(str);
	let revStr = "";

	for (let i = str.length - 1; i >= 0; i--) {
    	revStr += str[i];
	}

	if (str == revStr) {
    	return true;
  	} else {
    	return false;
	}
}
