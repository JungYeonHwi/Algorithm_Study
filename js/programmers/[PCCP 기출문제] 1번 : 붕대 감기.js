function solution(bandage, health, attacks) {
  var answer = 0;
  let currentHealth = health;
  let dusthr = 0;

  let attackTime = attacks.map((item) => String(item[0]));
  let attackHealth = attacks.map((item) => String(item[1]));

  for (let i = 1; i <= attacks[attacks.length - 1][0]; i++) {
    if (attackTime.indexOf(String(i)) !== -1) {
      // 공격
      currentHealth -= attackHealth[attackTime.indexOf(String(i))];
      dusthr = 0;
    } else {
      if (dusthr === bandage[0] - 1) {
        currentHealth += bandage[2];
        currentHealth += bandage[1];
        dusthr = 0;
      } else {
        currentHealth += bandage[1];
        dusthr += 1;
      }
    }
    currentHealth = Math.min(currentHealth, health);
    if (currentHealth <= 0) return -1;
  }

  return (answer = currentHealth <= 0 ? -1 : currentHealth);
}
