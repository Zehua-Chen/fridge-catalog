<template>
  <div id="updateItem" class="container">
    <div class="row">
      <div class="col">
        <div class="form-group">
          <ItemEditor v-model="item" :supports-date="false"></ItemEditor>
          <button class="mt-4 btn btn-primary" @click="update">Update</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { shallowRef, computed, watchEffect } from 'vue';
import { useRoute, useRouter, onBeforeRouteLeave } from 'vue-router';
import ItemEditor from 'app/components/ItemEditor.vue';
import { Item, getItem, putItem } from 'app/services/item';

const route = useRoute();
const router = useRouter();

const itemID = computed(() => Number.parseInt(route.params['id'] as string));
const item = shallowRef(Item.base);

const stopGettingItem = watchEffect(async () => {
  try {
    console.log(`get item ${itemID.value}`);
    item.value = await getItem(itemID.value);
  } catch (e) {
    alert(e);
    console.error(e);
  }
});

onBeforeRouteLeave(() => {
  stopGettingItem();
});

async function update() {
  await putItem(itemID.value, item.value);
  router.back();
}
</script>
