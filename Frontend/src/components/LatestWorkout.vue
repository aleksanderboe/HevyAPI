<template>
  <div
    class="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-blue-50 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-6xl w-full space-y-10">
      <WorkoutHeader :total-workouts="totalWorkouts" />

      <LoadingState v-if="loading" />

      <ErrorState v-else-if="error" :error="error" />

      <WorkoutDisplay v-else-if="workout" :workout="workout" @refresh="fetchLatestWorkout" />

      <NoWorkoutFound v-else />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import WorkoutHeader from './WorkoutHeader.vue'
import LoadingState from './LoadingState.vue'
import ErrorState from './ErrorState.vue'
import WorkoutDisplay from './WorkoutDisplay.vue'
import NoWorkoutFound from './NoWorkoutFound.vue'

const workout = ref(null)
const totalWorkouts = ref(null)
const loading = ref(false)
const error = ref(null)

const fetchLatestWorkout = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await fetch('/.netlify/functions/get-workout?page=1&pageSize=1', {
      headers: {
        Accept: 'application/json',
      },
    })
    if (!response.ok) throw new Error('Failed to fetch workout')
    const data = await response.json()
    workout.value = data.workouts[0] || null
  } catch (err) {
    error.value = err.message || 'An error occurred while fetching the workout'
  } finally {
    loading.value = false
  }
}

const fetchWorkoutCount = async () => {
  try {
    const response = await fetch('/.netlify/functions/get-workout-count', {
      headers: {
        Accept: 'application/json',
      },
    })
    if (!response.ok) throw new Error('Failed to fetch workout count')
    const data = await response.json()
    totalWorkouts.value = data.workout_count || 0
  } catch (err) {
    error.value = err.message || 'An error occurred while fetching the workout count'
  }
}

onMounted(() => {
  fetchLatestWorkout()
  fetchWorkoutCount()
})
</script>
