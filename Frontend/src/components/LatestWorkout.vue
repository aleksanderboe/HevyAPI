<template>
  <div
    class="min-h-screen bg-gradient-to-b from-blue-50 to-gray-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-5xl w-full space-y-8">
      <!-- Header -->
      <div class="text-center">
        <h1 class="text-5xl font-extrabold text-gray-900 tracking-tight">Latest Workout</h1>
        <p v-if="totalWorkouts !== null" class="mt-3 text-xl text-gray-600">
          Workout {{ totalWorkouts > 0 ? `#${totalWorkouts}` : '' }} of {{ totalWorkouts }} total
          workouts
        </p>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex flex-col items-center justify-center">
        <div class="animate-spin rounded-full h-16 w-16 border-t-4 border-blue-600"></div>
        <p class="mt-4 text-lg text-gray-600">Loading your latest workout...</p>
      </div>

      <!-- Error State -->
      <div
        v-else-if="error"
        class="bg-red-50 border-l-4 border-red-500 text-red-700 p-4 rounded-lg shadow-md"
      >
        <div class="flex">
          <div class="flex-shrink-0">
            <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
              <path
                fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                clip-rule="evenodd"
              />
            </svg>
          </div>
          <div class="ml-3">
            <h3 class="text-lg font-medium">Error</h3>
            <p class="mt-1">{{ error }}</p>
          </div>
        </div>
      </div>

      <!-- Workout Display -->
      <div
        v-else-if="workout"
        class="bg-white shadow-xl rounded-xl overflow-hidden transform transition-all hover:shadow-2xl"
      >
        <div class="bg-blue-600 text-white px-8 py-6">
          <h2 class="text-3xl font-bold">{{ workout.title || 'Untitled Workout' }}</h2>
          <p class="mt-1 text-sm opacity-80">{{ formatDate(workout.start_time) }}</p>
        </div>
        <div class="p-8">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Workout Details -->
            <div>
              <h3 class="text-xl font-semibold text-gray-900">Details</h3>
              <dl class="mt-4 space-y-3">
                <div>
                  <dt class="text-sm font-medium text-gray-500">Duration</dt>
                  <dd class="text-lg text-gray-900">
                    {{ calculateDuration(workout.start_time, workout.end_time) }}
                  </dd>
                </div>
                <div>
                  <dt class="text-sm font-medium text-gray-500">Exercises</dt>
                  <dd class="text-lg text-gray-900">{{ workout.exercises.length }}</dd>
                </div>
                <div>
                  <dt class="text-sm font-medium text-gray-500">Total Sets</dt>
                  <dd class="text-lg text-gray-900">{{ totalSets }}</dd>
                </div>
              </dl>
            </div>
            <!-- Exercises -->
            <div>
              <h3 class="text-xl font-semibold text-gray-900">Exercises</h3>
              <div class="mt-4 space-y-4">
                <div
                  v-for="exercise in workout.exercises"
                  :key="exercise.exercise_template_id"
                  class="bg-gray-50 p-4 rounded-lg"
                >
                  <h4 class="text-lg font-medium text-gray-800">{{ exercise.title }}</h4>
                  <ul class="mt-2 space-y-2 text-sm text-gray-600">
                    <li v-for="set in exercise.sets" :key="set.index">
                      Set {{ set.index + 1 }}: {{ set.reps }} reps @ {{ set.weight_kg }} kg
                    </li>
                  </ul>
                </div>
                <p v-if="workout.exercises.length === 0" class="text-gray-500 italic">
                  No exercises recorded.
                </p>
              </div>
            </div>
          </div>
          <div class="mt-8 flex justify-end">
            <button
              @click="fetchLatestWorkout"
              class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
            >
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                />
              </svg>
              Refresh
            </button>
          </div>
        </div>
      </div>

      <!-- No Workout Found -->
      <div v-else class="text-center py-12">
        <svg
          class="mx-auto h-12 w-12 text-gray-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
        <p class="mt-4 text-lg text-gray-600">No workouts found.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const workout = ref(null)
const totalWorkouts = ref(null)
const loading = ref(false)
const error = ref(null)

const API_BASE_URL = 'http://127.0.0.1:5000/api'

const fetchLatestWorkout = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await fetch(`${API_BASE_URL}/workouts/all?page=1&pageSize=1`, {
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
    const response = await fetch(`${API_BASE_URL}/workouts/count`, {
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

const formatDate = (dateString) => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
  })
}

const calculateDuration = (start, end) => {
  if (!start || !end) return 'N/A'
  const startTime = new Date(start)
  const endTime = new Date(end)
  const diffMs = endTime - startTime
  const minutes = Math.round(diffMs / 60000)
  return `${minutes} minutes`
}

const totalSets = computed(() => {
  if (!workout.value || !workout.value.exercises) return 0
  return workout.value.exercises.reduce((sum, exercise) => sum + (exercise.sets?.length || 0), 0)
})

onMounted(() => {
  fetchLatestWorkout()
  fetchWorkoutCount()
})
</script>
