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
            v-model="name"
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
import { createMethod } from 'app/services/method';

const name = ref('');
const router = useRouter();

async function create() {
  try {
    await createMethod((draft) => {
      draft.name = name.value;
    });
    router.back();
  } catch (e) {
    alert(e);
  }
}
</script>
