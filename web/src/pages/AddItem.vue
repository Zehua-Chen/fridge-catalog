<template>
  <div id="newItem" class="container">
    <div class="row">
      <div class="col">
        <div class="form-group">
          <ItemEditor v-model="newItem"></ItemEditor>
          <button class="mt-4 btn btn-primary" @click="create">Create</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ItemEditor from 'app/components/ItemEditor.vue';
import { Item } from 'app/services/item';

const route = useRoute();
const router = useRouter();
const userId = Number.parseInt(route.params['id'] as string);

const newItem = ref(new Item());

async function create() {
  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: newItem.value.name,
      price: newItem.value.price,
      amount: newItem.value.amount,
      calories: newItem.value.calories,
      purchase: new Date(newItem.value.purchase).toLocaleDateString(),
      useBy: new Date(newItem.value.useBy).toLocaleDateString(),
      mname: newItem.value.mname,
      clevel: newItem.value.clevel,
    }),
  };

  const response = await fetch(`/api/items/${userId}`, request);

  if (response.status == 201) {
    router.back();
  } else {
    alert(response.status);
  }
}
</script>
