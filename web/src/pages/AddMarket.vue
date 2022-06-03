<template>
  <div id="newMarket" class="container">
    <div class="row">
      <div class="col">
        <div class="form-group">
          <label for="">Name</label>
          <input class="form-control" type="text" v-model="mname" />
          <label for="">Location</label>
          <input class="form-control" type="text" v-model="location" />
          <button class="btn btn-primary" @click="create">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const location = ref('');
const mname = ref('');
const router = useRouter();

async function create() {
  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      mname: mname.value,
      location: location.value,
    }),
  };

  const response = await fetch('/api/markets', request);

  if (response.status == 201) {
    router.back();
  } else {
    alert(response.status);
  }
}
</script>
