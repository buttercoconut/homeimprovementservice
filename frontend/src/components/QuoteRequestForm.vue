<template>
  <form @submit.prevent="submitForm" class="quote-form">
    <div class="form-group">
      <label for="name">이름</label>
      <input id="name" v-model="form.name" required />
    </div>
    <div class="form-group">
      <label for="email">이메일</label>
      <input id="email" type="email" v-model="form.email" required />
    </div>
    <div class="form-group">
      <label for="budget">예산 (원)</label>
      <input id="budget" type="number" v-model.number="form.budget" required />
    </div>
    <div class="form-group">
      <label for="items">개량 항목 (쉼표로 구분)</label>
      <input id="items" v-model="form.items" required />
    </div>
    <button type="submit">견적 요청</button>
  </form>
</template>

<script setup>
import { reactive, toRefs } from 'vue'
import axios from 'axios'

const form = reactive({
  name: '',
  email: '',
  budget: null,
  items: '',
})

const submitForm = async () => {
  const payload = {
    name: form.name,
    email: form.email,
    budget: form.budget,
    items: form.items.split(',').map(i => i.trim()),
  }
  try {
    const response = await axios.post('http://localhost:8000/api/quote-request', payload)
    emit('submitted', response.data)
  } catch (err) {
    console.error('API error', err)
  }
}

const emit = defineEmits(['submitted'])
</script>

<style scoped>
.quote-form {
  display: flex;
  flex-direction: column;
}
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  box-sizing: border-box;
}
button {
  padding: 0.75rem;
  background: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background: #369870;
}
</style>
