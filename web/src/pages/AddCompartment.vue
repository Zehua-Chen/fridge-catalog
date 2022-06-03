<template>
  <div id="newCompartment" class="container">
    <div class="row">
      <div class="column">
        <div class="form-group">
          <label for="">Level</label>
          <input
            class="form-control"
            type="number"
            placeholder="Level"
            v-model="level"
          />
          <label for="">Temperature</label>
          <input
            class="form-control"
            type="number"
            placeholder="Temperature"
            v-model="temperature"
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

const level = ref(0);
const temperature = ref(0);

const router = useRouter();

async function create() {
  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      clevel: level.value,
      temperature: temperature.value,
    }),
  };

  const response = await fetch('/api/compartment', request);

  if (response.status == 201) {
    router.back();
  } else {
    alert(response.status);
  }
}
</script>
