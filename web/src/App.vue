<template>
  <div id="login" class="container">
    <div class="row mt-4">
      <div class="column">
        <h1 class="text-center">Login</h1>
      </div>
    </div>

    <div id="users" class="row">
      <div class="column d-grid gap-2">
        <a
          class="btn btn-primary"
          v-for="user in users"
          :key="user.uid"
          :href="`/dashboard/${user.uid}`"
        >
          {{ user.name }}
        </a>
      </div>
    </div>

    <!-- create user -->

    <div class="row mt-4">
      <div class="col">
        <h2 class="text-center">Create User</h2>
      </div>
    </div>

    <div id="createUser" class="row">
      <div class="form-group">
        <input
          class="form-control"
          type="text"
          placeholder="User Name"
          v-model="newUserName"
        />
        <input
          class="form-control mt-2"
          type="text"
          placeholder="User ID"
          v-model="newUserID"
        />
      </div>
      <div class="column d-grid gap-2">
        <button class="btn btn-primary mt-2" @click="create">
          Create User
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const users = ref([]);
const newUserName = ref('');

const newUserID = ref('');

async function load() {
  users.value = await fetch('/api/users').then((response) => response.json());
}

async function create() {
  await fetch(`/api/user?name=${newUserName}&uid=${newUserID}`, {
    method: 'POST',
  });
  await load();
}

onMounted(async () => {
  await load();
});
</script>
