<template>
  <div class="bg-gray-50 dark:bg-gray-700 p-6 rounded-xl shadow-sm transition-colors duration-300">
    <h3 class="text-2xl font-semibold text-gray-900 dark:text-white mb-6">Exercises</h3>
    <div class="space-y-6">
      <div
        v-for="exercise in exercises"
        :key="exercise.exercise_template_id"
        class="bg-white dark:bg-gray-600 p-6 rounded-lg shadow-sm transform transition-all hover:shadow-md hover:scale-[1.02] duration-300"
      >
        <h4 class="text-xl font-semibold text-gray-800 dark:text-white mb-4">
          {{ exercise.title }}
        </h4>
        <ul class="space-y-3">
          <li
            v-for="set in exercise.sets"
            :key="set.index"
            class="bg-white dark:bg-gray-500 p-3 rounded-lg border border-gray-100 dark:border-gray-400 shadow-sm flex items-center justify-between transition-colors duration-300"
          >
            <span class="flex items-center">
              <span
                class="w-8 h-8 flex items-center justify-center rounded-full bg-blue-50 dark:bg-blue-900 text-blue-600 dark:text-blue-300 font-semibold mr-3 transition-colors duration-300"
              >
                {{ set.index + 1 }}
              </span>
              <span class="text-gray-600 dark:text-gray-300">{{ set.reps }} reps</span>
            </span>
            <span v-if="set.weight_kg" class="text-gray-900 dark:text-white font-medium"
              >{{ set.weight_kg }} kg</span
            >
          </li>
        </ul>
      </div>
      <p
        v-if="exercises.length === 0"
        class="text-gray-500 dark:text-gray-400 italic text-center py-4 transition-colors duration-300"
      >
        No exercises recorded.
      </p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  exercises: {
    type: Array,
    required: true,
    default: () => [],
  },
})
</script>
