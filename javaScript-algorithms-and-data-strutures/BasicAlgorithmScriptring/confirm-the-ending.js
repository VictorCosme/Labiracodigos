function confirmEnding(str, target) {
  let substring = "";

  for (let i = str.length - target.length; i < str.length; i++) {
    substring += str[i];
  }

  return substring === target;
}

confirmEnding("Bastian", "n");