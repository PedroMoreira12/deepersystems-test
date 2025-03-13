<template>
  <v-dialog v-model="dialog" max-width="500px" persistent>
    <v-card>
      <v-card-title class="d-flex justify-space-between align-center">
        <span class="headline">{{ isEditMode ? 'Edit User' : 'Create User' }}</span>
        <v-btn icon @click="close">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text>
        <v-form ref="form" @submit.prevent="save">
          <v-text-field
            v-model="formData.username"
            label="Username"
            :rules="[requiredRule]"
            outlined
            class="mb-3"
          />

          <v-text-field
            v-model="formData.password"
            label="Password"
            :type="showPassword ? 'text' : 'password'"
            :rules="[!isEditMode && requiredRule]"
            outlined
            class="mb-3"
            :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append="showPassword = !showPassword"
          />

          <v-text-field
            v-model="formData.preferences.timezone"
            label="Timezone"
            :rules="[requiredRule]"
            outlined
            class="mb-3"
          />

          <v-switch
            v-model="formData.active"
            label="Active"
            color="success"
            inset
          />

      
          
          <v-checkbox v-model="formData.roles" :value="'admin'" label="Admin" />
          <v-checkbox v-model="formData.roles" :value="'manager'" label="Manager" />
          <v-checkbox v-model="formData.roles" :value="'tester'" label="Tester" />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="close">Cancel</v-btn>
        <v-btn text @click="save">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import axios from 'axios'

const props = defineProps({
user: { type: Object, default: null }
})
const emit = defineEmits(['close', 'saved'])

const dialog = ref(true)
const isEditMode = computed(() => props.user && props.user._id)

const formData = ref({
username: '',
password: '',
roles: [],
preferences: { timezone: '' },
active: true,
created_ts: Math.floor(Date.now() / 1000)
})

function close() {
dialog.value = false
emit('close')
}

function save() {
if (isEditMode.value) {
  axios.put(`http://localhost:5000/users/${props.user._id}`, formData.value)
    .then(() => {
      emit('saved')
      close()
    })
    .catch(error => console.error(error))
} else {
  axios.post(`http://localhost:5000/users`, formData.value)
    .then(() => {
      emit('saved')
      close()
    })
    .catch(error => console.error(error))
}
}
</script>