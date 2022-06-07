<template>
  <div id="shareItem" class="container">
    <div class="row">
      <div class="col">
        <div class="form-group">
          <select class="form-select" v-model="selectedUser">
            <option
              v-for="user in otherUsers"
              :key="user.uid"
              :value="user.uid"
            >
              {{ user.name }}
            </option>
          </select>

          <label for="">Share {{ share }}% of yours</label>
          <input class="form-control" v-model="share" type="range" />

          <button class="btn btn-primary" @click="shareItem">Share</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, shallowRef, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { User, getUsers } from 'app/services/user';

const route = useRoute();
const router = useRouter();

const ownerID = computed(() => {
  return Number.parseInt(route.params['owner'] as string);
});

const itemID = computed(() => {
  return Number.parseInt(route.params['item'] as string);
});

const share = ref(50);
const selectedUser = ref(-1);
const users = shallowRef<User[]>([]);
const otherUsers = computed(() =>
  users.value.filter((user) => user.uid !== ownerID.value)
);

async function shareItem() {
  const request = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      iid: itemID.value,
      originalOwner: ownerID.value,
      newOwner: selectedUser.value,
      share: share.value / 100.0,
    }),
  };

  const response = await fetch('/api/ownerships', request);

  if (response.status == 201) {
    router.back();
  } else {
    alert(response.status);
  }
}

onMounted(async () => {
  users.value = await getUsers();

  if (users.value.length > 0) {
    if (selectedUser.value === -1) {
      for (let i = 0; i < users.value.length; i++) {
        if (users.value[i].uid !== ownerID.value) {
          selectedUser.value = users.value[i].uid;
          break;
        }
      }
    }
  }
});
</script>
