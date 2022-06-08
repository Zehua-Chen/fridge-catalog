<template>
  <div id="login" class="container">
    <div class="row mt-4">
      <div class="column">
        <h1 class="text-center">Login</h1>
      </div>
    </div>

    <div id="users" class="row">
      <div class="column d-grid gap-2">
        <router-link
          class="btn btn-primary"
          v-for="user in users"
          key="user.uid"
          :to="`/dashboard/${user.uid}`"
        >
          {{ user.name }}
        </router-link>
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
import { getUsers, User } from 'app/services/user';

const users = ref<User[]>([]);
const newUserName = ref('');

const newUserID = ref('');

async function load() {
  users.value = await getUsers();
}

async function create() {
  if (!newUserName.value) {
    alert('Need user name');
    return;
  }

  if (!newUserID.value) {
    alert('Need user id');
    return;
  }

  await fetch(`/api/user?name=${newUserName.value}&uid=${newUserID.value}`, {
    method: 'POST',
  });

  await load();
}

onMounted(async () => {
  await load();
});
</script>
