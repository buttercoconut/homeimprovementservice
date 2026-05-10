<template>
  <div class="quote-request-view">
    <h2>주택 개량 견적 요청</h2>
    <QuoteRequestForm @submitted="handleSubmitted" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import QuoteRequestForm from '../components/QuoteRequestForm.vue'

const handleSubmitted = (data) => {
  console.log('Quote request submitted:', data)
  // Here you would normally call the backend API
}
</script>

<style scoped>
.quote-request-view {
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
}
</style>
