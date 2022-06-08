<template>
  <div id="newMethod" class="container">
    <div class="row">
      <div class="column">
        <div class="form-group">
          <label for="">Method</label>
          <input
            class="form-control"
            type="text"
            placeholder="Method"
            v-model="method"
          />
          <button class="btn btn-primary mt-2" @click="create">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const method = ref('');
const router = useRouter();

async function create() {
  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      method: method.value,
    }),
  };

  const response = await fetch('/api/methods', request);

  if (response.status == 201) {
    router.back();
  } else {
    alert(response.status);
  }
}
</script>
