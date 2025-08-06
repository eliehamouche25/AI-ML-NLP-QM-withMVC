// index.js
const mongoose = require('mongoose');

// 1. Connect to MongoDB
mongoose.connect('mongodb://127.0.0.1:27017/quantumDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('✅ Connected to MongoDB');
}).catch(err => {
  console.error('❌ MongoDB connection error:', err);
});

// 2. Define Schema
const particleSchema = new mongoose.Schema({
  name: String,
  mass: Number,
  charge: Number,
  spin: Number,
  quantumNumbers: {
    entangledWith: String,
    state: String
  },
  observations: [{
    result_id: String,
    circuit_id: String,
    counts: {
      shots: Number,
      success: Boolean,
      execution_time: String
    },
    timestamp: String
  }]
});

// 3. Create Model (Collection)
const QuantumParticle = mongoose.model('QuantumParticle', particleSchema);

// 4. CRUD Operations

async function run() {
  // CREATE
  const electron = new QuantumParticle({
    name: "Electron",
    mass: 9.11e-31,
    charge: -1,
    spin: 0.5,
    quantumNumbers: {
      entangledWith: null,
      state: "ground"
    },
    observations: [{
      result_id: "qr_001",
      circuit_id: "qc_001",
      counts: {
        shots: 1024,
        success: true,
        execution_time: "3.2s"
      },
      timestamp: "2025-07-27T14:40:00"
    }]
  });

  await electron.save();
  console.log('🧪 Created Electron:', electron);

  // READ
  const particles = await QuantumParticle.find();
  console.log('🔍 Found Particles:', particles);

  // UPDATE
  const updated = await QuantumParticle.findOneAndUpdate(
    { name: "Electron" },
    { $set: { "quantumNumbers.state": "excited" } },
    { new: true }
  );
  console.log('♻️ Updated Particle:', updated);

  // DELETE
  const deleted = await QuantumParticle.deleteOne({ name: "Electron" });
  console.log('🗑️ Deleted Particle:', deleted);
}

// Run the CRUD sequence
run().then(() => mongoose.connection.close());