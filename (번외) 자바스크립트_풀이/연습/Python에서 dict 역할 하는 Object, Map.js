/* Object 사용하기 */
const scores = {
  Junho: 95,
  Minho: 87,
  GichuL: 100
};

console.log(scores["Junho"]);  // 95
scores["Minho"] = 90;          // 값 변경
scores["Newbie"] = 75;         // 추가

console.log(Object.keys(scores));   // ["Junho", "Minho", "GichuL", "Newbie"]
console.log(Object.values(scores)); // [95, 90, 100, 75]
console.log(Object.entries(scores)); // [["Junho",95],["Minho",90],...]

const obj = {};
console.log(obj["key"]);    // undefined
console.log("key" in obj);  // false
delete obj["key"];          // 삭제





/* Map 사용하기 */
const scores = new Map();
scores.set("Junho", 95);
scores.set("Minho", 87);
scores.set("GichuL", 100);

console.log(scores.get("Junho")); // 95
scores.set("Minho", 90);          // 값 수정
console.log(scores.size);         // 3

const map = new Map();
map.set("key", 1);
console.log(map.get("key")); // 1
console.log(map.has("key")); // true
map.delete("key");           // 삭제