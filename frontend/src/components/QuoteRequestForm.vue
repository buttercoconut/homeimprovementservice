<template>
  <form @submit.prevent="submitForm" class="quote-request-form">
    <div class="form-group">
      <label for="homeType">Home Type</label>
      <select id="homeType" v-model="form.homeType" required>
        <option value="kitchen">Kitchen Renovation</option>
        <option value="bathroom">Bathroom Remodel</option>
        <option value="basement">Basement Finishing</option>
        <option value="full">Full Home Renovation</option>
      </select>
    </form-group>
    <div class="form-group">
      <label for="budget">Budget (KRW)</label>
      <input type="number" id="budget" v-model.number="form.budget" required min="0" />
    </div>
    <div class="form-group">
      <label for="description">Description</label>
      <textarea id="description" v-model="form.description" rows="4" required></textarea>
    </div>
    <button type="submit" class="submit-btn">Submit Quote Request</button>
  </form>
</template>

<script setup>
import { reactive, toRefs } from 'vue';
import axios from 'axios';

const form = reactive({
  homeType: 'kitchen',
  budget: 0,
  description: '',
});

const submitForm = async () => {
  try {
    const payload = { ...form };
    // Call backend API (placeholder URL)
    const response = await axios.post('/api/quote-requests', payload);
    emit('submitted', response.data);
  } catch (err) {
    console.error('Error submitting quote request:', err);
  }
};

const emit = defineEmits(['submitted']);
</script>

<style scoped>
.quote-request-form {
  display: flex;
  flex-direction: column;
}
.form-group {
  margin-bottom: 1rem;
}
.submit-btn {
  padding: 0.5rem 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
.submit-btn:hover {
  background-color: #369870;
}
</style>
