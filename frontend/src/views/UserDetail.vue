<template>
    <v-container>
      <v-card>
        <v-card-title>User Details</v-card-title>
        <v-card-text v-if="user">
          <p><strong>Username:</strong> {{ user.username }}</p>
          <p><strong>Roles:</strong> {{ user.roles.join(', ') }}</p>
          <p><strong>Timezone:</strong> {{ user.preferences.timezone }}</p>
          <p><strong>Active:</strong> {{ user.active ? 'Yes' : 'No' }}</p>
          <p><strong>Created At:</strong> {{ formatDate(user.created_ts) }}</p>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="editUser">Edit</v-btn>
          <v-btn color="error" @click="confirmDelete">Delete</v-btn>
        </v-card-actions>
      </v-card>
      <UserModal v-if="showModal" :user="user" @close="closeModal" @saved="fetchUser" />
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import axios from 'axios'
  import UserModal from '../components/UserModal.vue'
  
  const user = ref(null)
  const showModal = ref(false)
  const route = useRoute()
  const router = useRouter()
  
  function fetchUser() {
    axios.get(`http://localhost:5000/users/${route.params.id}`)
      .then(response => { user.value = response.data })
      .catch(error => console.error(error))
  }
  
  onMounted(fetchUser)
  
  function editUser() {
    showModal.value = true
  }
  
  function closeModal() {
    showModal.value = false
  }
  
  function confirmDelete() {
    if (confirm(`Are you sure you want to delete user ${user.value.username}?`)) {
      axios.delete(`http://localhost:5000/users/${user.value._id}`)
        .then(() => router.push('/'))
        .catch(error => console.error(error))
    }
  }
  
  function formatDate(timestamp) {
    return new Date(timestamp * 1000).toLocaleString()
  }
  </script>
  