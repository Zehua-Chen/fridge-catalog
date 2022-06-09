<template>
  <div id="newMarket" class="container">
    <div class="row">
      <div class="col">
        <div class="form-group">
          <label for="">Name</label>
          <input class="form-control" type="text" v-model="name" />
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
import { createMarket } from 'app/services/market';

const location = ref('');
const name = ref('');
const router = useRouter();

async function create() {
  try {
    await createMarket((draft) => {
      draft.location = location.value;
      draft.name = name.value;
    });
    router.back();
  } catch (e) {
    alert(e);
  }
}
</script>
