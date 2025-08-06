

const fs = require('fs').promises;
const path = require('path');

async function listFiles(folderPath) {
  try {
    const files = await fs.readdir(folderPath);
    console.log('Files in folder:', files);
  } catch (err) {
    console.error('Error reading folder:', err);
  }
}

// Example usage:
listFiles('./myFolder');


// You can recursively print out nested JSON like a tree
function printTree(obj, indent = 0) {
  for (let key in obj) {
    console.log(' '.repeat(indent) + '|-- ' + key);
    if (typeof obj[key] === 'object' && obj[key] !== null) {
      printTree(obj[key], indent + 4);
    }
  }
}
