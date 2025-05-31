<template>
  <div>
    <DarkModeToggle />
    <LatestWorkout />
    <Footer />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import LatestWorkout from './components/LatestWorkout.vue'
import Footer from './components/Footer.vue'
import DarkModeToggle from './components/DarkModeToggle.vue'
import { useDarkMode } from './composables/useDarkMode.js'

const { initializeTheme } = useDarkMode()

onMounted(() => {
  initializeTheme()
})
</script>
