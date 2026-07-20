<template>

<h2>Student Profile</h2>

<h3>Enrolled Courses</h3>

<div
  v-for="course in store.enrolledCourses"
  :key="course.id"
>

  <p>

    {{ course.name }}

    ({{ course.credits }} Credits)

  </p>

  <button
    @click="store.unenroll(course.id)"
  >
    Remove
  </button>

</div>

<hr>

<h3>

Total Credits :

{{ store.totalCredits }}

</h3>

</template>

<script setup>

import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

</script>