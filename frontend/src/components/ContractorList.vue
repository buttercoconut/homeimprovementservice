<template>
  <div class="contractor-list">
    <h3>Available Contractors</h3>
    <ul>
      <li v-for="contractor in contractors" :key="contractor.id">
        <strong>{{ contractor.name }}</strong> - {{ contractor.specialty }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const contractors = ref([]);

const fetchContractors = async () => {
  try {
    const res = await axios.get('/api/contractors');
    contractors.value = res.data;
  } catch (err) {
    console.error('Failed to load contractors', err);
  }
};

onMounted(fetchContractors);
</script>

<style scoped>
.contractor-list {
  margin-top: 2rem;
}
.contractor-list ul {
  list-style: none;
  padding: 0;
}
.contractor-list li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #ddd;
}
</style>
