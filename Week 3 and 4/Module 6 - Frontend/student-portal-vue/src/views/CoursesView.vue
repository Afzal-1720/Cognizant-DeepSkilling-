<template>

  <h2>Available Courses</h2>

  <input
    v-model="searchTerm"
    placeholder="Search Course"
  />

  <div
    v-for="course in filteredCourses"
    :key="course.id"
    class="course-container"
  >

    <CourseCard
      :name="course.name"
      :code="course.code"
      :credits="course.credits"
      :grade="course.grade"
    />
    

    <RouterLink :to="'/courses/' + course.id">
      <button>View Details</button>
    </RouterLink>

    <button
  @click="store.enroll(course)"
>
  Enroll
</button>

  </div>

</template>

<script setup>

import {

ref,

computed,

onMounted

}

from 'vue'

import { RouterLink } from 'vue-router'

import CourseCard

from '../components/CourseCard.vue'

import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const courses=ref([])

const searchTerm=ref('')

onMounted(()=>{

courses.value=[

{

id:1,

name:'Data Structures',

code:'CS101',

credits:4,

grade:'A'

},

{

id:2,

name:'Java Programming',

code:'CS102',

credits:3,

grade:'A+'

},

{

id:3,

name:'Database Systems',

code:'CS103',

credits:4,

grade:'B+'

},

{

id:4,

name:'Operating Systems',

code:'CS104',

credits:4,

grade:'A'

},

{

id:5,

name:'Web Development',

code:'CS105',

credits:3,

grade:'A+'

}

]

})

const filteredCourses = computed(()=>{

return courses.value.filter(course=>

course.name

.toLowerCase()

.includes(

searchTerm.value.toLowerCase()

)

)

})

</script>