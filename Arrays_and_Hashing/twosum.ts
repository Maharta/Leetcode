function twoSum(nums: number[], target: number): number[] {
  const map1 = new Map();

  for (let i = 0; i < nums.length; i++) {
    const needed = target - nums[i];

    if (map1.has(needed)) {
      return [i, map1.get(needed)];
    }
    map1.set(nums[i], i);
  }

  return [];
}

// [2,7,11,15]
// target = 9
// answer = [0, 1]

/*

    


*/
