import { createApp } from 'vue';
import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import App from './App.vue';
import Login from './pages/Login.vue';
import Dashboard from './pages/Dashboard.vue';
import AddMarket from './pages/Addmarket.vue';
import AddCompartment from './pages/AddCompartment.vue';
import AddItem from './pages/AddItem.vue';

const routes: RouteRecordRaw[] = [
  { path: '/', component: Login },
  { path: '/dashboard/:id', component: Dashboard },
  { path: '/dashboard/add_market', component: AddMarket },
  { path: '/dashboard/add_compartment', component: AddCompartment },
  { path: '/dashboard/add_item/:id', component: AddItem },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

const app = createApp(App);

app.use(router);
app.mount('#app');
