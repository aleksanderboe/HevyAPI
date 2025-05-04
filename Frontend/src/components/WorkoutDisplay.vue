<template>
  <div class="bg-white shadow-2xl rounded-2xl overflow-hidden">
    <div class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-8">
      <h2 class="text-4xl font-bold">{{ workout.title || 'Untitled Workout' }}</h2>
      <p class="mt-2 text-sm opacity-90">{{ formatDate(workout.start_time) }}</p>
    </div>
    <div class="p-8">
      <WorkoutDetails :workout="workout" />
      <ExerciseList :exercises="workout.exercises" />
      <div class="mt-10 flex justify-end">
        <button
          @click="$emit('refresh')"
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
</template>

<script setup>
import WorkoutDetails from './WorkoutDetails.vue'
import ExerciseList from './ExerciseList.vue'

defineProps({
  workout: {
    type: Object,
    required: true,
  },
})

defineEmits(['refresh'])

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
</script>
