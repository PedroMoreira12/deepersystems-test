<template>
  <v-container fluid class="background-gradient">
    <v-card class="mt-5 elevation-5" style="border-radius: 15px; background: rgba(255, 255, 255, 0.9);">
      <v-toolbar flat color="primary" dark>
        <v-toolbar-title class="text-h6 font-weight-bold">🔍 User Search</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="white" @click="openCreateModal" class="primary--text">
          <v-icon left>mdi-plus</v-icon>
          Create User
        </v-btn>
      </v-toolbar>

      <v-data-table
        :headers="headers"
        :items="users"
        :search="search"
        class="elevation-0 custom-table"
        :items-per-page="-1"
        :header-props="{ sortByText: 'Sort' }"
        :footer-props="{ itemsPerPageText: 'Items per page' }"
      >
        <template #top>
          <v-text-field
            v-model="search"
            label="Search Users"
            prepend-inner-icon="mdi-magnify"
            class="mx-4 my-2 search-field"
            clearable
            outlined
            rounded
            dense
          ></v-text-field>
        </template>

        <template #[`item.username`]="{ item }">
          <router-link :to="`/users/${item._id}`" class="router-link">
            {{ item.username }}
            <v-icon small color="primary">mdi-open-in-new</v-icon>
          </router-link>
        </template>

        <template #[`item.actions`]="{ item }">
          <v-btn small color="primary" class="mr-2 action-btn" @click="editUser(item)">
            <v-icon left>mdi-pencil</v-icon>
            Edit
          </v-btn>
          <v-btn small color="error" class="action-btn" @click="confirmDelete(item)">
            <v-icon left>mdi-delete</v-icon>
            Delete
          </v-btn>
        </template>

        <template #[`item.active`]="{ item }">
          <v-chip :color="item.active ? 'success' : 'error'" small>
            {{ item.active ? 'Active' : 'Inactive' }}
          </v-chip>
        </template>

        <template #no-data>
          <v-alert type="info" color="primary" border="left" class="ma-4">
            <v-icon left>mdi-information</v-icon>
            No users found.
          </v-alert>
        </template>
      </v-data-table>
    </v-card>

    <UserModal
      v-if="showModal"
      :user="selectedUser"
      @close="closeModal"
      @saved="fetchUsers"
    />
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import UserModal from '../components/UserModal.vue'

const users = ref([])
const showModal = ref(false)
const selectedUser = ref(null)

const search = ref('')

const headers = [
  { title: 'Username', key: 'username' },
  { title: 'Roles', key: 'roles' },
  { title: 'Timezone', key: 'preferences.timezone' },
  { title: 'Is Active?', key: 'active' },
  { title: 'Created At', key: 'created_ts' },
  { title: 'Actions', key: 'actions', sortable: false }
]

const router = useRouter()

function fetchUsers() {
  axios.get('http://localhost:5000/users')
    .then(response => {
      users.value = response.data
    })
    .catch(error => console.error(error))
}

onMounted(fetchUsers)

function openCreateModal() {
  selectedUser.value = null
  showModal.value = true
}

function editUser(user) {
  selectedUser.value = { ...user }
  showModal.value = true
}

function confirmDelete(user) {
  if (confirm(`Are you sure you want to delete user ${user.username}?`)) {
    axios.delete(`http://localhost:5000/users/${user._id}`)
      .then(() => fetchUsers())
      .catch(error => console.error(error))
  }
}

function closeModal() {
  showModal.value = false
}
</script>

<style scoped>
.background-gradient {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  min-height: 100vh;
  padding: 30px;
}

.custom-table {
  border-radius: 0 0 15px 15px;
}

.v-toolbar {
  border-radius: 15px 15px 0 0 !important;
}

.search-field {
  max-width: 400px;
}

.router-link {
  color: #1976d2;
  font-weight: 500;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.router-link:hover {
  color: #115293;
  transform: translateX(3px);
}

.action-btn {
  transition: transform 0.2s ease;
}

.action-btn:hover {
  transform: translateY(-2px);
}

.v-chip {
  font-weight: 500;
  letter-spacing: 0.5px;
}

::v-deep .v-data-table-header {
  background-color: #f8f9fa;
}

::v-deep .v-data-table-header th {
  font-weight: 700 !important;
  color: #2c3e50 !important;
}

::v-deep .v-data-table > .v-data-table__wrapper > table > tbody > tr:nth-of-type(even) {
  background-color: #f8f9fa;
}

::v-deep .v-data-table > .v-data-table__wrapper > table > tbody > tr:hover {
  background-color: #e9ecef !important;
  transition: background-color 0.3s ease;
}
</style>