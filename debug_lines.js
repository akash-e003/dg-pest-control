const fs = require('fs');
const file = 'c:\\\\Users\\\\akash\\\\OneDrive\\\\Desktop\\\\dg pest control\\\\index.html';
const lines = fs.readFileSync(file, 'utf-8').split(/\\r?\\n/);
console.log('Total lines parsed:', lines.length);
for (let i = 735; i <= 745; i++) {
    console.log(`Line ${i + 1}: ^${lines[i].trim()}$`);
}
