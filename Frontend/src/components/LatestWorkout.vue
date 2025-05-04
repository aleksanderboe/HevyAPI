<template>
  <div
    class="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-blue-50 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-6xl w-full space-y-10">
      <!-- Header -->
      <div class="text-center">
        <h1
          class="text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 tracking-tight"
        >
          Latest Workout
        </h1>
        <p v-if="totalWorkouts !== null" class="mt-4 text-xl text-gray-600 font-medium">
          Workout {{ totalWorkouts > 0 ? `#${totalWorkouts}` : '' }} of {{ totalWorkouts }} total
          workouts
        </p>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex flex-col items-center justify-center space-y-4">
        <div
          class="animate-spin rounded-full h-20 w-20 border-4 border-blue-600 border-t-transparent"
        ></div>
        <p class="text-lg text-gray-600 font-medium">Loading your latest workout...</p>
      </div>

      <!-- Error State -->
      <div
        v-else-if="error"
        class="bg-red-50 border-l-4 border-red-500 text-red-700 p-6 rounded-lg shadow-lg"
      >
        <div class="flex items-start">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-red-500" fill="currentColor" viewBox="0 0 20 20">
              <path
                fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                clip-rule="evenodd"
              />
            </svg>
          </div>
          <div class="ml-4">
            <h3 class="text-lg font-semibold">Error</h3>
            <p class="mt-1">{{ error }}</p>
          </div>
        </div>
      </div>

      <!-- Workout Display -->
      <div v-else-if="workout" class="bg-white shadow-2xl rounded-2xl overflow-hidden">
        <div class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-8">
          <h2 class="text-4xl font-bold">{{ workout.title || 'Untitled Workout' }}</h2>
          <p class="mt-2 text-sm opacity-90">{{ formatDate(workout.start_time) }}</p>
        </div>
        <div class="p-8">
          <!-- Workout Details -->
          <div class="bg-gray-50 p-6 rounded-xl shadow-sm mb-8">
            <h3 class="text-2xl font-semibold text-gray-900 mb-6">Details</h3>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
              <div class="bg-white p-4 rounded-lg shadow-sm">
                <dt class="text-sm font-medium text-gray-500">Duration</dt>
                <dd class="text-xl font-semibold text-gray-900 mt-1">
                  {{ calculateDuration(workout.start_time, workout.end_time) }}
                </dd>
              </div>
              <div class="bg-white p-4 rounded-lg shadow-sm">
                <dt class="text-sm font-medium text-gray-500">Exercises</dt>
                <dd class="text-xl font-semibold text-gray-900 mt-1">
                  {{ workout.exercises.length }}
                </dd>
              </div>
              <div class="bg-white p-4 rounded-lg shadow-sm">
                <dt class="text-sm font-medium text-gray-500">Total Sets</dt>
                <dd class="text-xl font-semibold text-gray-900 mt-1">{{ totalSets }}</dd>
              </div>
            </div>
          </div>
          <!-- Exercises-->
          <div class="bg-gray-50 p-6 rounded-xl shadow-sm">
            <h3 class="text-2xl font-semibold text-gray-900 mb-6">Exercises</h3>
            <div class="space-y-6">
              <div
                v-for="exercise in workout.exercises"
                :key="exercise.exercise_template_id"
                class="bg-white p-6 rounded-lg shadow-sm transform transition-all hover:shadow-md hover:scale-[1.02]"
              >
                <h4 class="text-xl font-semibold text-gray-800 mb-4">{{ exercise.title }}</h4>
                <ul class="space-y-3">
                  <li
                    v-for="set in exercise.sets"
                    :key="set.index"
                    class="bg-white p-3 rounded-lg border border-gray-100 shadow-sm flex items-center justify-between"
                  >
                    <span class="flex items-center">
                      <span
                        class="w-8 h-8 flex items-center justify-center rounded-full bg-blue-50 text-blue-600 font-semibold mr-3"
                      >
                        {{ set.index + 1 }}
                      </span>
                      <span class="text-gray-600">{{ set.reps }} reps</span>
                    </span>
                    <span class="text-gray-900 font-medium">{{ set.weight_kg }} kg</span>
                  </li>
                </ul>
              </div>
              <p
                v-if="workout.exercises.length === 0"
                class="text-gray-500 italic text-center py-4"
              >
                No exercises recorded.
              </p>
            </div>
          </div>
          <div class="mt-10 flex justify-end">
            <button
              @click="fetchLatestWorkout"
              class="inline-flex items-center px-8 py-4 border border-transparent text-lg font-semibold rounded-xl shadow-md text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-300 transform hover:scale-105"
            >
              <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
      <div v-else class="text-center py-16">
        <svg
          class="mx-auto h-16 w-16 text-gray-400"
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
        <p class="mt-6 text-xl text-gray-600 font-medium">No workouts found.</p>
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
