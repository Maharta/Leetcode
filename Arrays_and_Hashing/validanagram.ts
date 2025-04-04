function isAnagram(s: string, t: string): boolean {
  function setOrCompute<V>(
    map: Map<string, V>,
    key,
    computeFn: Function,
    defaultValue: V
  ) {
    if (map.has(key)) {
      map.set(key, computeFn(map.get(key)));
    } else {
      map.set(key, defaultValue);
    }
  }

  if (s.length !== t.length) {
    return false;
  }

  const sMap = new Map<string, number>();
  const tMap = new Map();

  for (let i = 0; i < s.length; i++) {
    const sChar = s.charAt(i);
    const tChar = t.charAt(i);
    setOrCompute(sMap, sChar, (v) => v + 1, 1);
    setOrCompute(tMap, tChar, (v) => v + 1, 1);
  }

  for (let i = 0; i < s.length; i++) {
    const sChar = s.charAt(i);
    if (sMap.get(sChar) !== tMap.get(sChar)) return false;
  }

  return true;
}
