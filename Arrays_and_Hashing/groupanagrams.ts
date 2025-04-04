function groupAnagrams(strs: string[]): string[][] {
  const map = new Map<string, number[]>();

  for (let i = 0; i < strs.length; i++) {
    const word = strs[i];
    const arr = new Array(26).fill(0);
    for (let j = 0; j < word.length; j++) {
      const charPos = word.charCodeAt(j) - 97;
      arr[charPos] += 1;
    }

    const key = arr.join("");

    if (map.has(key)) {
      map.set(key, [...map.get(key)!, i]);
    } else {
      map.set(key, [i]);
    }
  }

  const out: string[][] = [];

  for (const val of map.values()) {
    const x: string[] = [];
    val.forEach((lues) => x.push(strs[lues]));
    out.push(x);
  }

  return out;
}
