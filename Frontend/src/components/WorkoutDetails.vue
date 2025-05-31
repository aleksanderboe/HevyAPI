<template>
  <div
    class="bg-gray-50 dark:bg-gray-700 p-6 rounded-xl shadow-sm mb-8 transition-colors duration-300"
  >
    <h3 class="text-2xl font-semibold text-gray-900 dark:text-white mb-6">Details</h3>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
      <div
        class="bg-white dark:bg-gray-600 p-4 rounded-lg shadow-sm transition-colors duration-300"
      >
        <dt class="text-sm font-medium text-gray-500 dark:text-gray-300">Duration</dt>
        <dd class="text-xl font-semibold text-gray-900 dark:text-white mt-1">
          {{ calculateDuration(workout.start_time, workout.end_time) }}
        </dd>
      </div>
      <div
        class="bg-white dark:bg-gray-600 p-4 rounded-lg shadow-sm transition-colors duration-300"
      >
        <dt class="text-sm font-medium text-gray-500 dark:text-gray-300">Exercises</dt>
        <dd class="text-xl font-semibold text-gray-900 dark:text-white mt-1">
          {{ workout.exercises.length }}
        </dd>
      </div>
      <div
        class="bg-white dark:bg-gray-600 p-4 rounded-lg shadow-sm transition-colors duration-300"
      >
        <dt class="text-sm font-medium text-gray-500 dark:text-gray-300">Total Sets</dt>
        <dd class="text-xl font-semibold text-gray-900 dark:text-white mt-1">{{ totalSets }}</dd>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  workout: {
    type: Object,
    required: true,
  },
})

const totalSets = computed(() => {
  if (!props.workout || !props.workout.exercises) return 0
  return props.workout.exercises.reduce((sum, exercise) => sum + (exercise.sets?.length || 0), 0)
})

const calculateDuration = (start, end) => {
  if (!start || !end) return 'N/A'
  const startTime = new Date(start)
  const endTime = new Date(end)
  const diffMs = endTime - startTime
  const minutes = Math.round(diffMs / 60000)
  return `${minutes} minutes`
}
</script>
